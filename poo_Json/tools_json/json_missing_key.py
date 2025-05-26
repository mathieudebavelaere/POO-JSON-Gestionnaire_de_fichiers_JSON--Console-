# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools_json.json_save_file import save_json_file
from tools.display_info import display_info_print

def missing_key_json_file(self,user_key):
        counts_missing = 0
        for j_file in self.json_file:
            if str(user_key) not in j_file:
                j_file[str(user_key)] = ""  # Valeur vide ou par défaut
                counts_missing += 1
        display_info_print("[ MISE A JOUR ]",f" éffectuer, {counts_missing} bloc(s) ont était modifiés pour ajouter la key '{user_key}' absente.")
        # Écrire à nouveau le fichier avec la nouvelle clé
        return save_json_file(self.json_file_name,self.json_file)