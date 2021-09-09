build:
	@docker build -t video-conversion-api .

run:
	@docker run -d -p $(LOCAL_PORT):5000 --name $(CONTAINER_NAME) video-conversion-api

all: build run