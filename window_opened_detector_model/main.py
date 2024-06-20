from os.path import dirname
from pathlib import Path

from keras import Sequential
from keras.src.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.src.legacy.preprocessing.image import ImageDataGenerator

# Directories for your training and validation images
train_data_dir = Path(dirname(__file__), '..', 'data', 'train').absolute()
validation_data_dir = Path(dirname(__file__), '..', 'data', 'validation').absolute()

print(train_data_dir)
print(validation_data_dir)

# Image dimensions
img_width, img_height = 150, 150

# Hyperparameters
epochs = 50
batch_size = 32

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.compile(
    loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy']
)

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=True,
)

test_datagen = ImageDataGenerator(rescale=1. / 255)
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,

)

# Save the model
model.save('../window_detector/model.keras')
