# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from app_json.json_reader import Json_read #_class_Parent
from tools_json.json_open_file import open_json_file
from tools_json.json_save_file import save_json_file
from tools_json.json_missing_key import missing_key_json_file
from tools.display_info import display_info_print
from tools_json.json_check_str_int import check_str_int

class Rename_value_object(Json_read):
    def __init__(self):
        self.query = 0
        self.selected_key = 0
        self.selected_obj = 0
        self.query = ""

    def read_key_in_json(self):
        if len(self.json_file) > 10:
            display_info_print("[ ATTENTION ]",f" votre fichier JSON contient plus de {len(self.json_file)} objets."," Souhaitez-vous quand même charger par paquet de 10 objets ? ( Appuyez sur '0' pour oui )"," Ou rentrer directement le numéro de l'id de l'objet que vous voulez Modifier ?")
            self.query = int(input("    Choix : "))
            if self.query > 1:
                return self.choice_object()
        
        for index, obj in enumerate(self.json_file):
            print("\n" + "•" * 100 + "\n")
            print(f"    INDEX • {index+1}\n")
            for i, (key,value) in enumerate(obj.items()):
                if value == "":
                    value = "non renseigner"
                if key != "id":
                    print(f"    {key} • {value}")
        print("\n" + "•" * 100)
        self.query = 0
        return self.choice_object()

    def choice_object (self):
        while True :
            if self.query == 0:
                display_info_print("Entrez le numéro de l'index de l'objet :","( Appuyez sur '0' pour quitter. )")
            try:
                self.query = int(input("   Choix : "))
            except:
                display_info_print( "[ ERREUR ]","La réponse doit contenir uniquement le numéro.")
            else:
                if self.query == 0:
                    return
                if 1 <= self.query <= len(self.json_file):
                    self.query = self.query -1
                    self.selected_obj = self.json_file[self.query]
                    return self.choice_key()
                else:
                    display_info_print("[ ERREUR ]",f"Le choix doit être compris entre 1 et {len(self.json_file)}.")

    def choice_key (self):
        i=1
        display_info_print(f"Clés disponibles dans l'objet :")
        for obj in self.selected_obj:
            print(f"    {i} • {obj} : {self.selected_obj[obj]}")
            i +=1
        display_info_print("Choisissez la clé à modifier.","( Appuyez sur '0' pour changer d'objet )")
        while True:
            try:
                key_choice = int(input("    choix : "))
                if key_choice == 0:
                    display_info_print(f"Retour à la liste d'objet.")
                    return self.read_key_in_json()

                key_choice = key_choice -1
                self.selected_key = list(self.selected_obj.keys())[key_choice]
            except (IndexError, ValueError):
                display_info_print(f"[ ERREUR ]",f"Le choix de la clé doit être compris entre 1 et {i}.")
            else: 
                display_info_print(f"Entrez la nouvelle valeur pour la clé '{self.selected_key}'.","( Appuyez sur 'Enter' pour quitter )")
                new_value = input("     Choix : ").strip().lower()
                if new_value == "":
                    display_info_print(f"Fin du programme retour au menu principal")
                    return
                return self.save_value(new_value)
                    

    def save_value (self,new_value):
                if len(new_value) > 0:
                    query_value_check = check_str_int(new_value)
                self.selected_obj[self.selected_key] = query_value_check
                display_info_print("[ MISE A JOUR ]",f" de là valeur pour la clé '{self.selected_key}'.")
                save_json_file(self.json_file_name, self.json_file)
                return self.choice_key()