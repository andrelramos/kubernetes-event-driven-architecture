docker build . -t applications/bff-shares
docker image tag applications/bff-shares andrelramos/bff-shares-event-driven-platform:latest
docker push andrelramos/bff-shares-event-driven-platform:latest