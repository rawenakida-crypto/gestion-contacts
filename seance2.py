import csv
import json
import os

FICHIER_CSV = "contacts.csv"
FICHIER_JSON = "contacts.json"

contacts = []


# Charger les contacts depuis un fichier
def charger_contacts():
    global contacts

    print("\nChoisir le format de stockage :")
    print("1. CSV")
    print("2. JSON")

    try:
        choix = int(input("Votre choix : "))

        if choix == 1:
            if os.path.exists(FICHIER_CSV):
                with open(FICHIER_CSV, "r", encoding="utf-8", newline="") as fichier:
                    lecteur = csv.DictReader(fichier)
                    contacts = list(lecteur)
                print("Contacts charges depuis CSV.")

            else:
                contacts = []
                print("Fichier CSV absent. Nouvelle liste creee.")

        elif choix == 2:
            if os.path.exists(FICHIER_JSON):
                with open(FICHIER_JSON, "r", encoding="utf-8") as fichier:
                    contacts = json.load(fichier)

                if not isinstance(contacts, list):
                    contacts = []
                    print("Format JSON invalide.")

                print("Contacts charges depuis JSON.")

            else:
                contacts = []
                print("Fichier JSON absent. Nouvelle liste creee.")

        else:
            print("Choix invalide.")

    except ValueError:
        print("Erreur : entrez un nombre.")

    except (OSError, json.JSONDecodeError, csv.Error) as erreur:
        contacts = []
        print("Erreur de lecture :", erreur)


# Afficher les contacts
def afficher_contacts():
    if not contacts:
        print("\nAucun contact disponible.")
        return

    print("\n===== LISTE DES CONTACTS =====")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Nom :", contact["nom"])
        print("Telephone :", contact["telephone"])
        print("Email :", contact["email"])


# Ajouter un contact
def ajouter_contact():
    nom = input("Nom : ").strip()
    telephone = input("Telephone : ").strip()
    email = input("Email : ").strip()

    if not nom or not telephone or not email:
        print("Erreur : tous les champs sont obligatoires.")
        return

    contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email
    }

    contacts.append(contact)

    print("Contact ajoute avec succes.")


# Rechercher un contact
def rechercher_contact():
    nom_recherche = input("Nom a rechercher : ").strip().casefold()

    resultats = [
        contact for contact in contacts
        if nom_recherche in contact["nom"].casefold()
    ]

    if resultats:
        print("\n===== RESULTATS =====")

        for contact in resultats:
            print("Nom :", contact["nom"])
            print("Telephone :", contact["telephone"])
            print("Email :", contact["email"])
            print("---------------------")
    else:
        print("Contact introuvable.")


# Modifier un contact
def modifier_contact():
    nom_recherche = input("Nom du contact a modifier : ").strip().casefold()

    for contact in contacts:
        if contact["nom"].casefold() == nom_recherche:
            print("Laissez un champ vide pour le conserver.")

            nouveau_nom = input("Nouveau nom : ").strip()
            nouveau_telephone = input("Nouveau telephone : ").strip()
            nouvel_email = input("Nouvel email : ").strip()

            if nouveau_nom:
                contact["nom"] = nouveau_nom

            if nouveau_telephone:
                contact["telephone"] = nouveau_telephone

            if nouvel_email:
                contact["email"] = nouvel_email

            print("Contact modifie avec succes.")
            return

    print("Contact introuvable.")


# Supprimer un contact
def supprimer_contact():
    nom_recherche = input("Nom du contact a supprimer : ").strip().casefold()

    for contact in contacts:
        if contact["nom"].casefold() == nom_recherche:
            contacts.remove(contact)
            print("Contact supprime avec succes.")
            return

    print("Contact introuvable.")


# Sauvegarder les contacts en CSV
def sauvegarder_csv():
    try:
        with open(FICHIER_CSV, "w", encoding="utf-8", newline="") as fichier:
            champs = ["nom", "telephone", "email"]
            redacteur = csv.DictWriter(fichier, fieldnames=champs)

            redacteur.writeheader()
            redacteur.writerows(contacts)

        print("Sauvegarde CSV reussie.")

    except (OSError, csv.Error) as erreur:
        print("Erreur de sauvegarde CSV :", erreur)


# Sauvegarder les contacts en JSON
def sauvegarder_json():
    try:
        with open(FICHIER_JSON, "w", encoding="utf-8") as fichier:
            json.dump(contacts, fichier, ensure_ascii=False, indent=4)

        print("Sauvegarde JSON reussie.")

    except (OSError, TypeError) as erreur:
        print("Erreur de sauvegarde JSON :", erreur)


# Menu principal
def menu():
    while True:
        print("\n========== GESTION DES CONTACTS ==========")
        print("1. Charger les contacts")
        print("2. Afficher les contacts")
        print("3. Ajouter un contact")
        print("4. Rechercher un contact")
        print("5. Sauvegarder en CSV")
        print("6. Sauvegarder en JSON")
        print("7. Modifier un contact")
        print("8. Supprimer un contact")
        print("9. Quitter")
        print("==========================================")

        try:
            choix = int(input("Votre choix : "))

            if choix == 1:
                charger_contacts()

            elif choix == 2:
                afficher_contacts()

            elif choix == 3:
                ajouter_contact()

            elif choix == 4:
                rechercher_contact()

            elif choix == 5:
                sauvegarder_csv()

            elif choix == 6:
                sauvegarder_json()

            elif choix == 7:
                modifier_contact()

            elif choix == 8:
                supprimer_contact()

            elif choix == 9:
                print("Voulez-vous sauvegarder avant de quitter ?")
                print("1. CSV")
                print("2. JSON")
                print("3. Ne pas sauvegarder")

                try:
                    format_sauvegarde = int(input("Votre choix : "))

                    if format_sauvegarde == 1:
                        sauvegarder_csv()
                    elif format_sauvegarde == 2:
                        sauvegarder_json()
                    elif format_sauvegarde != 3:
                        print("Choix invalide.")

                except ValueError:
                    print("Choix invalide. Sauvegarde non effectuee.")

                print("Au revoir !")
                break

            else:
                print("Choix invalide. Choisissez de 1 a 9.")

        except ValueError:
            print("Erreur : entrez un nombre valide.")


if __name__ == "__main__":
    menu()
