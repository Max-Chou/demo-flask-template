FROM python:3.8

ENV FLASK_APP manage.py
ENV FLASK_CONFIG development

RUN apt-get update && apt-get install -y libmemcached-dev

WORKDIR /home/flask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY manage.py config.py celeryconfig.py boot.sh ./

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]
