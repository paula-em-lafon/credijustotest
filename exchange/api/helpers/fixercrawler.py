import requests
import json
import datetime
import pytz

timezone = pytz.timezone("America/Mexico_city")

fixer_api_token = "936acc04029dd419e39479e02ca9d673"

def parse_fixer():
    now = datetime.datetime.utcnow()
    try:
        eur_to_usd_str = "http://data.fixer.io/api/latest" +\
            "?access_key=" +fixer_api_token +\
            "&symbols=USD"
    except:
        raise
    eur_to_usd_json = requests.get(eur_to_usd_str).text
    eur_to_usd = json.loads(eur_to_usd_json)["rates"]["USD"]
    try:
        eur_to_mxn_str = "http://data.fixer.io/api/latest" +\
            "?access_key=" +fixer_api_token +\
            "&symbols=MXN"
    except:
        raise
    eur_to_mxn_json = requests.get(eur_to_mxn_str).text
    eur_to_mxn = json.loads(eur_to_mxn_json)["rates"]["MXN"]
    usd_to_mxn = eur_to_mxn/eur_to_usd
    datedict = {}
    datedict["date"] = now.astimezone(timezone)
    datedict["exc"] = usd_to_mxn
    return datedict

if __name__ =='__main__':

    print(parse_fixer())