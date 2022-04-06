#!/bin/bash
docker build  -t consumer .
docker run  -d -p 5001:5001 --network mynet consumer
