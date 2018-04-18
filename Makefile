IMAGE=molobrakos/tellsticknet

docker-build:
	docker build -t $(IMAGE) .

docker-run-mqtt:
	docker run \
	        --name tellsticknet \
		--restart always \
		--detach \
		--net=host \
		-v $(HOME)/.config/mosquitto_pub:/app/.config/mosquitto_pub:ro \
		-v $(HOME)/.tellsticknet.conf:/app/tellsticknet.conf:ro \
		$(IMAGE) ./script/tellsticknet mqtt -vv

docker-run-mqtt-term:
	docker run \
		-ti --rm \
		--net=host \
		-v $(HOME)/.config/mosquitto_pub:/app/.config/mosquitto_pub:ro \
		-v $(HOME)/.tellsticknet.conf:/app/tellsticknet.conf:ro \
		$(IMAGE) ./script/tellsticknet mqtt -vv
