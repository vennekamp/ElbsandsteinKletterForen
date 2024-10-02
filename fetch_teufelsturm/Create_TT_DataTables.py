import sqlite3
import time
import os
from datetime import datetime
from ReadingWebPage import python_get_url_source
import tt_summit_object
# Assuming these are predefined in your Python application
# TT_DownLoaderPC.path2SQLiteDBFile = "path_to_your_database.db"
# TT_DownLoaderPC.ERSTER_GIPFEL = 1
# TT_DownLoaderPC.ANZAHL_GIPFEL = 1120

path_to_db = "path_to_your_database.db"
first_gipfel = 1
last_gipfel = 1120

#region SQLite statements

# Connect to SQLite database
conn = sqlite3.connect(path_to_db)
cursor = conn.cursor()

# Create android_metadata table
cursor.execute("DROP TABLE IF EXISTS android_metadata;")
cursor.execute("CREATE TABLE android_metadata (locale TEXT DEFAULT 'en_US');")
cursor.execute("REPLACE INTO android_metadata VALUES ('en_US');")

# Function similar to Create1bDataTable_ANDROID_APP in Java (not provided here)
# Create1bDataTable_ANDROID_APP(cursor)

# Create TT_Summit_AND table
cursor.execute("DROP TABLE IF EXISTS TT_Summit_AND;")
cursor.execute("""
    CREATE TABLE TT_Summit_AND (
        _id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        _idTimeStamp INTEGER NOT NULL, 
        intTTGipfelNr INTEGER NOT NULL, 
        strName TEXT, 
        dblGPS_Latitude REAL, 
        dblGPS_Longitude REAL, 
        strGebiet TEXT, 
        intKleFuGipfelNr INTEGER, 
        intAnzahlWege INTEGER, 
        intAnzahlSternchenWege INTEGER, 
        strLeichtesterWeg TEXT, 
        fltGPS_Altitude REAL, 
        osm_type TEXT, 
        osm_ID INTEGER, 
        osm_display_name TEXT
    );
""")
cursor.execute("""
    CREATE UNIQUE INDEX index_TT_Summit_AND_intTTGipfelNr 
    ON TT_Summit_AND(intTTGipfelNr);
""")

# Prepare statements for inserting into TT_Summit_AND
insert_gipfel_query = """
    INSERT INTO TT_Summit_AND (
        _idTimeStamp, intTTGipfelNr, strName, dblGPS_Latitude, dblGPS_Longitude, 
        strGebiet, intKleFuGipfelNr, intAnzahlWege, intAnzahlSternchenWege, 
        strLeichtesterWeg, fltGPS_Altitude, osm_type, osm_ID, osm_display_name
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# Create TT_NeigbourSummit_AND table
cursor.execute("DROP TABLE IF EXISTS TT_NeigbourSummit_AND;")
cursor.execute("""
    CREATE TABLE TT_NeigbourSummit_AND (
        _id INTEGER PRIMARY KEY NOT NULL, 
        _idTimStamp INTEGER NOT NULL, 
        intTTHauptGipfelNr INTEGER NOT NULL, 
        intTTNachbarGipfelNr INTEGER NOT NULL
    );
""")

insert_neighbour_query = """
    INSERT INTO TT_NeigbourSummit_AND (
        _idTimStamp, intTTHauptGipfelNr, intTTNachbarGipfelNr
    ) VALUES (?, ?, ?);
"""

# Create TT_Route4SummitAND table
cursor.execute("DROP TABLE IF EXISTS TT_Route4SummitAND;")
cursor.execute("""
    CREATE TABLE TT_Route4SummitAND (
        _id INTEGER PRIMARY KEY, 
        _idTimStamp INTEGER, 
        intTTHauptGipfelNr INTEGER, 
        intTTKletterWeg4Gipfel INTEGER
    );
""")

insert_route4summit_query = """
    INSERT INTO TT_Route4SummitAND (
        _idTimStamp, intTTHauptGipfelNr, intTTKletterWeg4Gipfel
    ) VALUES (?, ?, ?);
"""

# Create TT_Route_AND table
cursor.execute("DROP TABLE IF EXISTS TT_Route_AND;")
cursor.execute("""
    CREATE TABLE TT_Route_AND (
        _id INTEGER PRIMARY KEY NOT NULL, 
        _idTimeStamp INTEGER NOT NULL, 
        intTTWegNr INTEGER NOT NULL, 
        intTTGipfelNr INTEGER NOT NULL, 
        WegName TEXT, 
        blnAusrufeZeichen INTEGER, 
        intSterne INTEGER, 
        strSchwierigkeitsGrad TEXT, 
        sachsenSchwierigkeitsGrad INTEGER, 
        ohneUnterstuetzungSchwierigkeitsGrad INTEGER, 
        rotPunktSchwierigkeitsGrad INTEGER, 
        intSprungSchwierigkeitsGrad INTEGER, 
        intAnzahlDerKommentare INTEGER, 
        fltMittlereWegBewertung REAL, 
        Erstbegeher TEXT, 
        Erstbegehungsdatum TEXT, 
        Wegbeschreibung TEXT
    );
