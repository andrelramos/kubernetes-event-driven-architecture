docker build . -t applications/get-price-earnings-ratio
docker image tag applications/get-price-earnings-ratio andrelramos/price-earnings-ratio-event-driven-platform:latest
docker push andrelramos/price-earnings-ratio-event-driven-platform:latest