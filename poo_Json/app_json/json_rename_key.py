# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools_json.json_open_file import open_json_file
from tools_json.json_save_file import save_json_file
from tools_json.json_check_list import check_list_in_json
from tools_json.json_missing_key import missing_key_json_file
from tools.display_info import display_info_print

# Ajouter une fonction pour que la clé renommer reste au même endroit est ne se retrouve pas en fin de la list de l'objet après modification. gérer l'index de la clé.
# Ajouter une fonction pour que si la clé existe déjà ne pas la prendre en compte !

class Rename_key_object:
    def __init__(self):
        self.list_key = []

    def choice_file(self):
            json_list = open_json_file()
            self.json_file = json_list[0]
            self.json_file_name = json_list[1]
            return check_list_in_json(self)

    def key_in_json(self):
        for file in self.json_file:
            for key,value in file.items():
                if not key == 'id':
                    if key not in self.list_key:
                        self.list_key.append(key)
                            
        count_key=1
        for l_value in self.list_key:
            print(f"{count_key} • {l_value}")
            count_key +=1
        
        while True:
                        display_info_print("Taper le NUMERO de la clé sur vous souhaitez Modifier ?","(Appuyez sur le nombre '0' pour retourner au menu principal).")
                        try:
                            query = int(input("     Choix : "))
                        except ValueError:
                            display_info_print(f"[ ERREUR ] la réponse ne peut contenir que des chiffres.")
                        else:
                            if query == 0:
                                return None
                            if 1 <= query <= count_key-1:
                                if int(query) > 0:
                                    query_select = self.list_key[int(query)-1]



                                    count = sum(1 for item in self.json_file if "id" in item)
                                    count_query = sum(1 for item in self.json_file if query_select in item)

                                    if count  != count_query:
                                        display_info_print(f" ERREUR ] Nous avons détecter qu'il manquer des key '{query_select}' à vos objet(s).")
                                        missing_key_json_file(self,query_select)
                                        return self.key_in_json()
                                    if not query_select:
                                        display_info_print(f"[ ERREUR ] La réponse donné doit être compris entre les choix 1 à {count_key-1}.")

                                    display_info_print(f"Vous avez selectioner le clé : {query_select}","Taper votre nouvelle clé."," (Taper sur le nombre '0' puis valider pour retourner au menu principal)")
                                    query_rename = str(input("  Choix : ")).strip().lower()
                                    if query_rename == "":
                                        display_info_print("[ ERREUR ]",f"La clé ne peut pas contenir un champ vide.")
                                    elif query_rename == "0":
                                        return
                                    else:    
                                        # Étape de renommage
                                        for obj in self.json_file:
                                            if query_select in obj:
                                                obj[query_rename] = obj.pop(query_select)
                                                # si dessus la fonction 'pop() va retirer la valeur des clefs pour ajouter la nouvelle.

                                        # Sauvegarder les modifications dans le fichier
                                        save_json_file(self.json_file_name, self.json_file)

                                        display_info_print(f"[ INFO ] La clé '{query_select}' a bien été renommée en '{query_rename}' dans tous les objets.")
                                          

                                else:
                                    display_info_print(f"[ ERREUR ] Le mot recherchée ne doit pas contenir moins de une lettres.")
                            else:
                                display_info_print(f"[ ERREUR ] La réponse donné doit être compris entre les choix 1 à {count_key-1}.")