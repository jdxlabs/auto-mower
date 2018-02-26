FROM debian:stretch

RUN apt-get update && apt-get install -y python

WORKDIR /wd
COPY inputs inputs
COPY gen_result.py gen_result.py
COPY mower.py mower.py
