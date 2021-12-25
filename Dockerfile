FROM python:3.9.7-slim

# If using nginx reverse proxy, set this to the IP of the console
# ENV CONSOLE_IP=13.37.13.37

WORKDIR /opt

EXPOSE 1337

COPY requirements.txt /opt/

RUN python3 -m pip install -r requirements.txt

COPY . /opt/

CMD python3 /opt/app.py
