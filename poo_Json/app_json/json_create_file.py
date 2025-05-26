# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import os
import json
from tools.display_info import display_info_print

class Create_json_file:

    def choice_file(self):
        while True:
            display_info_print("Nom du fichier à créer (sans l'extension '.json')"," (Taper sur le nombre '0' puis valider pour retourner au menu principal)")
            query_json_file = str(input("    Choix : ")).strip().lower()
            file_exist = f"./json/{query_json_file}.json"
            if str(query_json_file) == "":
                display_info_print("[ ERREUR ]",f"Le fichier ne peut pas contenir un champ vide.")
            elif os.path.exists(file_exist):
                display_info_print("[ ERREUR ]",f"Le fichier '{query_json_file}.json' existe déjà.")
            elif query_json_file == "0":
                return
            else:
                try:
                    with open(f"./json/{query_json_file}.json", "w") as f:
                        json.dump([], f, indent=4)
                except Exception as e:
                    display_info_print(f"[ ERREUR ]",f"{e}")
                else:
                    display_info_print("[ SUCCES ]",f"Le fichier '{query_json_file}.json' à été créé avec succès dans le dossier 'json'.")
                    return