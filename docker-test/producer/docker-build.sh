#!/bin/bash
docker build -t flask-producer .
#docker network create -d bridge mynet
docker run --network=mynet -d -p  5000:5000 flask-producer
