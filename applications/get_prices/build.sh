docker build . -t applications/get-prices
docker image tag applications/get-prices andrelramos/listener-event-driven-platform:latest
docker push andrelramos/listener-event-driven-platform:latest