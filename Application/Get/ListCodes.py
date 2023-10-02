"""Fichier qui permet de récupérer et gérer la liste des codes 
"""

def ListAllCodes(VesselParticulars:dict)->dict:
        """_summary_

        Args:
            VesselParticulars (dict): Récupération de toutes les infos des bateaux grâce à la méthode GetVesselParticulars()

        Returns:
            dict: Sortie d'un dictionnaire, pour chaque bateau, retourne uniquement son Code Vessel
        """
        ListCode = {}
        for Vessel in VesselParticulars.values():
            if Vessel != ["Null"]:
                ListCode[Vessel['serviceLoopAbbrv']+"."+Vessel['lloydsNumber']] = Vessel['vesselCode']
        return ListCode