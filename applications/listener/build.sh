docker build . -t applications/listener
docker image tag applications/listener andrelramos/listener-event-driven-platform:latest
docker push andrelramos/listener-event-driven-platform:latest