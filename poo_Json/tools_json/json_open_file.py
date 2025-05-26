# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools.display_info import display_info_print
from tools.clean_screen_terminal import clear_screen
import os

def open_json_file():
    json_dir = "./json"

    fichiers = [f for f in os.listdir(json_dir) if f.endswith('.json')]
    if not fichiers:
        display_info_print("[ ERREUR ] Aucun fichier JSON trouvé dans le dossier.","[ REDIRECTION ]","Merci de créer un fichier 'json' avec l'outil disponible.","--> Créer un fichier JSON")
        return
    else:
        for i, nom in enumerate(fichiers, start=1):
            print(f"    {i} • {nom}")
        display_info_print("Quel fichier voulez-vous ouvrir ? ( Numéro demander )")
    while True:
        try:
            # L'utilisateur peut choisir sont fichier.
            query = int(input("     Choix : "))
            
        except ValueError:
            display_info_print(f"[ ERREUR ]",f"La réponse ne peut contenir que des chiffres.")
        else:
            if 1 <= query <= i :
                json_file_name = fichiers[query - 1]

                chemin_fichier = os.path.join(json_dir, json_file_name)

                with open(chemin_fichier, "r") as f:
                    file_json = json.load(f)

                display_info_print(f"[ SUCCES ]",f"Lecture du fichier '{json_file_name}.json'.")

                return file_json,json_file_name
            else:
                display_info_print(f"[ ERREUR ]",f"La réponse donné doit être compris entre les query 1 à {i}.")
                
            
