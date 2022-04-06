FROM python:3.8

EXPOSE 5000

WORKDIR  /app

COPY /templates /app/templates

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

RUN chmod +x /app

CMD python3 producer.py
