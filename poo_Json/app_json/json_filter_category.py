# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from app_json.json_reader import Json_read #_class_Parent
from tools_json.json_missing_key import missing_key_json_file
from tools.display_info import display_info_print
from tools.clean_screen_terminal import clear_screen

class Filter_category(Json_read):
    def __init__(self):
        self.list_key = []
        self.list_value = []

    def read_json(self):
        self.user_key = self.list_key[self.user_choice-1]
        display_info_print(f"Voici le(s) résultat(s) de la recherche de la catégorie '{self.user_key}'.")
        #Boucle pour gérer les cas d'érreurs si l'objet n'existe pas dans le fichier se qui évite la relance du programme.
        count_obj = 1
        for file in self.json_file:
                for key,value in file.items():
                    if key == self.user_key:
                        try:
                            value_split = value.split(", ")
                        except :
                            display_info_print(f"[ ERREUR ]",f"L'objet n°{count_obj} à une valeur non conforme.")
                        else:
                            for value in value_split:
                                if value != "":
                                    if value not in self.list_value:
                                        self.list_value.append(value)
                count_obj +=1

        count_key=1
        for l_value in self.list_value:
                if len(l_value) > 0 :
                    print(f"    {count_key} • {l_value}")
                count_key +=1
        
        while True:
                try:
                    display_info_print("Taper le NUMERO que vous souhaitez utiliser pour filtrer votre recherche ?"," (Appuyez sur le nombre '0' pour retourner au menu principal).")
                    query = int(input("     Choix : "))
                except ValueError:
                    display_info_print(f"[ ERREUR ]",f"La réponse ne peut contenir que des chiffres.")
                else:
                    if query == 0:
                        return None
                    if 1 <= query <= count_key-1:
                        if int(query) > 0:
                            #Condition pour l'utilisateur s'il souhaite quitter le programme.
                            # vérifie dans le fichier JSON si il et présent.
                            query_select = self.list_value[int(query)-1]

                            count = sum(1 for item in self.json_file if "id" in item)
                            count_query = sum(1 for item in self.json_file if self.user_key in item)

                            if count  != count_query:
                                display_info_print(f"[ ERREUR ]",f"Nous avons détecter qu'il manquer des clés '{self.user_key}'.")
                                missing_key_json_file(self,self.user_key)
                                return self.read_json()
                            if not query_select:
                                display_info_print(f"[ ERREUR ]",f"La réponse donné doit être compris entre les choix 1 à {count_key-1}.")

                            else:
                                if count  == count_query:
                                    results = self.search_json(query_select,self.user_key)

                                    display_info_print(f"Voici le(s) résultat(s) de la recherche de la catégorie '{query_select}'.")

                                    for json_file_results in results:
                                        self.display_json(json_file_results)

                        else:
                            display_info_print(f"[ ERREUR ]",f"Le mot recherchée ne doit pas contenir moins de une lettres.")
                            
                    else:
                        display_info_print(f"[ ERREUR ]",f"La réponse donné doit être compris entre les choix 1 à {count_key - 1 }.")
