import sqlite3
import os
import Levenshtein
import math
import re
# import datetime module
from datetime import datetime
from datetime import date

from summit_table_helper import get_files_dir

def move_exclamation_to_start(grade):
    # Check if the last character is an exclamation mark
    if grade.endswith(' !'):
        # Move the exclamation mark to the start
        return ('! ' + grade[:-2]).replace(' *','*')  # Add the exclamation mark to the start, and remove it from the end
    else:
        return grade  # If no exclamation mark at the end, return the string unchanged

def LongCardinalDirections(original: str):
    # Transformed value
    transformed = original.replace("NO-","Nordost-")
    transformed = transformed.replace("NW-","Nordwest-")
    transformed = transformed.replace("SO-","Südost-")
    transformed = transformed.replace("SW-","Südwest-")
    transformed = transformed.replace("S-","Süd-")
    transformed = transformed.replace("W-","West-")
    transformed = transformed.replace("N-","Nord-")
    transformed = transformed.replace("O-","Ost-")
    transformed = transformed.replace("Riß","Riss")
    if (transformed.startswith("DE ") ):
        transformed = transformed.replace("DE ", "Direkteinstieg ", 1)
    if (transformed.startswith("Var. ") ):
        transformed = transformed.replace("Var. ", "Variante ", 1)
    if (transformed == "EV"):
        transformed = "Einstiegsvariante"
    if (transformed.startswith("EV ") ):
        transformed = transformed.replace("EV", "Einstiegsvariante ", 1)
    if (transformed == "AW"):
        transformed = "Alter Weg"
    if (transformed.startswith("AW ") ):
        transformed = transformed.replace("AW ", "Alter Weg", 1)
    return transformed

route_data = []
result = []
save_dir = get_files_dir("")
climbing_routes = []
# os.remove(save_dir + "/data.sqlite")
db_all_together_data = sqlite3.connect(save_dir + "/all_together_data.sqlite")
dbCursor_sbb_data = db_all_together_data.cursor()
dbCursor_tt_data = db_all_together_data.cursor()

dbCursor_sbb_data.execute("SELECT a.sf_gipfel, a.sbb_gipfel, a.tt_strName, a.ssk_gipfelname_d from summit_data a;")
rows_gipfel = [[ idx, summits] for  idx, summits in enumerate(dbCursor_sbb_data.fetchall())]

