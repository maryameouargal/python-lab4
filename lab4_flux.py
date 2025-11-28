# Configuration du système de notation
print("Systèmes de notation disponibles:")
print("1 - Sur 10 ")
print("2 - Sur 20 ")
print("3 - Sur 100 ")

try:
    choix_systeme = int(input("Choisissez le système de notation (1-3): \n"))
except ValueError:
    print("Choix invalide - veuillez entrer un nombre.")
    exit(1)


if choix_systeme == 1:      # Sur 10
    note_max = 10
    seuil = 5
elif choix_systeme == 2:    # Sur 20
    note_max = 20
    seuil = 10
elif choix_systeme == 3:    # Sur 100
    note_max = 100
    seuil = 50
else:
    print("Choix invalide - veuillez choisir entre 1, 2 ou 3.")
    exit(1)

print(f"Système choisi: notation sur {note_max}")
print(f"Seuil d'admission: {seuil}/{note_max}")

# la note
try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide. Veuillez entrer un nombre.")
    exit(1)
    
#Verification du note
if note < 0 or note > note_max:
    print(f"Erreur: La note doit être comprise entre 0 et {note_max}.")
    exit(1)

# Détermination du résultat
if note >= note_max * 0.8:  
    print(f"Admis avec mention Très Bien ({note:.1f}/{note_max})")
elif note >= note_max * 0.7: 
    print(f"Admis avec mention Bien ({note:.1f}/{note_max})")
elif note >= note_max * 0.6: 
    print(f"Admis avec mention Assez Bien ({note:.1f}/{note_max})")
elif note >= seuil:
    print(f"Admis ({note:.1f}/{note_max})")
elif note >= seuil * 0.7:  
    print(f"Rattrapage nécessaire ({note:.1f}/{note_max})")
else:
    print(f"Refusé ({note:.1f}/{note_max})")