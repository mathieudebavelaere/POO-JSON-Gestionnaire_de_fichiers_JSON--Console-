# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

# [ MaJ ] Créer une boucle While pour permettre à l'utilisateur de créer plusieur nouvelle clés et évite de relancer le programme pour chaque clés créer.

import json
from tools_json.json_open_file import open_json_file
from tools_json.json_save_file import save_json_file
from tools_json.json_check_list import check_list_in_json
from tools_json.json_check_str_int import check_str_int
from tools.display_info import display_info_print


# Ajouter des keys et une value général à notre fichier JSON
class Json_key:
    def __init__(self):
        self.query_key = ""
        self.query_value = ""
        self.json_file = None
        self.json_file_name = ""
        self.list_key = []

    def choice_file(self):
            json_list = open_json_file()
            self.json_file = json_list[0]
            self.json_file_name = json_list[1]
            return check_list_in_json(self)

    def key_in_json(self):

        #Afficher la liste des key déjà existante. pour informer l'utilisateur.
        print("\n    Liste des clés déjà existante dans le fichier :\n")
        for file in self.json_file:
            for i, (key,value) in enumerate(file.items()):
                    if key != "id":
                        key_exist = any(key in item for item in self.list_key)
                        if not key_exist:
                            self.list_key.append(key)
                    else:
                        self.key_id = value
        for l in self.list_key:
            print(f"    • {l}")

                        
        display_info_print("Quel et le nom de la clés que vous souhaitez ajouter ?","( Taper 'exit' pour finir et sauvegarder )")
        while True:
            self.query_key = input("    Choix : ").strip().lower()
            if self.query_key.lower() == "exit":
                return self.json_add_key()
            if self.query_key == "":
                display_info_print("[ ERREUR ]",f"Le fichier ne peut pas contenir un champ vide.")
            else:    
                key_exists = any(self.query_key.lower() in item for item in self.json_file)

                if key_exists:
                    display_info_print(f"[ ERREUR ]",f"La clés {self.query_key} existe déjà dans votre liste {self.json_file_name}.json")
                else:
                    display_info_print("Souhaitez-vous ajouter une value générale avec votre clés ? ","( Appuyez sur ENTER pour non )")
                    self.query_value = input("     Choix : ").strip().lower()
                    if len(self.query_value) > 0:
                        self.query_value_check = check_str_int(self.query_value)
                    return self.json_add_key()
 
    def json_add_key(self):
        if self.query_key.lower() != "exit":
            self.count = 0
            for json_file_results in self.json_file:
                try:
                    json_file_results[self.query_key.lower()] = self.query_value_check.lower() if self.query_value else ""
                except:
                    json_file_results[self.query_key.lower()] = self.query_value_check if self.query_value else ""
                self.count += 1
            return self.key_in_json()
        else:
            save_json_file(self.json_file_name,self.json_file)
            display_info_print(f"[ MISE A JOUR ] ",f"{self.count} blocs on était modifiés.")