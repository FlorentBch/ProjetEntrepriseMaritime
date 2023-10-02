import csv
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  

def HeadersCSV(NomDocument:str, Headers:list)->None:
    """Ecriture de l'entete CSV
    """
    try:
        os.mkdir(os.getenv("PATH_CSV"))
    except OSError as e:
        with open(os.getenv("PATH_CSV")+ NomDocument, 'w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(Headers)

def EcritureData(NomDocument, ListeHeaders:list):
    """Fonction d'ecrire de données dans le fichier CSV afin de sauvegarder les données scrapé
    Args:

    """
    try:
        os.mkdir(os.getenv("PATH_CSV"))
    except OSError as e:
        with open(os.getenv("PATH_CSV")+NomDocument, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(ListeHeaders)
            file.close()