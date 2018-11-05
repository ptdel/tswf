FROM python:alpine

WORKDIR /player

VOLUME /songs

COPY requirements.txt ./

RUN apk add --no-cache \
    build-base  \
    libffi-dev  \
    python-dev  \
    openssl-dev \
    ffmpeg

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "player" ]
