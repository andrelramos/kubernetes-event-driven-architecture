import os
import time
import json

import requests
import redis
from bs4 import BeautifulSoup

LISTENNING_LIST = "prices"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"

# connect with redis server
conn = redis.Redis.from_url(os.getenv("REDIS_HOST", "redis://localhost:6379"))
cache_conn = redis.Redis.from_url(os.getenv("REDIS_CACHE_HOST", "redis://localhost:6379"))


while True:
    if conn.llen(LISTENNING_LIST) > 0:
        price = json.loads(conn.lpop(LISTENNING_LIST).decode('utf-8'))
        print(price)
        url = f"https://fundamentus.com.br/detalhes.php?papel={price['papel']}"
        payload = requests.get(
            url, 
            headers={"User-Agent": USER_AGENT}
        ).text
        soup = BeautifulSoup(payload, 'html.parser')

        result = {
            "price-earnings-ratio": soup.findAll("td", {"class": "data"})[15].text,
            **price
        }

        cache_conn.mset({price["papel"]: json.dumps(result)})

    else:
        print("Nothing to show...")

    time.sleep(1)