FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3-pip libpq-dev
RUN groupadd weatherupdates
RUN useradd weatherupdates -g weatherupdates
RUN mkdir -p /var/log/weatherupdates/ \
	&& chown -R weatherupdates /var/log/weatherupdates/ \
	&& chmod -R u+rX /var/log/weatherupdates/
RUN mkdir -p /opt/weatherupdates
COPY . /opt/weatherupdates/
RUN chmod 755 /opt/weatherupdates/
RUN pip3 install -r /opt/weatherupdates/requirements.txt
WORKDIR /opt/weatherupdates/www/
EXPOSE 8000
USER weatherupdates
