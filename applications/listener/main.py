import os
import redis
import time

RLIST = "events"

# connect with redis server
conn = redis.Redis.from_url(os.getenv("REDIS_HOST", "redis://localhost:6379"))


while True:
    if conn.llen(RLIST) > 0:
        message = conn.lpop(RLIST)
        if message:
            print(f"Received: {message}")
    else:
        print("Nothing to show...")

    time.sleep(1)