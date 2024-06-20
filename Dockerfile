FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

RUN apt-get update \
     && apt-get install -y --no-install-recommends \
      pkg-config libhdf5-103 libhdf5-dev python3-h5py gcc \
      libgl1 libglib2.0-0 \
      && pip install poetry

WORKDIR /app
COPY . /app

RUN chmod +x ./entrypoint.sh \
  && poetry config virtualenvs.create false \
  && poetry lock --no-update --no-interaction --no-ansi \
  && poetry install --no-interaction --no-ansi

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/usr/local/bin/ml-window-detector"]
