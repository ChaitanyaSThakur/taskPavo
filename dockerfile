FROM python:3.10.5-alpine3.16


COPY ./requirements.txt /app/requirements.txt


WORKDIR /app


RUN pip install -r requirements.txt


copy . /app


ENTRYPOINT [ "python" ]


CMD ["app.py"]
