import argparse
import os

# Nome del file di testo per salvare i contatti
FILE_RUBRICA = 'rubrica.txt'

# Funzione per verificare se una stringa è composta solo da lettere


def solo_lettere(s):
    return all(char.isalpha() for char in s)

# Funzione per verificare se un numero di telefono è valido


def numero_telefono_valido(telefono):
    return telefono.isdigit() and len(telefono) <= 10

# Funzione per visualizzare tutti i contatti


def visualizza_contatti():
    if not os.path.exists(FILE_RUBRICA):
        print("Non ci sono contatti salvati.")
        return
    with open(FILE_RUBRICA, 'r') as f:  # usiamo la modalità di apertura r (read)
        contatti = f.readlines()
    if contatti:
        for contatto in contatti:
            print(contatto.strip())
    else:
        print("Non ci sono contatti nella rubrica.")

# Funzione per aggiungere o modificare un contatto


def aggiungi_contatto(nome, cognome, telefono):

    nome = nome.capitalize()
    cognome = cognome.capitalize()

    if not solo_lettere(nome):
        print("Il nome deve contenere solo lettere.")
        return
    if not solo_lettere(cognome):
        print("Il cognome deve contenere solo lettere.")
        return
    if not numero_telefono_valido(telefono):
        print("Il numero di telefono deve contenere solo numeri e avere un massimo di 10 cifre.")
        return

    contatto_trovato = False
    contatti_modificati = []

    # Controllo se il contatto esiste già
    if os.path.exists(FILE_RUBRICA):
        with open(FILE_RUBRICA, 'r') as f:  # usiamo la modalità di apertura r (read)
            contatti = f.readlines()

        for contatto in contatti:
            contatto_nome, contatto_cognome, *numero = contatto.strip().split()
            if contatto_nome.lower() == nome.lower() and contatto_cognome.lower() == cognome.lower():
                contatto_trovato = True
                print("Il contatto " + nome + " " + cognome +
                      " esiste già. Vuoi modificare il numero di telefono? (y/n)")
                risposta = input().strip().lower()
                if risposta == 'y':
                    # Aggiungi il nuovo numero
                    contatti_modificati.append(
                        nome + " " + cognome + " " + telefono + "\n")
                    print("Contatto " + nome + " " + cognome + " modificato.")
                else:
                    # Mantieni il contatto originale
                    contatti_modificati.append(contatto)
                    print("Nessuna modifica al contatto.")
                continue
            contatti_modificati.append(contatto)  # Mantieni gli altri contatti

    if not contatto_trovato:
        # Aggiungi nuovo contatto
        contatti_modificati.append(
            nome + " " + cognome + " " + telefono + "\n")
        print("Contatto " + nome + " " + cognome + " aggiunto.")

    with open(FILE_RUBRICA, 'w') as f:  # usiamo la modalità di apertura w (write)
        f.writelines(contatti_modificati)

# Funzione per eliminare un contatto specifico


def elimina_contatto(nome, cognome):
    if not os.path.exists(FILE_RUBRICA):
        print("Non ci sono contatti salvati.")
        return
    with open(FILE_RUBRICA, 'r') as f:  # usiamo la modalità di apertura r (read)
        contatti = f.readlines()

    # Converti il nome e cognome in minuscolo per il confronto
    nome_lower = nome.lower()
    cognome_lower = cognome.lower()

    contatti_modificati = []
    contatto_trovato = False

    for contatto in contatti:
        # Estrai il nome e cognome dal contatto e converti in minuscolo
        contatto_nome, contatto_cognome, *_ = contatto.strip().split()

        # Controlla se è il contatto da eliminare
        if contatto_nome.lower() == nome_lower and contatto_cognome.lower() == cognome_lower:
            contatto_trovato = True
            continue  # Salta il contatto da eliminare
        else:
            contatti_modificati.append(contatto)  # Mantieni gli altri contatti

    if not contatto_trovato:
        print("Contatto " + nome + " " + cognome + " non trovato.")
    else:
        with open(FILE_RUBRICA, 'w') as f:  # usiamo la modalità di apertura w (write)
            f.writelines(contatti_modificati)
        print("Contatto " + nome + " " + cognome + " eliminato.")

# Funzione principale per gestire i comandi


def main():
    parser = argparse.ArgumentParser(description="Gestione della rubrica")

    subparsers = parser.add_subparsers(
        dest='comando', help='Comando da eseguire')

    # Comando per visualizzare i contatti
    subparsers.add_parser('visualizza', help='Visualizza tutti i contatti')

    # Comando per aggiungere un contatto
    parser_aggiungi = subparsers.add_parser(
        'aggiungi', help='Aggiungi un nuovo contatto')

    # Argomenti Obbligatori
    parser_aggiungi.add_argument('nome', type=str, help='Nome del contatto')
    parser_aggiungi.add_argument(
        'cognome', type=str, help='Cognome del contatto')
    parser_aggiungi.add_argument(
        'telefono', type=str, help='Numero di telefono')

    # Comando per eliminare un contatto
    parser_elimina = subparsers.add_parser(
        'elimina', help='Elimina un contatto')
    parser_elimina.add_argument('nome', type=str, help='Nome del contatto')
    parser_elimina.add_argument(
        'cognome', type=str, help='Cognome del contatto')

    args = parser.parse_args()

    # Esegui il comando appropriato
    if args.comando == 'aggiungi':
        aggiungi_contatto(args.nome, args.cognome, args.telefono)
    elif args.comando == 'visualizza':
        visualizza_contatti()
    elif args.comando == 'elimina':
        elimina_contatto(args.nome, args.cognome)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
