CONFIG_PATH=/data/options.json
MQTT_HOST=$(bashio::services mqtt "host")
MQTT_USER=$(bashio::services mqtt "username")
MQTT_PASSWORD=$(bashio::services mqtt "password")

export MQTT_URL = "http://$MQTT_USER:$MQTT_PASSWORD@$MQTT_HOST"


dumb-init -- python3 -m tellsticknet mqtt