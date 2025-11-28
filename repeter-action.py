mot_cle = "stop"
message = ""

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")
    
    # controle de chaine vide 
    if message == "":
        pass
    # Sortie de boucle
    elif message.lower() == mot_cle:
        break  
    else:
        print(f"Vous avez saisi : {message}")

print("Boucle terminée, mot-clé détecté.")