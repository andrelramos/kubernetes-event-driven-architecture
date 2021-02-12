import os
import redis
import json
from bottle import route, run

RESULT_LIST = "shares"

conn = redis.Redis.from_url(os.getenv("REDIS_HOST", "redis://localhost:6379"))
cache_conn = redis.Redis.from_url(os.getenv("REDIS_CACHE_HOST", "redis://localhost:6379"))

def get_share_data(share: str):
    data = cache_conn.get(share)

    if data:
        price = json.loads(data.decode('utf-8'))
        return price

    conn.lpush(RESULT_LIST, share.upper())


@route('/search/<share>')
def search(share: str):
    price = get_share_data(share)

    if price:
        return f"Papel: {price['papel']}<br>Cotação: {price['cotacao']}<br>P/L: {price['price-earnings-ratio']}"

    return f'Estamos buscando a cotação do papel <b>{share}</b>. Atualize essa página depois de alguns segundos para obter o resultado!'


@route('/api/search/<share>')
def api_search(share: str):
    price = get_share_data(share)

    if price:
        return {"status": "COMPLETED", **price}
    
    return {"status": "SEARCHING", "papel": share}
    

run(host='0.0.0.0', port=8080)
