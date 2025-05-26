def display_info_print(text_1="", text_2 = "", text_3 = "",text_4 = "",text_5 = ""):
        NUMBER = 100
        code_color = 0
        
        if any(keyword in text_1 for keyword in ["ERREUR", "ATTENTION","SUPPRESSION"]):
                code_color = 91 # rouge
        elif any(keyword in text_1 for keyword in ["SUCCES","MISE A JOUR"]):
                code_color = 92 # vert
        elif any(keyword in text_1 for keyword in ["ANNULATION","INFO"]):
                code_color = 93 # jaune

        ligne ="\n"+ f"\033[{code_color}m•" * NUMBER +"\n\033[0m"
        
        espace = int((NUMBER - len(text_1))/2)
        text_1 =f"\033[{code_color}m\n\n"  + " " * espace + text_1 +  " " * espace +"\n\n\033[0m"

        if not text_2 == "":
                espace = int((NUMBER - len(text_2))/2)
                text_2 =f"\n\033[{code_color}m"  + " " * espace + text_2 +  " " * espace +"\n\n"

                if not text_3 == "":
                        espace = int((NUMBER - len(text_3))/2)
                        text_3 =f"\n\033[{code_color}m"  + " " * espace + text_3 +  " " * espace +"\n\n"

                        if not text_4 == "":
                                espace = int((NUMBER - len(text_4))/2)
                                text_4 =f"\n\033[{code_color}m"  + " " * espace + text_4 +  " " * espace +"\n\n"

                                if not text_5 == "":
                                        espace = int((NUMBER - len(text_5))/2)
                                        text_5 =f"\n\033[{code_color}m"  + " " * espace + text_5 +  " " * espace +"\n\n"
                                        return print(ligne + text_1 + text_2 + text_3 + text_4 + text_5 + ligne)

                                return print(ligne + text_1 + text_2 + text_3 + text_4 + ligne)

                        return print(ligne + text_1 + text_2 + text_3 + ligne)

                return print(ligne + text_1 + text_2 + ligne)

        return print(ligne + text_1 + ligne)