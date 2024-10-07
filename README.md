# Rubrica

Questo progetto è un'applicazione per la gestione di una rubrica di contatti. Permette di aggiungere, visualizzare ed eliminare contatti, salvando le informazioni in un file di testo.

## Funzionalità

- **Aggiungi**: Permette di aggiungere un nuovo contatto con nome, cognome e numero di telefono.
- **Visualizza**: Mostra tutti i contatti salvati nella rubrica.
- **Elimina**: Rimuove un contatto esistente dalla rubrica.

## Requisiti

- Python 3.x
- Modulo `argparse` (incluso nella libreria standard di Python)

## Installazione

1. Clona questo repository:
   ```
   git clone https://github.com/tuo-username/gestione-rubrica.git
   cd gestione-rubrica
   ```

2. Assicurati di avere Python 3 installato sul tuo sistema. Puoi verificarlo eseguendo:
   ```
   python --version
   ```

## Utilizzo

Puoi utilizzare l'applicazione dalla riga di comando. Ecco i comandi disponibili:

### Aggiungere un contatto

```
python rubrica.py aggiungi <nome> <cognome> <telefono>
```

### Visualizzare i contatti

```
python rubrica.py visualizza
```

### Eliminare un contatto

```
python rubrica.py elimina <nome> <cognome>
```

## File di Rubrica

I contatti vengono salvati in un file di testo chiamato `rubrica.txt`. Se il file non esiste, verrà creato automaticamente alla prima esecuzione del programma.