#for i in range(0, 3):
for i in range(0, len(rows_gipfel) ):
    gipfel_steinfibel = rows_gipfel[i][1][0]
    gipfel_sbbdb = rows_gipfel[i][1][1]
    gipfel_teufelsturm = rows_gipfel[i][1][2]
    gipfel_sandstein = rows_gipfel[i][1][3]
    if gipfel_steinfibel == None:
        continue
    # print (str(i) +": sf = " + gipfel_steinfibel +"; sbb = " + gipfel_sbbdb +"; tt = " + gipfel_teufelsturm +"; ss = " + gipfel_sandstein) 
    dbCursor_ss_routes = db_all_together_data.cursor()
    dbCursor_sbb_data.execute("SELECT sbb._id, "
                              + "sbb.wegname, "
                              + "sbb.[Gesamtschwierigkeit], "
                              + "sbb.[VarianteVon_Wegname], " 
                              + "sbb.[Datum der Erstbegehung], "
                              + "sbb.[Geführt von], "
                              + "sbb.[Nachgestiegen von] FROM route_data_sbb sbb WHERE sbb.sbb_gipfel = '" + gipfel_sbbdb + "' ")
    rows_sbb_routes = [[ idx, routes] for  idx, routes in enumerate(dbCursor_sbb_data.fetchall())]

    dbCursor_ss_routes.execute("SELECT ssk.weg_ID, "
                               + "ssk.wegname_d, "
                               + "ssk.schwierigkeit, "
                               + "ssk.erstbegvorstieg, "
                               + "ssk.erstbegnachstieg, "
                               + " ssk.erstbegdatum FROM route_data_ssk ssk WHERE ssk.gipfelname_d = '" + gipfel_sandstein + "'")
    rows_ss_routes = [[ idx, routes] for  idx, routes in enumerate(dbCursor_ss_routes.fetchall())]
    
    for j in range(0, len(rows_sbb_routes) ):
        sbb_id =  str(rows_sbb_routes[j][1][0])
        sbb_name = LongCardinalDirections(rows_sbb_routes[j][1][1])
        if (sbb_name == "DE" or sbb_name == "EV" or sbb_name == "AV" or sbb_name == "Variante"):
            sbb_name = sbb_name + " " + LongCardinalDirections(rows_sbb_routes[j][1][3])
        sbb_grade = rows_sbb_routes[j][1][2]
        sbb_erstbegvorstieg = rows_sbb_routes[j][1][5]
        sbb_erstbegnachstieg = rows_sbb_routes[j][1][6]
        # convert datetime string into date,month,day
        datumErst =  rows_sbb_routes[j][1][4]       # e.g.: 16.06.1907 i.e.: dd.mm.yyyy
        m = re.match(r"\d\d\.\d\d\.\d\d\d\d", datumErst)
        if m != None:
            sbb_erstbegdatum = datetime.strptime(datumErst, '%d.%m.%Y').strftime('%Y-%m-%d')

        for i in range(0, len(rows_ss_routes) ):
            ss_id = str(rows_ss_routes[i][1][0])
            ss_name = LongCardinalDirections(rows_ss_routes[i][1][1]) 
            ss_grade = rows_ss_routes[i][1][2].replace("anstr.", "").strip()
            pat = re.compile(r"^([!\*]+)*\s*" )
            if (match := pat.search(ss_name)) is not None:
                ss_name = ss_name.replace(match.group(0), "").strip()
                ss_grade = match.group(0).strip() + " " + ss_grade
            ss_grade = move_exclamation_to_start(ss_grade)
            ss_erstbegvorstieg = rows_ss_routes[i][1][3]
            ss_erstbegnachstieg = rows_ss_routes[i][1][4]
            # convert datetime string into date,month,day
            datumErst =  rows_ss_routes[i][1][5]       # e.g.: 1987-06-21 i.e.: yyyy-mm-dd
            if datumErst != '0000-00-00':
                ss_erstbegdatum = date.fromisoformat(datumErst).isoformat()
            else:
                ss_erstbegdatum = sbb_erstbegdatum
            ### Do the Calculation....
            route_data.append([gipfel_sandstein, ss_name, ss_grade, ss_id, gipfel_sbbdb,sbb_name, sbb_grade, sbb_id,
                                math.sqrt(
                                    Levenshtein.jaro(ss_name.lower(), sbb_name.lower())**2 +  
                                    0.3*(Levenshtein.jaro(ss_grade.replace(" ", ""), sbb_grade.replace(" ", "")))**2 +   
                                    0.25*(Levenshtein.jaro(ss_erstbegvorstieg.lower(), sbb_erstbegvorstieg.lower()))**2 +   
                                    0.25*(Levenshtein.jaro(ss_erstbegvorstieg.lower(), sbb_erstbegvorstieg.lower()))**2
                                    )]
                            )
            # print("\t" + tt_name + "\t" + sbb_name + "\t" + "{:.4f}".format(Levenshtein.jaro(tt_name.lower(), sbb_name.lower())))
            # print('i: ' + "{:.1f}".format(i/len(rows_sbb)*100) + '; j: ' + "{:.1f}".format(j/len(rows_tt)*100))

    while(len(route_data)> 0):
        # print("len(summit_data): " + str(len(route_data)))
        # Step 1: Find the row with the highest value in the levenstein column
        max_row = max(route_data, key=lambda x: x[8])
        result.append(max_row)
        # Step 2: Filter out elements where the first element is "max_row[k]"
        route_data = [item for item in route_data if item[3] != max_row[3]]    
        route_data = [item for item in route_data if item[7] != max_row[7]]
        # print("Filtered out: '" + aKey + "' len(summit_data): " + str(len(route_data)))
        print(max_row)

