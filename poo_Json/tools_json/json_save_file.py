# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools.display_info import display_info_print

def save_json_file(json_file_name,json_file):
    with open(f"./json/{json_file_name}", "w") as f:
        json.dump(json_file, f, indent=4, ensure_ascii=False)
    display_info_print("[ MISE A JOUR ]",f"Fichier '{json_file_name}.json' terminée.")