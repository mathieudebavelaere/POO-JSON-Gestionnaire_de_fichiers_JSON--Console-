# Manipulation de fichier JSON
# Créer par Debavelaere Mathieu.
# https://mathieudebavelaere.fr

import json
from tools_json.json_open_file import open_json_file
from tools.display_info import display_info_print

class Json_read: #CLASS PARENT
    
    def __init__(self):
        self.list_key = []
        self.user_choice = 0
        self.count_key = 0
        

    def choice_file(self): #Fonction pour récupérer le nom du fichier et la liste Json.
        json_list_key = open_json_file() #Fonction pour ouvrire mon fichier JSON.
        self.json_file = json_list_key[0] #Récupération de la liste Json.
        self.json_file_name = json_list_key[1] #Récupération du nom du fichier JSON.
        return self.read_key_in_json()

    
    def read_key_in_json(self): #Fonction pour lire les key existante dans le fichier JSON pour les importers dans une liste.

        if not self.json_file: #Vérification qu'il exite au moins une clé dans l'objet. Si 'self.count_key' reste à une valeur de '1' cela veut dire que notre fichier n'a pas boucler car aucune clé trouver.
            display_info_print(f"[ ERREUR ]",f" Votre fichier {self.json_file_name}.json ne contient aucun objet.")#Affichage d'erreur à l'utilisateur en lui indiquant le nom du fichier JSON.
            return self.choice_file() #Retourne sur la fonction présédente pour re-demender à l'utilisateur de choisir un fichier JSON exploitable.
        else:
            display_info_print(f"Voici la liste des clés disponible dans le fichier '{self.json_file_name}'")#Affichage du résultat de la liste des clés.
            return self.choice_key() #Envoi les résultats a là fonction suivante.

    
    def search_json(self, query,user_key): #Fonction de rechecher dans le fichier JSON.
        try:
            query = int(query) #On teste si on peut convertir la réponse en valeur numérique pour savoir quel recherche on peut retourner.
        except ValueError:
            try:
                result = [json_file for json_file in self.json_file if query.lower() in (json_file[user_key]).lower()]
            except: 
                display_info_print(f"[ ERREUR ]"," Les valeurs dans la clefs doit contenir une 'list'.","Le programme n'est pas encore configueré pour se cas de figure","Merci de réssayer plus tard.")
                return self.choice_key()
            else:
                return  result
                #Version si la réponse est un type 'str'.
            #[ ERREUR ] si la valeur est une 'list' la fonction .lower() ne fonctionnera pas.
            #Calculer 
        else:
            return [json_file for json_file in self.json_file if str(query) in str(json_file[user_key])] #Version si la réponse est un type 'int'.
            


    def choice_key(self): #Fonction pour choisir sur quelle key faire notre recherche.
        self.count_key = 1
        for file in self.json_file[0:1]: #Boucle sur le premier objet pour récupérer les information à l'interieur.
            for i,(key,value) in enumerate(file.items()): #Boucle avec la fonction 'items()' pour récupérer ici les clefs de l'objet.
                print(f"        {i+1} • {key}") #Affichage de la liste des clefs à l'utilisateur.
                key_any = any([True if key in self.list_key else False for d in self.list_key])#Vérifie si il est déjà présent dans la liste afin d'éviter les doublons.
                if not key_any:
                    self.list_key.append(key) #Ajout des clefs dans une liste a part.
                self.count_key +=1
            display_info_print("Taper le numéro de la clé que vous souhaitez pour éffectuer votre recherche."," (Taper sur le nombre '0' puis valider pour retourner au menu principal)")
        while True: #Boucle tant que l'utilisateur ne répond pas au bonne condition demander.
            try: 
                self.user_choice = int(input(f"     Choix : ")) #Demande a l'utilisateur avec quel clé il souhaite travailler.
            except: 
                display_info_print(f"[ ERREUR ]"," La réponse doit contenir uniquement le numéro.") #Message d'erreur si l'utilisateur ne répond pas un nombre.
            else:
                if int(self.user_choice) == 0: #Condition si l'utilisateur souhaite sortir de la fonction pour retourner au menu principal.
                        return 
                if 1 <= self.user_choice <= self.count_key-1: #Condition si l'utilisateur rentre bien un nombre correspondant au nombre de clé afficher.
                    return self.read_json() #Envoi les résultats a là fonction suivante.
                else:
                    display_info_print(f"[ ERREUR ]",f" La réponse donné doit être compris entre les choix 1 à {self.count_key-1}.")#Message d'erreur si l'utilisateur rentre un nombre supperieur ou inferieur au nombre de clé afficher.
                
    
    def read_json(self): #Fonction pour lire le fichier JSON

        user_key = self.list_key[self.user_choice-1] #Décrémente de '1' pour avoir le bonne index par la suite.
        
        display_info_print(f"Quel et votre recherche avec la key : {user_key} ?","(Taper sur 'exit' puis valider pour éffectuer nouvelle recherche sur une autre clé )")
        while True: #Boucle pour gérer les cas d'erreurs si le jeux n'existe pas dans le fichier se qui évite la relance du programme.
                query = str(input("     Choix : ")).strip().lower() #Demande à l'utilisateur quel jeux il recherche.

                if len(query) >= 1:
                    if query.lower() == "exit": #Condition pour l'utilisateur s'il souhaite quitter le programme.
                        return self.read_key_in_json()

                    query_exists = any([True if str(query.lower()) in str(json_file[f"{user_key}"]).lower() else False for json_file in self.json_file]) #Vérifie dans le fichier JSON si il et présent.

                    if not query_exists: #Condition si la variable 'query_exists' retourne 'False'
                        display_info_print(f"[ ERREUR ]",f" La recherche : '{query}' n'existe pas dans le fichier : {self.json_file_name}.") #Message d'erreur à l'utilisateur que sa recherche n'existe pas dans le fichier JSON.
                    else:
                        results = self.search_json(query,user_key) #Création d'une variable qui récupère les résultats de la fonction de recherche.
                        display_info_print(f"Voici le(s) résultat(s) de la recherche :")
                        for json_file_results in results: #Boucle les résultats trouver.
                            self.display_json(json_file_results)#Envoie en boucle sur une fonction qui affiche à l'utilisateur les résultats de sa recherche.
                else:
                    display_info_print("[ ERREUR ]"," Le mot recherchée ne doit pas contenir moins de une lettres.")#Message d'erreur si l'utilisateur rentre un champs vide.


    def display_json(self,json_file_results): #Fonction pour afficher les résultats des recherche.
        print("•" * 100) 
        for key in self.list_key: #Boucle la liste des clefs qu'on à créer au précédament.
            value = json_file_results.get(key, "Inconnu")
            if value == "": #Condition d'affichage si une clé existe mais na aucune valeur, on affiche à l'utilisateur une valeur 'Iconnue' au lieu de laisser un champs vide.
                value = "Inconnu"
            if key != "id":
                print(f"{key.capitalize()} : {value}") #Affichage des résultats d'objet avec leurs clefs et leurs valeurs.
        print("•" * 100 + "\n")