dbCursor_ss_routes.execute("DROP TABLE IF EXISTS link_sbb2ssk;")
dbCursor_ss_routes.execute("CREATE TABLE IF NOT EXISTS link_sbb2ssk (_id INTEGER PRIMARY KEY, sbb_id INTEGER, ss_id INTEGER, Corr_Coeff FLOAT);")
print("Saving in: " + save_dir + "/routes_outfile_sbb2ssk.txt")
for item in result:
    item_sbbID = item[7]
    item_ssID =  item[3]
    item_Corr_Coeff = "{:.3f}".format(item[8] / math.sqrt(1.8) * 100) # normalized to sum of weight: sqrt(1.8) 
    print("item_sbbID: " + item_sbbID + "; item_ttID: " + item_ssID + "; " + item[5] + "; item_Corr_Coeff: " + item_Corr_Coeff)
    dbCursor_ss_routes.execute("INSERT INTO link_sbb2ssk(sbb_id , ss_id, Corr_Coeff) VALUES(" + item_sbbID + ", " + item_ssID + ", " + item_Corr_Coeff  + ")")
db_all_together_data.commit()
db_all_together_data.close()
with open( save_dir + "/routes_outfile_sbb2ssk.txt", "w", encoding='utf-8') as outfile:
    outfile.write("\n".join(str(item) for item in result))
outfile.close()

# Correlation-Table
'''     
    SELECT ss.weg_ID,           
           ss.WegName_d || ' (' || ss.gipfelname_d || ' #' || CAST(ss.gipfelid AS INTEGER)|| ')' AS [ss_wegname],
           ss.schwierigkeit, 
           CASE
               WHEN ss.[erstbegvorstieg] || ss.[erstbegnachstieg] IS '' THEN null
               ELSE ss.[erstbegvorstieg] || '/' || ss.[erstbegnachstieg]
           END ss_erstbegeher,
           ss.wegbeschr_d,
           CAST(link.Corr_Coeff AS FLOAT), 
           sbb._id,
           sbb.Wegname || ' (' || sbb.sbb_gipfel
                       || '; #' || CAST(sbb.sbb_gipfel_ID AS INTEGER)
                       || ' - ' || sbb.sbb_Gebiet  
                       || ')'  AS [sbb_Wegname], 
           sbb.[Gesamtschwierigkeit], 
           sbb.VarianteVon_Wegname, 
           sbb.[Einsortierung im Kletterführer (nach welchem Weg?)], 
           sbb.Wegbeschreibung
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ss WHERE Corr_Coeff >= 70.0) AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN  route_data_ss ss ON ss.weg_ID = link.ss_id 
        WHERE sbb.sbb_gipfel = 'David' 
    UNION
      SELECT ss.weg_ID, 
           ss.WegName_d || ' (' || ss.gipfelname_d || ' #' || CAST(ss.gipfelid AS INTEGER)|| ')' AS [ss_wegname],
           ss.schwierigkeit, 
           CASE
               WHEN ss.[erstbegvorstieg] || ss.[erstbegnachstieg] IS '' THEN null
               ELSE ss.[erstbegvorstieg] || '/' || ss.[erstbegnachstieg]
           END ss_erstbegeher,
           ss.wegbeschr_d,
           NULL AS Corr_Coeff, 
           NULL AS [sbb._id], 
           NULL AS [sbb_Wegname], 
           NULL AS [sbb.Gesamtschwierigkeit], 
           NULL AS [sbb.VarianteVon_Wegname], 
           NULL AS [sbb.Einsortierung im Kletterführer (nach welchem Weg?)], 
           NULL AS [sbb.Wegbeschreibung]
      FROM route_data_ss ss  
      WHERE ss.gipfelname_d = 'David' 
      AND ss.weg_ID NOT IN (SELECT DISTINCT(weg_ID) FROM 
        (
        SELECT ss.weg_ID
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ss WHERE Corr_Coeff > 70.0) AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN  route_data_ss ss ON ss.weg_ID = link.ss_id 
        WHERE sbb.sbb_gipfel = 'David' 
        ORDER BY sbb._id 
        )
       WHERE weg_ID NOT NULL)
      ORDER BY sbb._id NULLS LAST
  ;
'''

