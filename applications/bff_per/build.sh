docker build . -t applications/bff_price_earnings_ratio
docker image tag applications/bff_price_earnings_ratio andrelramos/bff_price_earnings_ratio:latest
docker push andrelramos/bff_price_earnings_ratio:latest