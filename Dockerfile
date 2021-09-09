FROM python:3.8
COPY . /app
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y ffmpeg && \
    pip install -r requirements.txt

ENV FLASK_APP main.py

EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0" ]