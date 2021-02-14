import os
import requests
from bottle import route, run

SHARES_API_ROUTE = os.getenv("SHARES_API_ROUTE")

@route('/api/per/<share>')
def index(share: str):
    payload = requests.get(f"{SHARES_API_ROUTE}/api/search/{share}?version=v1").json()

    return {
        "share": share,
        "status": payload.get("status"),
        "price-earnings-ratio": payload.get("price-earnings-ratio", ""),
    }
    
run(host='0.0.0.0', port=8080)
