
import time
import sqlite3

try:
    from functions import insertBand, insertAlbum

    bandId = insertBand("Allegaeon", "United States", "Technical Melodic Death Metal", 2008, True)
    insertAlbum("Apoptosis", 2019, bandId)
    insertAlbum("Formshifter", 2012, bandId)

    bandId = insertBand("Cytotoxin", "Germany", "Technical Death Metal", 2010, True)
    insertAlbum("Radiophobia", 2012, bandId)
    insertAlbum("Gammageddon", 2017, bandId)
    insertAlbum("Nuklearth", 2020, bandId)
    insertAlbum("Biographyte", 2025, bandId)

    bandId = insertBand("Vomitory", "Sweden", "Death Metal", 1989, True)
    insertAlbum("Terrorize, Brutalize, Sodomize", 2007, bandId)
    insertAlbum("Carnage Euphoria", 2009, bandId)
    insertAlbum("Opus Mortis VIII", 2011, bandId)
    insertAlbum("All Heads Are Gonna Roll", 2023, bandId)

    bandId = insertBand("Lik", "Sweden", "Death Metal", 2014, True)
    insertAlbum("Carnage", 2018, bandId)
    insertAlbum("Misanthropic Breed", 2020, bandId)
    insertAlbum("Necro", 2025, bandId)

    bandId = insertBand("Cut Up", "Sweden", "Death Metal", 2014, False)
    insertAlbum("Forensic Nightmares", 2015, bandId)
    insertAlbum("Wherever They May Rot", 2017, bandId)

    bandId = insertBand("Necrophagist", "Germany", "Technical Death Metal", 1992, False)
    insertAlbum("Onset Of Putrefaction", 1999, bandId)
    insertAlbum("Epitaph", 2004, bandId)

    bandId = insertBand("Benighted", "France", "Technical Death Metal", 1998, True)
    insertAlbum("Necrobreed", 2017, bandId)
    insertAlbum("Ekbom", 2024, bandId)

    bandId = insertBand("Gorod","France","Technical Death Metal", 2005, True)
    insertAlbum("Neurotripsicks", 2005, bandId)
    insertAlbum("Leading Vision", 2006, bandId)
    insertAlbum("Process Of A New Decline", 2009, bandId)
    insertAlbum("A Perfect Absolution", 2012, bandId)
    insertAlbum("A Maze Of Recycled Creeds", 2015, bandId)
    insertAlbum("Aethra", 2018, bandId)
    insertAlbum("The Orb", 2023, bandId)

    bandId = insertBand("Havok", "United States", "Thrash Metal", 2004, True )
    insertAlbum("Burn", 2009, bandId)
    insertAlbum("Time Is Up", 2011, bandId)
    insertAlbum("Unnatural Selection", 2013, bandId)
    insertAlbum("Conformicide", 2017, bandId)
    insertAlbum("V", 2020, bandId)

    




    print("Bandas y álbumes insertados correctamente.")
    
except(sqlite3.OperationalError) as e:
    print(f"Error: -{e}-")
    print()

finally:
    print("Fin del programa")
    print()
    time.sleep(2)

