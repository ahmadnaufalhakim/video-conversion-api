FROM python:3.8-alpine
COPY . /app
WORKDIR /app

RUN apk update && \
    apk add ffmpeg && \
    pip install -r requirements.txt

ENV FLASK_APP main.py

EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0" ]