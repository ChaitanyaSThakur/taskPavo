RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz

FROM python:3.10.5-alpine3.16


COPY ./requirements.txt /app/requirements.txt


WORKDIR /app


RUN pip install -r requirements.txt


copy . /app


ENTRYPOINT [ "python" ]


CMD ["app.py"]
