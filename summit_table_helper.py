import pandas as pd
import sqlite3
import os

def get_files_dir(run_name: str):
    # Directory to save the database file
    dirname = os.path.dirname(__file__)
    d = os.path.join(dirname, run_name)
    os.makedirs(d, exist_ok=True)
    return d

if __name__ == '__main__':
    save_dir = get_files_dir("")
    print ("Writing all data in SQLITE database in: " + str(save_dir))

    print ("###################################################################################" )
    print ("### ADDING data from summmit table (excel/ods)")
    print ("###################################################################################" )
    db = sqlite3.connect(save_dir + "/all_together_data.sqlite")
    odsdata = pd.read_excel(".\summit_data.ods", engine="odf")
    odsdata.to_sql('summit_data', db, if_exists='replace')


    print ("###################################################################################" )
    print ("### ADDING data from fetched sandsteinklettern DB")
    print ("###################################################################################")
    db.execute('ATTACH DATABASE "F:\\Programming\\git\\SaechsischeKletterforen\\fetch_sandsteinklettern\\ssk_database\\DB_SandSteinKlettern.sqlite" AS ssk')
    create_skk_tabele_in_all = '''DROP TABLE IF EXISTS route_data_ssk;'''
    db.execute(create_skk_tabele_in_all)
    create_skk_tabele_in_all = '''CREATE TABLE route_data_ssk AS SELECT 
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
    FROM  ssk.wege r, ssk.gipfel gi, ssk.gebiet ge   
    WHERE r.gipfelid = gi.gipfel_ID AND gi.sektorid = ge.[sektor_ID]
    '''
    db.execute(create_skk_tabele_in_all)

    print ("###################################################################################")
    print ("### ADDING data from fetched SBB DB")
    print ("###################################################################################")
    db.execute('ATTACH DATABASE "F:\\Programming\\git\\SaechsischeKletterforen\\fetch_sbb\\sbb_database\\sbb_data.sqlite" AS sbb')
    create_sbb_tabele_in_all = '''DROP TABLE IF EXISTS route_data_sbb;'''
    db.execute(create_sbb_tabele_in_all)
    create_sbb_tabele_in_all = '''
    CREATE TABLE route_data_sbb AS 
    SELECT 
        sbb.[_id],
    gi.[sbb_Gebiet],
    gi.[sbb_gipfel_ID],
        gi.[sbb_gipfel],
        gi.[sbb_gipfel_Nr],
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
    FROM sbb.data sbb, summit_data gi
    WHERE sbb.Gipfel = gi.sbb_gipfel
    ORDER BY CAST(sbb._id AS INTEGER);
    '''
    db.execute(create_sbb_tabele_in_all)

    print ("###################################################################################")
    print ("### ADDING data from fetched TEUFELSTURM DB")
    print ("###################################################################################")
    db.execute('ATTACH DATABASE "F:\\Programming\\git\\SaechsischeKletterforen\\fetch_teufelsturm\\tt_database\\TT_DownLoader_PC.sqlite" AS tt;')
    create_tt_tabele_in_all = '''DROP TABLE IF EXISTS route_data_tt;'''
    db.execute(create_tt_tabele_in_all)
    create_tt_tabele_in_all = '''CREATE TABLE route_data_TT AS SELECT 
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
    FROM  tt.TT_Route_AND tt, tt.TT_Summit_AND gi   
    WHERE tt.intTTGipfelNr = gi.intTTGipfelNr;'''
    db.execute(create_tt_tabele_in_all)

    db.close()


