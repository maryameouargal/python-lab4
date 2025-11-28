def saisir_notes(max_notes=5):
    notes = []
    compteur = 0
    
    while compteur < max_notes:
        entree = input(f"Note {compteur+1}/{max_notes} ou 'stop' : ").strip()
        
        if entree.lower() == "stop":
            break
            
        if entree == "":
            print("Entrée vide, ignorée.")
            continue
            
        try:
            note = float(entree)
            if note < 0 or note > 20:
                print("Erreur: La note doit être entre 0 et 20.")
                continue
                
            notes.append(note)
            compteur += 1
        except ValueError:
            print("Nombre invalide.")
            continue
    
    return notes

def afficher_resultats(notes, seuil=10):
    print("\n=== RÉSULTATS ===")
    for index, note in enumerate(notes, start=1):
        if note >= seuil:
            statut = "Admis"
        else:
            statut = "Refusé"
        print(f"Étudiant {index} : note {note} → {statut}")

def calculer_moyenne_mention(notes):
    if not notes:
        return None, "Aucune note"
    
    moyenne = sum(notes) / len(notes)
    
    if moyenne >= 16:
        mention = "Très Bien"
    elif moyenne >= 14:
        mention = "Bien" 
    elif moyenne >= 12:
        mention = "Assez Bien"
    elif moyenne >= 10:
        mention = "validé"
    else:
        mention = "Non validé"
    
    return moyenne, mention

seuil = 10
max_notes = 5

notes = saisir_notes(max_notes)
afficher_resultats(notes, seuil)

if notes:
    moyenne, mention = calculer_moyenne_mention(notes)
    print(f"\nMoyenne : {moyenne:.2f} → {mention}")
