from bs4 import BeautifulSoup
import requests
import datetime
import json

def parse_dof():
    now = datetime.datetime.now()
    fourteen_days = now - datetime.timedelta(days = 14)
    urlstr = "https://www.dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador" +\
        "=158&dfecha=" + str(fourteen_days.day).zfill(2) + \
        "%2F"+ str(fourteen_days.month).zfill(2) +"%2F" + str(fourteen_days.year) + \
        "&hfecha=" + str(now.day).zfill(2) + "%2F" + str(now.month).zfill(2) +\
         "%2F" + str(now.year)
    dofhtml = requests.get(urlstr).text
    soup = BeautifulSoup(dofhtml, 'html.parser')
    exchangedates = soup.findAll("tr", class_="Celda 1")
    firstdate = exchangedates[-1]
    firstdate = [x.text for x in firstdate.find_all('td')]
    datedict ={}
    datedict["date"] = now
    datedict["exc"] = float(firstdate[1])
    return datedict

if __name__ == '__main__':

    print(parse_dof())