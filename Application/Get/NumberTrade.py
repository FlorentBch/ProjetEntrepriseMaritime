from ExportData.CsvUse import HeadersCSV, EcritureData
import requests
import time
import json
import datetime
from HTTP.RandomAgent import RandomAgent
from HTTP.CheckerHTTP import RequestChecker

TimeStampATM = int(time.time())

"""Fichier qui permet de récupérer et gérer la liste des number trades
"""

def GetNumberTrade()->list:
    """
    Le but ici est d'avoir la liste des codes des trades. Si le site rajoute un code il sera detecte
    ex: America Service = code=1

    Returns:
        list: Retourne une liste de code de trade
    """
    
    url = 'https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode=0&timestamp='
    CptIterate = 0
    Current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    NomCSV = f"NumberTrade/NumberTrade-{Current_date}.csv"
    ListeElementHeaders = ["ID_TRADE", "NAME_TRADE"]
    code_values = []
    
    # Create the header of the CSV (and create the doc)
    HeadersCSV(NomCSV, ListeElementHeaders)
    
    print("GetNumberTrade() is running =>")
    
    # URL du site en code 0 pour avoir tous les codes disponible
    ParseNumberLine = requests.get(url+str(TimeStampATM), headers=RandomAgent())
        
    # Check if request is 200
    if RequestChecker(ParseNumberLine) == 1:
        
        # Transform the request response to JSON
        data = json.loads(ParseNumberLine.text)
        
        # Appen the value item in the dict
        code_values = [item['code'] for item in data['data']['content']]

        for element in code_values:
            EcritureData(NomCSV, element)
            CptIterate += 1
        
        print(f"    Done with {CptIterate} codes !")
        
    else:
        code_values = ["Response failed"]
        EcritureData(NomCSV, code_values)

    return code_values




