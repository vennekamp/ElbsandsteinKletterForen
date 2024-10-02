

import sqlite3

import os
import urllib.request

def python_get_url_source(link):
    builder = []
    try:
        req = urllib.request.Request(
            link, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2'}
        )
        with urllib.request.urlopen(req) as response:
            for line in response:
                builder.append(line.decode('utf-8'))
    except Exception as ex:
        print(f"Error occurred: {ex}")
        raise RuntimeError(ex)
    
    return ''.join(builder)


def get_path_to_sqlite_db_file():
    return os.path.join("F:", "Programming", "git", "TT_DownLoaderPC_Netbeans", "TT_DownLoader_PC_2.sqlite")



def create_1b_data_table_android_app(cursor):
    # SQLite Statement to create the "MY Route Data" table
    print("****   SQLite Statement zur Erzeugung der \"MEINE Routen Daten\" Tabelle")
    cursor.execute("DROP TABLE IF EXISTS myTT_Route_AND;")
    cursor.execute("DROP TABLE IF EXISTS MyTT_Comment_AND;")
    
    cursor.execute("""
        CREATE TABLE MyTT_Comment_AND(
            _id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, -- #01 - ID
            myCommentTimStamp INTEGER NOT NULL, -- #02 - TIME STAMP
            myIntTTGipfelNr INTEGER NOT NULL, -- #03 - gipfel nr (TT)
            myIntTTWegNr INTEGER, -- #04 - weg nr (TT)
            myAscendedPartner TEXT, -- #05 - Partner (Name)
            isAscendedType INTEGER NOT NULL, -- #06 - wie bestiegen z.B.: 0 - nix; 1 - Will mal
            myIntDateOfAscend TEXT, -- #07 - Datum der Besteigung als formatierter String
            strMyComment TEXT -- #07 - meine Bemerkungen (eigener Kommentar)
        );
    """)

    # SQLite Statement to create the "MY Summit Data" table
    print("****   SQLite Statement zur Erzeugung der \"MEINE Gipfel Daten\" Tabelle")
    cursor.execute("DROP TABLE IF EXISTS myTT_Summit_AND;")
    
    cursor.execute("""
        CREATE TABLE MyTT_Summit_AND(
            _id INTEGER PRIMARY KEY NOT NULL, 
            mySummitCommentTimStamp INTEGER NOT NULL, 
            myIntTTGipfelNr INTEGER NOT NULL, 
            isAscendedSummit INTEGER, 
            myIntDateOfAscend INTEGER, 
            strMySummitComment TEXT
        );
    """)

    cursor.execute("DROP TABLE IF EXISTS MyTT_RoutePhotos_AND;")
    
    cursor.execute("""
        CREATE TABLE MyTT_RoutePhotos_AND(
            _id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, -- Ignore on conflict AUTOINCREMENT
            commentID INTEGER NOT NULL, 
            uri TEXT, 
            caption TEXT
        );
    """)

    cursor.execute("DROP TABLE IF EXISTS MyTT_Route_AND;")
    
    cursor.execute("""
        CREATE TABLE MyTT_Route_AND(
            _id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            myRouteCommentTimStamp INTEGER NOT NULL, 
            myIntTTWegNr INTEGER NOT NULL, 
            myAscendedPartner TEXT, 
            isAscendedRouteType INTEGER, 
            myIntDateOfAscendRoute TEXT, 
            strMyRouteComment TEXT
        );
    """)

    cursor.execute("DROP TABLE IF EXISTS MyTT_Summit_AND;")
    
    cursor.execute("""
        CREATE TABLE MyTT_Summit_AND(
            _id INTEGER PRIMARY KEY NOT NULL, 
            mySummitCommentTimStamp INTEGER NOT NULL, 
            myIntTTGipfelNr INTEGER NOT NULL, 
            isAscendedSummit INTEGER, 
            myIntDateOfAscend INTEGER, 
            strMySummitComment TEXT
        );
    """)

# Example usage
# Connect to the SQLite database and create a cursor
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Call the function to create tables
create_1b_data_table_android_app(cursor)

# Commit the transaction and close the connection
conn.commit()
conn.close()
