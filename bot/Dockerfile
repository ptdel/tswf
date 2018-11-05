FROM python:alpine

WORKDIR /bot

ENV NICKNAME=tswf
ENV PASSWORD=
ENV IRC_SERVER=irc.rizon.net
ENV QUEUE_URL="https://hackerchan.org/api/submit"

COPY requirements.txt ./

RUN apk add --no-cache \
    build-base  \
    libffi-dev  \
    python-dev  \
    openssl-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "bot" ]
