# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json

from app_json.json_reader import Json_read #_class_Parent

from tools_json.json_open_file import open_json_file
from tools_json.json_save_file import save_json_file
from tools_json.json_check_list import check_list_in_json
from tools_json.json_check_str_int import check_str_int
from tools.display_info import display_info_print

class Add_new_object():

    def __init__(self):
        self.list_key = []
        self.key_id = 0

    def choice_file(self):
            json_list = open_json_file()
            self.json_file = json_list[0]
            self.json_file_name = json_list[1]
            return self.check_key_object()

    def check_key_object(self):
        if int(len(self.json_file)) > 0:
            #Boucle for pour parcourir pas tranche de 5 10 20 objects ect ...
            
            for file in self.json_file:
                for i, (key,value) in enumerate(file.items()):
                    if key != "id":
                        key_exist = any(key in item for item in self.list_key)
                        if not key_exist:
                            print(f"{i+1} • {key}")
                            self.list_key.append(key)
                    else:
                        self.key_id = value
                    
            if self.key_id == 0:
                display_info_print( f"[ ERREUR ] ",
                                    f"Votre fichier {self.json_file_name} ne contient aucune key et valeur."
                                    )
                return 
            else:
                display_info_print(f"Voici la list_keye des clés disponible dans le fichier.")
                return self.add_object()
        else:
            display_info_print( "[ ATTENTION ]",
                                " le fichier contient aucun objet dans le fichier.",
                                "[ REDIRECTION ]",
                                "Vers le menu, merci de selectioner le programme :",
                                "-> Créer un nouvelle objet avec une clé et valeur à un fichier vide."
                                )
            display_info_print("Taper 'ENTER' pour retourner sur le menu principal.")
            return_menu = input("    Choix : ").strip()
            if return_menu == "":
                return
            else:
                return

    def add_object(self):
        while True:
            new_object = {}
            new_object["id"] = self.key_id +1
            for name_key in self.list_key:
                if name_key != "id":
                    display_info_print(f"Rentrer la valeur pour {name_key}","( Tapper sur 'ENTER' pour quitter )")
                    value_object = input("     Choix : ").strip().lower()
                    if value_object == "":
                        return
                    
                    query_check = check_str_int(value_object) # Check pour ajouter la valeur en format STR ou INT.
                    new_object[name_key] = query_check
                else:
                    new_object[name_key] = value_object.lower()
            print("\n")
            for key,value in new_object.items(): # Boucle avec la fonction 'items()' pour récupérer ici les clefs de l'ogjet.
                if not key == "id":
                    print(f"{key} : {value}") # Affichage de la liste des clefs à l'utilisateur.

            self.key_id +=1
            self.json_file.append(new_object)
            save_json_file(self.json_file_name,self.json_file)