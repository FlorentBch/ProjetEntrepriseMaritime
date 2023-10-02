# Encapsulation des phases de test avant de commencer le programme
from DataBase.CheckerDB import ConnectDB_Checker
from HTTP.CheckerHTTP import RequestChecker
from HTTP.RandomAgent import RandomAgent
import requests

def MandatoryBeforeStart():
    """
    Sert à vérifier que tout fonctionne comme il faut, les prérequis sont les suivant : Connexion à la BDD et Connexion à l'URL 

    Returns:
        CalculChecker : Return le nombre d'erreurs, si 0 à la sortie c'est OK pour continuer le programmes
    """
    CalculChecker = 0
    
    # Vérification de la connexion à la bdd
    if ConnectDB_Checker() == "OK":
        CalculChecker += 0
    else :
        CalculChecker += 1
    
    # Verification for the connection to the WebSite
    request = requests.get('https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode=0', headers=RandomAgent())
    if RequestChecker(request) == 1:
        CalculChecker += 0
    else :
        CalculChecker += 1

    return CalculChecker