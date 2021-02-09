import os
import redis
import json
from bottle import route, run

RESULT_LIST = "shares"

conn = redis.Redis.from_url(os.getenv("REDIS_HOST", "redis://localhost:6379"))
cache_conn = redis.Redis.from_url(os.getenv("REDIS_CACHE_HOST", "redis://localhost:6379"))

@route('/prices/<share>')
def index(share: str):
    data = cache_conn.get(share)

    if data:
        price = json.loads(data.decode('utf-8'))
        return f"Papel: {price['papel']}<br>Cotação: {price['cotacao']}<br>P/L: {price['price-earnings-ratio']}"

    conn.lpush(RESULT_LIST, share.upper())
    return f'Estamos buscando a cotação do papel <b>{share}</b>. Atualize essa página depois de alguns segundos para obter o resultado!'

run(host='localhost', port=8080)
