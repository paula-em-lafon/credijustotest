import requests
import json
import datetime
import pytz
import os

timezone = pytz.timezone("America/Mexico_city")

banxico_api_token = os.environ.get("BANXICO_KEY")

def parse_bdm():
    now = datetime.datetime.now(timezone)
    urlstr = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/" +\
    "oportuno?token=" + banxico_api_token
    try:
        bdmxml = requests.get(urlstr).text
    except:
        raise
    bdmxml = json.loads(bdmxml)
    datadict = bdmxml["bmx"]["series"][0]["datos"][0]
    datedict ={}
    datedict["date"] = now.astimezone(timezone)
    datedict["exc"] = float(datadict["dato"])
    return datedict

if __name__ == '__main__':

    print(parse_bdm())