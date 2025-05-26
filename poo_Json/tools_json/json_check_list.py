# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

#FICHIER ABANDONNER !

import json
from tools.display_info import display_info_print


def check_list_in_json(self):
        if len(self.json_file) > 0:
            return self.key_in_json()
        else:
            display_info_print(f"[ ATTENTION ] Aucune liste d'objet existante dans le fichier {self.json_file_name}.",
                                "[ REDIRECTION ]",
                                "Vers le menu, merci de selectioner le programme :",
                                "-> Créer un nouvelle objet avec des clés et des valeurs à un fichier vide.")
            return None