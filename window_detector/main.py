#!/usr/bin/env python3

"""
This is an API that accepts an image
 and returns true or false if the image contains an opened window
"""
import os

import cv2
import numpy as np
from flask import Flask, jsonify, request
from keras.src.saving import load_model

app = Flask(__name__)

# Load the model
model = load_model(
    os.path.join(os.path.dirname(__file__), 'model.keras')
)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image = request.files['image']
    image.save('image.jpg')

    try:
        # Read the image
        img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
        img = cv2.resize(img, (150, 150))

        # Predict
        prediction = model.predict(np.array([img]))
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        os.remove('image.jpg')
        # Return the prediction
    return jsonify(
        {
            'opened': bool(prediction[0][0] > 0.5),
            'confidence': prediction
        }
    )


def main():
    app.run(host='0.0.0.0', port=8000)