""")

insert_route_query = """
    INSERT INTO TT_Route_AND (
        _idTimeStamp, intTTWegNr, intTTGipfelNr, WegName, blnAusrufeZeichen, 
        intSterne, strSchwierigkeitsGrad, sachsenSchwierigkeitsGrad, 
        ohneUnterstuetzungSchwierigkeitsGrad, rotPunktSchwierigkeitsGrad, 
        intSprungSchwierigkeitsGrad, intAnzahlDerKommentare, 
        fltMittlereWegBewertung, Erstbegeher, Erstbegehungsdatum, 
        Wegbeschreibung
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# Create TT_Comment_AND table
cursor.execute("DROP TABLE IF EXISTS TT_Comment_AND;")
cursor.execute("""
    CREATE TABLE TT_Comment_AND (
        _id INTEGER PRIMARY KEY NOT NULL, 
        _idTimStamp INTEGER NOT NULL, 
        intTTWegNr INTEGER NOT NULL, 
        strEntryKommentar TEXT, 
        entryBewertung INTEGER, 
        strEntryUser TEXT, 
        entryDatum INTEGER
    );
""")

insert_comment_query = """
    INSERT INTO TT_Comment_AND (
        _idTimStamp, intTTWegNr, strEntryKommentar, entryBewertung, 
        strEntryUser, entryDatum
    ) VALUES (?, ?, ?, ?, ?, ?);
"""
#endregion

# Iterate over each Gipfel
for i in range(first_gipfel, last_gipfel + 1):
    print(f"Processing Gipfel {i}")
    
    time.sleep(2)  # Simulate a delay as in the Java code
    
    # strGipfelDetails ==> GIPFELSEITE "GPS-Koordinaten"
    # e.g.:  https://teufelsturm.de/gipfel/details.php?gipfelnr=954
    strGipfelDetails = python_get_url_source("http://teufelsturm.de", "/gipfel/details.php?gipfelnr=" + i)
    # strWegeSuche ==> GIPFELSEITE "Liste der Wege"
    # e.g.: https://teufelsturm.de/wege/suche.php?gipfelnr=954&anzahl=Alle
    strWegeSuche = python_get_url_source("https://teufelsturm.de", "/wege/suche.php?gipfelnr=" + i + "&anzahl=Alle")
    
    params = {'aIntGipfelNr': i, 'aStrGipfelDetails': strGipfelDetails, 't': strWegeSuche}
    objTT_Gipfel = tt_summit_object(**params)
    
    # Create dummy object representing Gipfel (in place of TT_Gipfel class)
    # You need to define the actual TT_Gipfel class in Python if you have it
    gipfel = {
        'intGipfelNr': objTT_Gipfel. i,
        'strName': f"Gipfel {i}",
        'dblGPS_Latitude': 50.1234,
        'dblGPS_Longitude': 13.1234,
        'strGebiet': "Gebiet name",
        'intKleFuGipfelNr': i % 10,
        'fltGPS_Altitude': 500 + i,
        'osm_type': "NODE",
        'osm_ID': i,
        'osm_display_name': f"Gipfel {i} Name",
    }

    # Insert into TT_Summit_AND table
    cursor.execute(insert_gipfel_query, (
        int(time.time()),  # Timestamp
        gipfel['intGipfelNr'], gipfel['strName'], gipfel['dblGPS_Latitude'],
        gipfel['dblGPS_Longitude'], gipfel['strGebiet'], gipfel['intKleFuGipfelNr'],
        0, 0, None, gipfel['fltGPS_Altitude'], gipfel['osm_type'], gipfel['osm_ID'],
        gipfel['osm_display_name']
    ))

    # Insert neighbors (dummy data)
    for neighbor in range(5):
        cursor.execute(insert_neighbour_query, (
            int(time.time()),  # Timestamp
            gipfel['intGipfelNr'],  # Hauptgipfel
            neighbor  # NachbarGipfelNr
        ))

    # Insert routes (dummy data)
    cursor.execute(insert_route_query, (
        int(time.time()),  # Timestamp
        i,  # WegNr
        gipfel['intGipfelNr'],  # GipfelNr
        f"Route {i}",  # WegName
        1,  # AusrufeZeichen
        5,  # Sterne
        "SchwierigkeitsGrad",  # Schwierigkeit
        10, 20, 30, 40,  # Various difficulties
        3,  # Anzahl Kommentare
        4.5,  # Mittlere Bewertung
        "Erstbegeher Name",  # Erstbegeher
        "2024-01-01",  # Erstbegehungsdatum
        "Route description"
    ))

    # Insert comments (dummy data)
    cursor.execute(insert_comment_query, (
        int(time.time()),  # Timestamp
        i,  # WegNr
        f"Comment for route {i}",  # Kommentar
        5,  # Bewertung
        f"User {i}",  # User
        int(time.time())  # Datum
    ))

# Commit and close connection
conn.commit
