import time
import random
import requests
import json
import datetime
import os
from ExportData.CsvUse import HeadersCSV, EcritureData
from HTTP.RandomAgent import RandomAgent
from HTTP.CheckerHTTP import RequestChecker
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def GetVesselParticulars(ServiceLineCodes: list) -> dict:
    """
    A la suite de la récupération du code de trade et le code du service line, on récupére pour chaque code de Service line, la liste des colonne suivantes pour tous les navires :
        -> Service	/ Vessel Name / Vessel Code / Lloyds Number / Flag / Year Built / Call Sign

    Returns:
        DictionnaireVessel->dict : Retourne un dictionnaire avec [Clé: Code Service Line + . + Lloyds Number ex: (AWE1.998334) Valeur: Liste d'infos sur le bateau)]
    """
    cpt = 0  # A supprimer en prod, sert à limiter les requêtes

    cptIterate = 0
    DictionnaireVessel = {}
    Current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    NomCSV = f"Vessels/VesselsParticular-{Current_date}.csv"
    Headers = ["serviceLoopAbbrv", "vesselCode", "vesselName",
               "lloydsNumber", "flagCountry", "yearBuilt", "callSign"]
    HeadersCSV(NomCSV, Headers)

    print("GetVesselParticular() is running =>")
    for valeurs in ServiceLineCodes.values():
        for valeur in valeurs:
            # Attente pour ne pas se faire repérer
            TempsEnvoi = int(random.randint(2, 7))
            time.sleep(TempsEnvoi)

            # Parse de tous les navires avec leurs infos
            ParseVesselAll = requests.get(
                'https://elines.coscoshipping.com/ebbase/public/vesselParticulars/search?pageSize=9999&state=lines&code='+str(valeur), headers=RandomAgent())

            if RequestChecker(ParseVesselAll) == 1:
                # Transformation de la requête en JSON
                data = json.loads(ParseVesselAll.text)

                # Vérification du contenu de la page afin de ne pas récupérer une page vide
                if data['data']['content'] is None:
                    DictionnaireVessel[valeur] = ["Null"]
                    EcritureData(NomCSV, [valeur, "Null"])
                else:
                    # Pour chaque element dans la structure JSON donné, on ajoute dans le dictionnaire les valeurs
                    for item in data['data']['content']:
                        DictionnaireVessel[valeur+"." +
                                           item['lloydsNumber']] = item
                        ListeElements = [item["serviceLoopAbbrv"], item["vesselCode"], item["vesselName"],
                                         item["lloydsNumber"], item["flagCountry"], item["yearBuilt"], item["callSign"]]
                        EcritureData(NomCSV, ListeElements)
                        cptIterate += 1

        #         cpt += 1  # A supprimer en prod, sert à limiter les requêtes
        #         if cpt >= 2:
        #             break
        #     cpt += 1
        #     if cpt >= 2:
        #         break  # A supprimer en prod, sert à limiter les requêtes

        # cpt += 1  # A supprimer en prod, sert à limiter les requêtes
        # if cpt >= 2:
        #     break

    print(f"    Done with {cptIterate} vessels !")
    # Sortie des données dans un JSON

    return (DictionnaireVessel)
