# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json

from app_json.json_rename_value import Rename_value_object
from tools_json.json_save_file import save_json_file
from tools.display_info import display_info_print
# ATTENTION sur les choix d'ojet qui ne sont plus cohérent car les id ne se mette pas a jour.!
 
class Delete_object(Rename_value_object):
    def choice_key (self):
        display_info_print(f"Objet sélectionné :")
        for i,(key,value) in enumerate(self.json_file[self.query].items()):
            if key != "id":
                if value == 0: 
                    value = "Iconnue"
                print(f" {key} • {value}")
        return self.delete()

    def delete(self):
        display_info_print(" [ ATTENTION ]"," Toute suppression de L'objet éffacera automatiquement tout se qu'elle contient et sesra irréversible !","Appuyez sur 'y' pour confirmer sinon n'importe quel touche pour annuler.")
        query_del = input(f"    Choix : ").strip().lower()
        if query_del == 'y':
            try:
                del self.json_file[self.query]
                display_info_print(f" [ SUPPRESSION ]",f"Objet à l'index {self.query + 1} supprimé.")
                save_json_file(self.json_file_name, self.json_file)
                return self.read_key_in_json()
            except IndexError:
                display_info_print(f"[ ERREUR ]",f"Aucun objet trouvé à l'index {self.query + 1}.")
        else: 
            display_info_print(f"[ ANNULATION ]",f"De la suppression de l'objet, retour à la liste d'objet.")
            return self.read_key_in_json()

