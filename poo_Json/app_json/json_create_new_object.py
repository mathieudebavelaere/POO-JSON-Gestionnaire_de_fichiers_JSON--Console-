# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools_json.json_open_file import open_json_file
from tools_json.json_save_file import save_json_file
from tools_json.json_check_str_int import check_str_int
from app_json.json_add_object import Add_new_object
from tools.display_info import display_info_print

class Create_new_object:

    def choice_file(self):
            json_list = open_json_file()
            self.json_file = json_list[0]
            self.json_file_name = json_list[1]
            return self.new_object()

    #__ Ajouter une fonction pour savoir si l'utilistateur veut récupérer les clés déjà existante pour rajouter une nouvelle données (ex: ajouter un deuxième utilisateur )
    
    def new_object(self):
            if int(len(self.json_file)) > 0:
                display_info_print( "[ ATTENTION ]",
                                    " le fichier contient déjà des objets dans le fichier.",
                                    "[ REDIRECTION ]",
                                    " vers le menu, merci de selectionner le programme :",
                                    "-> Rajouter un ou plusieur nouveaux objets à partir d'un objet déjà existant"
                                    )
                display_info_print("Taper 'ENTER' pour retourner sur le menu principal.")
                return_menu = input("   Choix : ")
                if return_menu == "":
                    return
                else:
                    return

            new_list = {}
            id_exist = 0
            for l in self.json_file:
                id_exist = l['id']

            if id_exist:
                new_list['id'] = id_exist +1
            else:
                new_list['id'] = 1
                
            while True:
                display_info_print("Quel et le nom de la clé que vous souhaitez créer ?","( Taper 'exit' pour finir et sauvegarder )")
                query_key = input("     Choix : ").strip().lower()
                
                if len(query_key.replace(" ","")) != 0:

                    if query_key.lower() == "exit":
                        if len(new_list) > 0:
                            self.json_file.append(new_list)
                            save_json_file(self.json_file_name,self.json_file)
                            return

                    display_info_print("Souhaitez-vous ajouter une value générale avec votre clé ?","( Appuyez sur ENTER pour non )")
                    query_value = input("   Choix : ").strip().lower()
                    
                    if query_value != '':
                        query_check = check_str_int(query_value) # Check pour ajouter la valeur en format STR ou INT.
                        new_list[query_key] = query_check
                    else:
                        new_list[query_key] = query_value
                    
                    print("\n" + "•" * 100 + "\n")
                    for i, (key,value) in enumerate(new_list.items()):
                        if str(value) == "":
                            print(f"    {key}  •  Non renseigner ")
                        else:
                            print(f"    {key}  •  {value}")

                    
                else:
                    display_info_print("[ ERREUR ]","Vous ne pouvez pas créer une clé avec un champ vide")