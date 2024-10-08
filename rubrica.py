import argparse
import os

# Nome della cartella per le rubriche
DIRECTORY_RUBRICHE = 'rubriche'


def show_file_available():
    """Mostra la lista dei file rubrica disponibili nella directory rubriche"""
    if not os.path.exists(DIRECTORY_RUBRICHE):
        print("Non esiste la directory rubriche. Creandola ora...")
        os.makedirs(DIRECTORY_RUBRICHE)

    # Ottiene la lista dei file di testo nella directory rubriche
    address_books = [f for f in os.listdir(
        DIRECTORY_RUBRICHE) if f.endswith('.txt')]

    if address_books:
        print("Rubriche disponibili:")
        for address_book in address_books:
            # Mostra i file senza estensione .txt
            print(f"- {address_book[:-4]}")
    else:
        print("Non ci sono rubriche disponibili al momento.")


class AddressBook:
    def __init__(self, file):
        self.file = file
        self.initialize_file()  # Inizializza il file della rubrica

    def initialize_file(self):
        # Crea il file della rubrica se non esiste già
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                pass  # Crea un file vuoto

    def only_letters(self, s):
        return all(char.isalpha() for char in s)

    def valid_phone_number(self, phone):
        return phone.isdigit() and len(phone) <= 10

    def read_contacts(self):
        # Legge i contatti dal file
        if not os.path.exists(self.file):
            return []
        with open(self.file, 'r') as f:
            return f.readlines()

    def write_contacts(self, contacts):
        # Scrive i contatti nel file
        with open(self.file, 'w') as f:
            f.writelines(contacts)

    def display_contacts(self):
        # Visualizza tutti i contatti nella rubrica
        contacts = self.read_contacts()
        if contacts:
            print("\nContatti presenti in questa Rubrica:\n")
            for contact in contacts:
                print(contact.strip())
        else:
            print("Non ci sono contatti nella rubrica.")

    def add_contact(self, first_name, last_name, phone):
        # Aggiungi un nuovo contatto alla rubrica.
        first_name = first_name.capitalize()  # Maiuscola per il nome
        last_name = last_name.capitalize()  # Maiuscola per il cognome

        # Controlla la validità del nome
        if not self.only_letters(first_name):
            print("Il nome deve contenere solo lettere.")
            return
        if not self.only_letters(last_name):
            print("Il cognome deve contenere solo lettere.")
            return
        if not self.valid_phone_number(phone):
            print("""Il numero di telefono deve contenere solo numeri
                  e avere un massimo di 10 cifre.""")
            return

        contacts = self.read_contacts()  # Legge i contatti esistenti
        contact_found = False
        modified_contacts = []

        # Controlla se il contatto esiste già
        for contact in contacts:
            contact_first_name, contact_last_name, *n = contact.strip().split()

            if (contact_first_name.lower() == first_name.lower() and
                    contact_last_name.lower() == last_name.lower()):
                contact_found = True
                print(
                    f"""Il contatto {first_name} {last_name} esiste già.
                      Vuoi modificare il numero di telefono? (y/n)"""
                )

                answer = input().strip().lower()
                if answer == 'y':
                    # Modifica il contatto
                    modified_contacts.append(
                        f"{first_name} {last_name} {phone}\n")
                    print(f"Contatto {first_name} {last_name} modificato.")
                else:
                    # Mantiene il contatto esistente
                    modified_contacts.append(contact)
                    print("Nessuna modifica al contatto.")
                continue
            modified_contacts.append(contact)

        # Se il contatto non esiste, lo aggiunge alla lista
        if not contact_found:
            modified_contacts.append(f"{first_name} {last_name} {phone}\n")
            print(f"Contatto {first_name} {last_name} aggiunto.")

        # Scrive i contatti modificati nel file
        self.write_contacts(modified_contacts)

    def delete_contact(self, first_name, last_name):
        # Elimina un contatto dalla rubrica.
        contacts = self.read_contacts()
        first_name_lower = first_name.lower()
        last_name_lower = last_name.lower()
        modified_contacts = []
        contact_found = False

        for contact in contacts:
            contact_first_name, contact_last_name, *n = contact.strip().split()

            # Se il contatto corrisponde a quello da eliminare
            if (contact_first_name.lower() == first_name_lower
                    and contact_last_name.lower() == last_name_lower):
                contact_found = True
                continue
            else:
                modified_contacts.append(contact)

        if not contact_found:
            print(f"Contatto {first_name} {last_name} non trovato.")
        else:
            self.write_contacts(modified_contacts)
            print(f"Contatto {first_name} {last_name} eliminato.")

    def search_contact(self, term):
        # Cerca un contatto in base a nome o cognome.
        contacts = self.read_contacts()
        results = []

        for contact in contacts:
            contact_first_name, contact_last_name, *n = contact.strip().split()
            if (term.lower() in contact_first_name.lower() or
                    term.lower() in contact_last_name.lower()):
                results.append(contact.strip())

        if results:
            return results
        else:
            return [f"Nessun contatto trovato con il parametro di ricerca: {term}"]


def main():
    # Mostra le rubriche disponibili
    show_file_available()

    # Crea un parser per gestire gli argomenti della riga di comando
    parser = argparse.ArgumentParser(description="Gestione della rubrica")

    # Aggiungi un argomento per il nome della rubrica (es: amici, lavoro, famiglia)
    parser.add_argument('rubrica', type=str,
                        help="Nome della rubrica (senza estensione)")

    # Sottocomandi per le operazioni (visualizza, aggiungi, elimina, cerca)
    subparsers = parser.add_subparsers(
        dest='command', help='Comando da eseguire')

    # Sottocomando per visualizzare i contatti
    subparsers.add_parser('visualizza', help='Visualizza tutti i contatti')

    # Sottocomando per aggiungere un nuovo contatto
    parser_add = subparsers.add_parser(
        'aggiungi', help='Aggiungi un nuovo contatto')
    parser_add.add_argument('first_name', type=str, help='Nome del contatto')
    parser_add.add_argument('last_name', type=str, help='Cognome del contatto')
    parser_add.add_argument('phone', type=str, help='Numero di telefono')

    # Sottocomando per eliminare un contatto
    parser_delete = subparsers.add_parser(
        'elimina', help='Elimina un contatto')
    parser_delete.add_argument(
        'first_name', type=str, help='Nome del contatto')
    parser_delete.add_argument(
        'last_name', type=str, help='Cognome del contatto')

    # Sottocomando per cercare un contatto
    parser_search = subparsers.add_parser('cerca', help='Cerca un contatto')
    parser_search.add_argument(
        'term', type=str, help='Nome o cognome da cercare')

    args = parser.parse_args()  # Analizza gli argomenti della riga di comando

    # Crea il file rubrica scelto
    rubrica_file = os.path.join(DIRECTORY_RUBRICHE, f"{args.rubrica}.txt")

    # Crea un'istanza della rubrica con il file scelto
    address_book = AddressBook(rubrica_file)

    # Esegue il comando specificato dall'utente
    if args.command == 'aggiungi':
        address_book.add_contact(args.first_name, args.last_name, args.phone)
    elif args.command == 'visualizza':
        address_book.display_contacts()
    elif args.command == 'elimina':
        address_book.delete_contact(args.first_name, args.last_name)
    elif args.command == 'cerca':
        results = address_book.search_contact(args.term)
        for result in results:
            print(result)
    else:
        parser.print_help()  # Mostra aiuto se il comando non è riconosciuto


if __name__ == '__main__':
    main()  # Avvia il programma
