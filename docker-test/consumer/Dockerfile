FROM python:3.8
  
WORKDIR  /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

RUN chmod +x /app

CMD python3 consumer.py

