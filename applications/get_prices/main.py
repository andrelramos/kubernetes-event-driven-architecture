import os
import time
import json

import requests
import redis
from bs4 import BeautifulSoup

LISTENNING_LIST = "shares"
RESULT_LIST = "prices"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"

# connect with redis server
conn = redis.Redis.from_url(os.getenv("REDIS_HOST", "redis://localhost:6379"))


while True:
    if conn.llen(LISTENNING_LIST) > 0:
        share = conn.lpop(LISTENNING_LIST).decode('utf-8')
        print(share)
        url = f"https://fundamentus.com.br/detalhes.php?papel={share}"
        payload = requests.get(
            url, 
            headers={"User-Agent": USER_AGENT}
        ).text

        soup = BeautifulSoup(payload, 'html.parser')

        result = {
            "cotacao": soup.findAll("td", {"class": "destaque"})[1].text,
            "papel": share,
        }

        conn.lpush(RESULT_LIST, json.dumps(result))

    else:
        print("Nothing to show...")

    time.sleep(1)