FROM python:3.8-alpine
COPY . /app
WORKDIR /app

RUN apk update && \
    apk add ffmpeg && \
    pip install -r requirements.txt

EXPOSE 5000
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "5", "wsgi:app" ]