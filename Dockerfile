#FROM python:3.9.7-slim
FROM vaultvulp/python-slim-git:3.8

WORKDIR /opt

EXPOSE 1337

COPY requirements.txt /opt/

RUN python3 -m pip install -r requirements.txt

COPY . /opt/

RUN git submodule update --remote

RUN python3 get_last.py

CMD python3 /opt/app.py
