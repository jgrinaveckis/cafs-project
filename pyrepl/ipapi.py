import logging
import sys
import requests

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

def getIpJson(ip:str) -> dict:
    resp = requests.get(f'https://ipapi.co/{ip}/json/')

    #client errors
    if resp.status_code >= 400:
        raise Exception(f'Status code: {resp.status_code}, reason: {resp.reason}')

    data = resp.json()
    if 'error' in data:
        logging.info(f'There was an error in request, reason being: {data["reason"]}')
        return None
    
    return {
            "ip": data["ip"],
            "lat": data["latitude"],
            "lon":data["longitude"],
            "city": data["city"],
            "region": data["region_code"],
            "country_code": data["country_code"],
            "country_name": data["country_name"]
        }
