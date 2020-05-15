FROM python:3.8-alpine
RUN set -xe && apk add --update --no-cache smartmontools curl && pip install requests && rm -rf /tmp/* /var/tmp/
COPY smartd.conf /etc/smartd.conf
COPY google_chat.py /etc/smartd_warning.d/google_chat
CMD /usr/sbin/smartd --debug