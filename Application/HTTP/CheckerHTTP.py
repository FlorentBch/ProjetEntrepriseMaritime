import requests
from time import sleep
def RequestChecker(r:requests)->int:
    """Request checker for catch HTTP error 

    Args:
        r (requests): Request for parse the website

    Returns:
        int: if ValueResponse == 1 OK Else it's an error
    """
    ValueResponse = 0
    
    try:
        r.raise_for_status()
        ValueResponse = 1
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        ValueResponse = 2
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting (Connection Refused):",errc)
        sleep(600)
        ValueResponse = 3
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        ValueResponse = 4
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        ValueResponse = 5

    return ValueResponse