# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.self.self.count_key
# https://mathieudebavelaere.fr

import json
from app_json.json_reader import Json_read #_class_Parent
from tools_json.json_save_file import save_json_file
from tools.display_info import display_info_print

class Delete_key_object(Json_read):
    def choice_key(self):
        while True:
            self.count_key = 1
            for file in self.json_file[0:1]: #Boucle sur le premier objet pour récupérer les information à l'interieur.
                for i , (key,value) in enumerate(file.items()): #Boucle avec la fonction 'items()' pour récupérer ici les clefs de l'objet.
                    print(f"        {i +1} • {key}") #Affichage de la liste des clefs à l'utilisateur.
                    key_any = any([True if key in self.list_key else False for d in self.list_key])#Vérifie si il est déjà présent dans la liste afin d'éviter les doublons.
                    if not key_any:
                        self.list_key.append(key) #Ajout des clefs dans une liste a part.
                    self.count_key +=1
            display_info_print("Taper le numéro de la key que vous souhaitez SUPPRIMER.","(Appuyez sur le nombre '0' pour retourner au menu principal)")
            try:
                user_choice = int(input("   Choix : "))
            except:
                display_info_print( "[ ERREUR ]"," La réponse doit contenir uniquement le numéro.")
            else:
                if user_choice == 0:
                        return None
                if user_choice == 1:
                    display_info_print( "[ ERREUR ]","Impossible de suprimer l'id des objets.")
                else:
                    if 1 <= user_choice <= self.count_key-1:
                        return self.delete_key(user_choice)
                    else:
                        display_info_print(f"[ ERREUR ]",
                                        f"La réponse donné doit être compris entre les choix 1 à {self.count_key-1}.")
    
    def delete_key (self,user_choice):
        user_key = self.list_key[user_choice-1]
        display_info_print(f"[ ATTENTION ]",f" Toute suppression des clefs '{user_key}' sera irréversible ainsi que leurs valeurs !","Appuyez sur 'y' pour confirmer sinon n'importe quel touche pour annuler.")
        query_del = input("     Choix : ").strip().lower()
        if query_del.lower() == 'y':
            try:
                for obj in self.json_file:
                    del obj[user_key]
                display_info_print(f"[ SUPPRESSION ]",
                                    f" De là clé '{user_key}'.")

                save_json_file(self.json_file_name, self.json_file)
                return self.read_key_in_json()
            except IndexError:
                display_info_print("[ ERREUR ]",
                                    f" Aucune clé n'a été trouvé à l'index {user_choice - 1}.")
        else: 
            display_info_print("[ ANNULATION ]",
                                " de la suppression de l'objet, retour au menu.")
            return self.read_key_in_json()
       