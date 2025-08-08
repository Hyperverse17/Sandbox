
import time
import sqlite3

try:
    from functions import bandQuery, AlbumQuery
    
    print()
    bandName = input("Band: ")
    print()
    AlbumQuery(bandName)
    print()
        
except(sqlite3.OperationalError) as e:
    print(f"Error: -{e}-")
    print()

finally:
    print("Fin del programa")
    print()
    time.sleep(2)

