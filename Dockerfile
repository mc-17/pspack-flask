FROM python:3.9.7-slim

WORKDIR /opt

EXPOSE 1337

COPY requirements.txt /opt/

RUN python3 -m pip install -r requirements.txt

RUN git submodule update --remote

RUN python3 get_last.py

COPY . /opt/

CMD python3 /opt/app.py
