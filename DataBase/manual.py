
import sqlite3
import time

try:
    from properties import *
    from functions import insertBand, insertAlbum

    conn = sqlite3.connect(dataBaseName) #42-55#
    cursor = conn.cursor()

    cursor.execute(""" DELETE 
                   FROM albums
                   WHERE id BETWEEN 42 and 55
                   """)
    conn.commit()
    conn.close()
    
finally:
    print("Fin del programa")
    print()
    time.sleep(2)

