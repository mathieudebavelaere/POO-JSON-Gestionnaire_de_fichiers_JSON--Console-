# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr
# VERSION : 1.0

# [ Prochainement ] Possibiliter d'exporter dans un fichier 'json' les résultats éffectuer.

from app_json.json_add_key import Json_key
from app_json.json_reader import Json_read
from app_json.json_create_file import Create_json_file
from app_json.json_filter_category import Filter_category
from app_json.json_create_new_object import Create_new_object
from app_json.json_add_object import Add_new_object
from app_json.json_rename_key import Rename_key_object
from app_json.json_rename_value import Rename_value_object
from app_json.json_delete_object import Delete_object
from app_json.json_delete_key import Delete_key_object

from tools.clean_screen_terminal import clear_screen
from tools.display_info import display_info_print


class Menu_json:
       
    def display_menu_json(self):
        #List des commandes JSON.
        list_menu_json =    [
                            {"key":1, "value":"Parcourir un fichier JSON à partir d'une clés.","action": Json_read},
                            {"key":2, "value":"Filtrer par catégories.","action": Filter_category},
                            {"key":3, "value":"Créer un fichier JSON.","action": Create_json_file},
                            {"key":4, "value":"Créer un nouvelle objet avec des clés et des valeurs à un fichier vide.","action": Create_new_object},
                            {"key":5, "value":"Rajouter un ou plusieur nouveaux objets à partir d'un objet déjà existant.","action": Add_new_object},
                            {"key":6, "value":"Créer une nouvelle clé à tout les objets existant du fichier.","action": Json_key},
                            {"key":7, "value":"Renommer une clé sur tout les objets.","action": Rename_key_object},
                            {"key":8, "value":"Supprimer une clé sur tout les objets.","action": Delete_key_object},
                            {"key":9, "value":"Renommer une valeur sur un objet.","action": Rename_value_object},
                            {"key":10, "value":"Supprimer un objet d'un fichier.","action": Delete_object},
                            {"key":0, "value":"Fermer le programme.","action": ""}
                            ]

        display_info_print("Menu JSON")#Fonction print() pour un meilleur affichage automatique et épurée.

        for l in list_menu_json:
            print(f"        {l['key']}\033[94m •\033[0m {l['value']}\n")
        print("•" * 100)
        while True:
            try:
                query_list = int(input("    Choix : "))
            except:
                display_info_print("[ ERREUR ]","La réponse ne peut contenir que des chiffres.")
            else:
                if 0 <= query_list <= len(list_menu_json)-1:
                    if query_list == 0:
                        clear_screen()
                        display_info_print("Merci d'avoir utiliser se programme et à bientôt !","Créer par Debavelaere Mathieu","https://mathieudebavelaere.fr")
                        return
                    for l in list_menu_json:
                        if query_list == l["key"]:
                            return self.lunch_json(l["value"],l["action"])
                    
                else:
                    display_info_print("[ ERREUR ]",f"La réponse donné doit être compris entre les choix 0 à {len(list_menu_json)-1}.\n")

    def lunch_json(self,value,action):
        clear_screen()
        display_info_print(value)
        user = action()
        user.choice_file()
        return self.display_menu_json()


def main():
    clear_screen()
    user = Menu_json()
    user.display_menu_json()