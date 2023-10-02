import time
import random
import requests
import json
import datetime
from ExportData.CsvUse import HeadersCSV, EcritureData
from HTTP.RandomAgent import RandomAgent
from HTTP.CheckerHTTP import RequestChecker

TimeStampATM = int(time.time())

def GetServiceLineCode(NumberTrades: list) -> dict:
    """
        Nous récuperons ici les codes des Service Lines grâce au code des Trades précedemment récupéré via la fonction GetNumberTrade()
        URL : https://elines.coscoshipping.com/ebusiness/vesselParticulars/vesselParticularsByServices

        Returns:
            ListAllElements->dict() : Retourne la liste de tous les codes des service line en Dictionnaire [cle: Code Trade, Valeur: list(Code Service Line)]
        """

    url = 'https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode='
    ListAllElements = {}
    Current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    NomCSV = f"ServiceLineCode/ServiceLineCode-{Current_date}.csv"
    ListeElementsHeaders = ["ID_SERVICE", "NAME_SERVICE", "CODE_SERVICE"]
    cpt = 0

    # Définition du header CSV
    HeadersCSV(NomCSV, ListeElementsHeaders)

    print("GetServiceLineCode() is running =>")

    for code in (NumberTrades):
            # Fonctionnalité de temporisation
            time.sleep(random.randint(2, 7))

            # Parsing de l'url avec les codes precedemment récupéré via la fonction GetNumberLine()
            ParseServiceLine = requests.get(
                url+str(code)+'&timestamp='+str(TimeStampATM), headers=RandomAgent())

            if RequestChecker(ParseServiceLine) == 1:
                # Transformation de la requête en JSON
                data = json.loads(ParseServiceLine.text)

                # Récupération du contenu des items 'code' dans le JSON
                code_values = [item['code']
                for item in data['data']['content']]

                for element in data['data']['content']:
                    cpt += 1
                    ListeElementsWrite = [cpt, element['code'], code]

                    EcritureData(NomCSV, ListeElementsWrite)

                # Ajout des valeurs dans un dictionnaire avec Clé : le numero de ligne et la valeur le code de Service
                ListAllElements[str(code)] = code_values
            else:
                ListAllElements[str(code)] = ["Response failed"]
                EcritureData(NomCSV, ListAllElements[str(code)])

    print(f"    Done with {cpt} service lines !")

    return ListAllElements
