import unittest
import os
from rubrica import AddressBook


class TestRubrica(unittest.TestCase):
    FILE_TEST_RUBRICA = 'test_rubrica.txt'

    def setUp(self):
        # Crea un'istanza della rubrica e pulisce il file prima di ogni test
        self.rubrica = AddressBook(self.FILE_TEST_RUBRICA)
        # Pulisce il file rubrica prima di ogni test
        with open(self.FILE_TEST_RUBRICA, 'w') as f:
            pass

    def tearDown(self):
        # Elimina il file della rubrica dopo ogni test
        if os.path.exists(self.FILE_TEST_RUBRICA):
            os.remove(self.FILE_TEST_RUBRICA)

    def test_numero_telefono_valido(self):
        # Test per la validità dei numeri di telefono
        self.assertTrue(self.rubrica.valid_phone_number("1234567890"))
        self.assertFalse(self.rubrica.valid_phone_number("12345678904854"))
        self.assertFalse(self.rubrica.valid_phone_number("1234567890www"))
        self.assertFalse(self.rubrica.valid_phone_number("1234567890+"))

    def test_solo_lettere(self):
        # Test per la validità dei nomi contenenti solo lettere
        self.assertTrue(self.rubrica.only_letters("Mario"))
        self.assertTrue(self.rubrica.only_letters("MarioRossi"))
        self.assertFalse(self.rubrica.only_letters("Mario7Rossi"))
        self.assertFalse(self.rubrica.only_letters("MarioRossi!"))

    def test_aggiungi_contatto(self):
        # Test per aggiungere un contatto alla rubrica
        self.rubrica.add_contact("Mario", "Bianchi", "1234567890")

        with open(self.FILE_TEST_RUBRICA, 'r') as f:
            contatti = f.readlines()
            found = False
            if "Mario Bianchi 1234567890" in contatti[0]:
                found = True
            self.assertTrue(found, """Il contatto Mario Bianchi 
                            non è stato trovato nella rubrica.""")

    def test_elimina_contatto(self):
        # Test per eliminare un contatto dalla rubrica
        self.rubrica.add_contact("Mario", "Bianchi", "1234567890")

        self.rubrica.delete_contact("Mario", "Bianchi")

        with open(self.FILE_TEST_RUBRICA, 'r') as f:
            contatti = f.readlines()

            found = False
            if "Mario Bianchi" in contatti:
                found = True
            self.assertFalse(found,
                             """Il contatto Mario Bianchi è ancora presente 
                             nella rubrica dopo l'eliminazione.""")

    def test_visualizza_contatti(self):
        # Test per visualizzare i contatti nella rubrica

        self.rubrica.add_contact("Mario", "Rossi", "1234567890")
        self.rubrica.add_contact("Luigi", "Verdi", "0987654321")
        self.rubrica.add_contact("Giulia", "Bianchi", "1122334455")

        contacts = self.rubrica.read_contacts()

        found_mario = False
        found_luigi = False
        found_giulia = False

        for contact in contacts:
            if "Mario Rossi 1234567890" in contact:
                found_mario = True
            if "Luigi Verdi 0987654321" in contact:
                found_luigi = True
            if "Giulia Bianchi 1122334455" in contact:
                found_giulia = True

        self.assertTrue(
            found_mario, "Il contatto Mario Rossi non è stato trovato ")
        self.assertTrue(
            found_luigi, "Il contatto Luigi Verdi non è stato trovato ")
        self.assertTrue(
            found_giulia, "Il contatto Giulia Bianchi non è stato trovato ")

    def test_search_contact(self):
        # Test per verificare la ricerca di contatti nella rubrica

        # Aggiungi i contatti
        self.rubrica.add_contact("Mario", "Rossi", "1234567890")
        self.rubrica.add_contact("Luigi", "Verdi", "0987654321")
        self.rubrica.add_contact("Giulia", "Bianchi", "1122334455")

        search_term = "Mario"
        results = self.rubrica.search_contact(search_term)
        found = False
        if "Mario Rossi 1234567890" in results[0]:
            found = True
        self.assertTrue(found,
                        "Il contatto Mario Rossi non è stato trovato.")

        search_term = "Bianchi"
        results = self.rubrica.search_contact(search_term)
        found = False
        if "Giulia Bianchi 1122334455" in results[0]:
            found = True
        self.assertTrue(found,
                        "Il contatto Giulia Bianchi non è stato trovato.")

        search_term = "Ferrari"
        results = self.rubrica.search_contact(search_term)
        found = False
        if ((f"Nessun contatto trovato con il parametro di ricerca: {search_term}" in results[0])):
            found = True
        self.assertFalse(
            found,
            f"""Un contatto è stato trovato per il termine
            di ricerca '{search_term}'""")


if __name__ == '__main__':
    unittest.main()
