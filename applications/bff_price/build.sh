docker build . -t applications/bff-price
docker image tag applications/bff-price andrelramos/bff-price-event-driven-platform:latest
docker push andrelramos/bff-price-event-driven-platform:latest