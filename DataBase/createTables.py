
import sqlite3
from properties import *

try: 
#   Conexión a la base de datos (se crea si no existe)
    conn   = sqlite3.connect(dataBaseName)
    cursor = conn.cursor()

#   Crear tabla de bandas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT,
            genre TEXT,
            formedIn INTEGER,
            active BOOLEAN
        )
    ''')

#   Crear tabla de álbumes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            bandId INTEGER,
            FOREIGN KEY (bandId) REFERENCES bands(id)
        )
    ''')

#   Crear tabla de subgéneros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subgenres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    ''')

#   Crear tabla intermedia banda-subgénero
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bandSubgenre (
            bandId INTEGER,
            subgenreId INTEGER,
            FOREIGN KEY (bandId) REFERENCES bands(id),
            FOREIGN KEY (subgenreId) REFERENCES subgenres(id),
            PRIMARY KEY (bandId, subgenreId)
        )
    ''')

#   Guardar y cerrar
    conn.commit()
    conn.close()

    print("Tablas creadas correctamente.")

finally:
    print()

