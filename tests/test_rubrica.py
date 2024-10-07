import unittest
import os
from rubrica import solo_lettere, numero_telefono_valido, aggiungi_contatto, visualizza_contatti, elimina_contatto


class TestRubrica(unittest.TestCase):
    FILE_RUBRICA = 'rubrica.txt'

    def test_numero_telefono_valido(self):

        argomento = numero_telefono_valido("1234567890")
        self.assertTrue(argomento)

        argomento = numero_telefono_valido("12345678904854")
        self.assertFalse(argomento)

        argomento = numero_telefono_valido("1234567890www")
        self.assertFalse(argomento)

        argomento = numero_telefono_valido("1234567890+")
        self.assertFalse(argomento)

    def test_solo_lettere(self):

        argomento = solo_lettere("Mario")
        self.assertTrue(argomento)

        argomento = solo_lettere("Mario" + "Rossi")
        self.assertTrue(argomento)

        argomento = solo_lettere("Mario7" + "Rossi")
        self.assertFalse(argomento)

        argomento = solo_lettere("Mario" + "Rossi!")
        self.assertFalse(argomento)

    def test_aggiungi_contatto(self):

        aggiungi_contatto("Mario", "Bianchi", "1234567890")

        with open(self.FILE_RUBRICA, 'r') as f:
            contatti = f.readlines()
            trovato = any(
                "Mario Bianchi 1234567890" in contatto for contatto in contatti)
            self.assertTrue(
                trovato, "Il contatto Mario Bianchi non è stato trovato nella rubrica.")

    def test_elimina_contatto(self):

        # Ora elimina il contatto
        elimina_contatto("Mario", "Bianchi")

        # Verifica se il contatto è stato eliminato correttamente
        with open(self.FILE_RUBRICA, 'r') as f:
            contatti = f.readlines()
            trovato = any("Mario Bianchi" in contatto for contatto in contatti)
            self.assertFalse(
                trovato, "Il contatto Mario Bianchi è ancora presente nella rubrica dopo l'eliminazione.")
