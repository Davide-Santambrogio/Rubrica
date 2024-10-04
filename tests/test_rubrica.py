import unittest
import os
from rubrica import solo_lettere, numero_telefono_valido, aggiungi_contatto, visualizza_contatti, elimina_contatto


class TestRubrica(unittest.TestCase):
    FILE_RUBRICA = 'test_rubrica.txt'

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

