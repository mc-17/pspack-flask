FROM python:3.9.7-slim

WORKDIR /opt

EXPOSE 1337

COPY . /opt/

RUN pip3 install -r requirements.txt

CMD python3 /opt/app.py
