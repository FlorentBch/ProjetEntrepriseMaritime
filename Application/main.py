from Get.NumberTrade import GetNumberTrade
from Get.ServiceLineCode import GetServiceLineCode
from Get.VesselsParticulars import GetVesselParticulars
from Get.ListCodes import ListAllCodes
from Get.Schedules import GetSchedules
# from Get.EncapsulationTests import MandatoryBeforeStart

if __name__ == '__main__': #and MandatoryBeforeStart() == 0:

    # Récupération des codes régions
    ListeNumberTrade = GetNumberTrade()

    # Récupération des Service Line Code
    ServiceLineCode = GetServiceLineCode(ListeNumberTrade)

    # Récupération des informations sur tous les bateaux
    VesselParticular = GetVesselParticulars(ServiceLineCode)

    # Récupération des codes unique des bateaux
    ListCodes = ListAllCodes(VesselParticular)

    # Récupération de tous les schedules des bateaux entre ports
    Schedules = GetSchedules(ListCodes)

else:
    print("ERREUR DANS UN TEST DE PRE-REQUIS")