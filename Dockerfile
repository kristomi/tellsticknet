FROM molobrakos/tellsticknet
ENV LANG C.UTF-8
RUN apt-get install -y bashio

LABEL io.hass.version="VERSION" io.hass.type="addon" io.hass.arch="armhf|aarch64|i386|amd64"

# Copy data for add-on
COPY /config/tellsticknet/tellsticknet.conf /tellsticknet/tellsticknet.conf

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]