#route_data_sbb
'''
DROP TABLE IF EXISTS route_data_sbb;
CREATE TABLE route_data_sbb AS 
SELECT 
	sbb.[_id],
  gi.[sbb_Gebiet],
  gi.[sbb_gipfel_ID],
	gi.[sbb_gipfel],
	sbb.[Wegname],
	sbb.[Datum der Erstbegehung],
	sbb.[Geführt von],
	sbb.[Nachgestiegen von],
	sbb.[Wegbeschreibung],
	sbb.[Einsortierung im Kletterführer (nach welchem Weg?)],
	sbb.[Variante von],
    sbb.[Gesamtschwierigkeit],
	sbb.[Schwierigkeit a.f. bzw. m.U.],
	sbb.[Schwierigkeit o.U.],
	sbb.[Schwierigkeit RP],
	sbb.[Sprungschwierigkeit],
	sbb.[Sternchen & Ausrufezeichen],
	sbb.[Brüchig],
	sbb.[Anstrengend],
	sbb.[Erstbegehung im Rotpunkt],
	sbb.[offene Schadensmeldungen],
	sbb.[offene Umstufungsvorschläge],
	sbb.[VarianteVon_Ausrufezeichen],
	sbb.[VarianteVon_Wegname],
	sbb.[VarianteVon_AfMuSchwierigkeit],
	sbb.[VarianteVon_RPSchwierigkeit],
	sbb.[VarianteVon_OUSchwierigkeit],
	sbb.[VarianteVon_Sprungschwierigkeit],
	sbb.[VarianteGeführtVon],
	sbb.[VarianteNachgestiegenVon],
	sbb.[VarianteVon_DatumDerErstbegehung],
	sbb.[EinsortierungNach_Ausrufezeichen],
	sbb.[EinsortierungNach_Wegname],
	sbb.[EinsortierungNach_AfMuSchwierigkeit],
	sbb.[EinsortierungNach_RPSchwierigkeit],
	sbb.[EinsortierungNach_OUSchwierigkeit],
	sbb.[EinsortierungNach_Sprungschwierigkeit],
	sbb.[EinsortierungNach_WegNameVariante]
FROM data.data sbb, gipfel_data gi
WHERE sbb.Gipfel = gi.sbb_gipfel
ORDER BY CAST(sbb._id AS INTEGER)
'''

#route_data_ss
'''
DROP TABLE IF EXISTS route_data_ss;
CREATE TABLE route_data_ss AS SELECT 
       r.[weg_ID],
       ge.sektorname_d,   
       r.[gipfelid],
       gi.[gipfelname_d],
       gi.[gipfelname_cz],   
       r.[schwierigkeit],   
       r.[skala_sachsen], 
       r.[baustelle],
       r.[skala_rp], 
       r.[skala_sprung], 
       r.[blnAusrufeZeichen], 
       r.[erstbegvorstieg], 
       r.[erstbegnachstieg], 
       r.[erstbegdatum], 
       r.[ringzahl], 
       r.[wegbeschr_d], 
       r.[wegbeschr_cz], 
       r.[kletterei], 
       r.[wegname_d], 
       r.[wegname_cz], 
       r.[wegstatus], 
       r.[wegnr] 
 FROM  DB_SandSteinKlettern.wege r, DB_SandSteinKlettern.gipfel gi, DB_SandSteinKlettern.gebiet ge   
 WHERE r.gipfelid = gi.gipfel_ID AND gi.sektorid = ge.[sektor_ID]
'''
#route_data_TT
'''
DROP TABLE IF EXISTS route_data_TT;
CREATE TABLE route_data_TT AS SELECT 
     tt.[intTTWegNr],
     gi.[strGebiet],
     tt.[intTTGipfelNr],
     gi.[strName],
     tt.[WegName],
     tt.[blnAusrufeZeichen],
     tt.[intSterne],
     tt.[strSchwierigkeitsGrad],
     tt.[sachsenSchwierigkeitsGrad],
     tt.[ohneUnterstuetzungSchwierigkeitsGrad],
     tt.[rotPunktSchwierigkeitsGrad],
     tt.[intSprungSchwierigkeitsGrad],
     tt.[intAnzahlDerKommentare],
     tt.[fltMittlereWegBewertung] 
 FROM  TT_DownLoader_PC.TT_Route_AND tt, TT_DownLoader_PC.TT_Summit_AND gi   
 WHERE tt.intTTGipfelNr = gi.intTTGipfelNr 
 '''