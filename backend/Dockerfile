FROM python:3.7-slim

RUN apt-get update
RUN apt-get install libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx -y

ENV INSTALL_PATH /backend
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

