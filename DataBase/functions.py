
import sqlite3
from properties import *

# Conexión a la base de datos existente
conn   = sqlite3.connect(dataBaseName)
cursor = conn.cursor()

# --- Insertar banda ---
def insertBand(name, country, genre, formedIn, active):
    conn   = sqlite3.connect(dataBaseName)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bands (name, country, genre, formedIn, active)
        VALUES (?, ?, ?, ?, ?)
    """, (name, country, genre, formedIn, active))
    conn.commit()
    conn.close()
    return cursor.lastrowid  # Devuelve el ID de la banda insertada

# --- Insertar álbum ---
def insertAlbum(title, year, bandId):
    conn   = sqlite3.connect(dataBaseName)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO albums (title, year, bandId)
        VALUES (?, ?, ?)
    """, (title, year, bandId))
    conn.commit()
    conn.close()

# --- Insertar subgénero (si no existe) ---
def insertSubgenre(name):
    cursor.execute("""
        INSERT OR IGNORE INTO subgenres (name) VALUES (?)
    """, (name,))
    cursor.execute("""
        SELECT id FROM subgeneros WHERE nombre = ?
    """, (name,))
    return cursor.fetchone()[0]

def bandQuery():
    conn   = sqlite3.connect(dataBaseName)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bands")
    bands = cursor.fetchall()

    for band in bands:
        print(band)

    conn.close()

def AlbumQuery(bandName):

    conn   = sqlite3.connect(dataBaseName)
    cursor = conn.cursor()

    if bandName == "":
        cursor.execute('''SELECT * 
                       FROM albums
                       ORDER BY title''')
        
    else:
        cursor.execute("""
        SELECT albums.title, albums.year 
        FROM albums
        JOIN bands ON albums.bandId = bands.id
        WHERE bands.name = ?
        ORDER BY year
    """, (bandName,))

    albums = cursor.fetchall()

    for album in albums:
        print(album)


    conn.close()