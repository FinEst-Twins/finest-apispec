FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

#ENTRYPOINT ["python3"]

#CMD ["-m", "swagger_server"]

CMD gunicorn --bind 0.0.0.0:8080 swagger_server.__main__:application