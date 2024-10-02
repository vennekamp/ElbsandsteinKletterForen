import sqlite3
import os
import re 

GRADES = ["I", "II", "III", "IV", "V", "VI", "VIIa", "VIIb", "VIIc", "VIIIa", "VIIIb", "VIIIc", "IXa", "IXb", "IXc",
          "Xa", "Xb", "Xc", "XIa", "XIb", "XIc", "XIIa", "XIIb", "XIIc", "XIIIa", "XIIIb", "XIIIc"]
REGEX_STERNCHEN_AUSRUFEZEICHEN = r'([!|*|**])\s'
REGEX_RP_GRADES = 'RP\s'+'$|RP\s'.join(reversed(GRADES)) + '$'
REGEX_OU_GRADES = '\(('+')\)$|\(('.join(reversed(GRADES))+')\)' + '$'
REGEX_GRADES = '$|\s'.join(reversed(GRADES)) + '$'
REGEX_UIAA_GRADES_AT_END = '7a$|7b$|7c$|8a$|8b$|8c$|9a$|9b$|9c$|10a$|10b$|10c$|11a$|11b$|11c$|12a$|12b$|12c$'

def run_dir(run_name: str):
    # Directory to save the HTML files
    d = os.path.join(os.getcwd(), "data", run_name)
    os.makedirs(d, exist_ok=True)
    return d
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def get_Praedikate(VarianteVonWegPraedikatNameGrade):
    VarianteVon_Ausrufezeichen = ''
    while re.match( r'^[!*]', VarianteVonWegPraedikatNameGrade):
        VarianteVon_Ausrufezeichen += VarianteVonWegPraedikatNameGrade[:1]
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade[1:]
    VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade.strip()
    return VarianteVonWegPraedikatNameGrade,VarianteVon_Ausrufezeichen
def get_RPSchwierigkeit(VarianteVonWegPraedikatNameGrade):
    VarianteVon_RPSchwierigkeit = ''
    m = re.search(REGEX_RP_GRADES, VarianteVonWegPraedikatNameGrade, re.MULTILINE) 
    if m: 
        VarianteVon_RPSchwierigkeit = m.group(0)
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade.replace(VarianteVon_RPSchwierigkeit, '').strip()
    return VarianteVonWegPraedikatNameGrade,VarianteVon_RPSchwierigkeit[3:].strip()
def get_OUSchwierigekeit(VarianteVonWegPraedikatNameGrade):
    VarianteVon_OUSchwierigkeit = ''
    m = re.search(REGEX_OU_GRADES, VarianteVonWegPraedikatNameGrade) 
    if m: 
        VarianteVon_OUSchwierigkeit = m.group()[1:-1]
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade.replace(m.group(), '').strip()
    return VarianteVonWegPraedikatNameGrade,VarianteVon_OUSchwierigkeit
def get_AfmUSchwierigkeit(VarianteVonWegPraedikatNameGrade):
    VarianteVon_AfMuSchwierigkeit = ''
    m = re.search(REGEX_GRADES, VarianteVonWegPraedikatNameGrade) 
    if m: 
        VarianteVon_AfMuSchwierigkeit = m.group()
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade.replace(VarianteVon_AfMuSchwierigkeit, '').strip()
    return VarianteVonWegPraedikatNameGrade,VarianteVon_AfMuSchwierigkeit
def get_SprungSchwierigkeit(VarianteVonWegPraedikatNameGrade):
    VarianteVon_Sprungschwierigkeit = ''
    # Sprungschwierigkeit ist mit backslash abgetrennt vom Rest
    if VarianteVonWegPraedikatNameGrade.endswith('/'): 
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade[:-1]
    m = re.search(r'\d$', VarianteVonWegPraedikatNameGrade)
    # if the string ends in digit m will be a Match object, or None otherwise.
    if m:
        VarianteVon_Sprungschwierigkeit = m.group()
        VarianteVonWegPraedikatNameGrade = VarianteVonWegPraedikatNameGrade.replace(m.group(), '').strip()
    return VarianteVonWegPraedikatNameGrade,VarianteVon_Sprungschwierigkeit
def get_RPSchwierigkeit_from_UIAA(grade_UIAA:str) -> str:
    if grade_UIAA.startswith('7'): return 'RP ' + grade_UIAA.replace('7','VII')
    elif grade_UIAA.startswith('8'): return 'RP ' + grade_UIAA.replace('8','VIII')
    elif grade_UIAA.startswith('9'): return 'RP ' + grade_UIAA.replace('9','IX')
    elif grade_UIAA.startswith('10'): return 'RP ' + grade_UIAA.replace('10','X')
    elif grade_UIAA.startswith('11'): return 'RP ' + grade_UIAA.replace('11','XI')
    elif grade_UIAA.startswith('12'): return 'RP ' + grade_UIAA.replace('12','XII')
    raise Exception
def get_data_Variante_von( text_VarianteVon: str) -> dict:
    dict_VarianteVon = {'VarianteVon_Ausrufezeichen': '', 'VarianteVon_Wegname': '', 'VarianteVon_AfMuSchwierigkeit': '','VarianteVon_RPSchwierigkeit': '', \
                        'VarianteVon_OUSchwierigkeit': '', 'VarianteVon_Sprungschwierigkeit': '', 'VarianteGeführtVon': '', 'VarianteNachgestiegenVon': '', \
                        'VarianteVon_DatumDerErstbegehung':''}
    if len(text_VarianteVon) < 2: return dict_VarianteVon
    VarianteVon = text_VarianteVon
    VarianteVonWegPraedikatNameGrade = VarianteVon.split('; ')[0]
    
    # Variante von: Sternchen & Ausrufezeichen
    VarianteVonWegPraedikatNameGrade, VarianteVon_Ausrufezeichen = get_Praedikate(VarianteVonWegPraedikatNameGrade)
    dict_VarianteVon['VarianteVon_Ausrufezeichen'] = VarianteVon_Ausrufezeichen    
    # Variante von: RP Schwierigkeit
    VarianteVonWegPraedikatNameGrade, VarianteVon_RPSchwierigkeit = get_RPSchwierigkeit(VarianteVonWegPraedikatNameGrade)
    dict_VarianteVon['VarianteVon_RPSchwierigkeit'] = VarianteVon_RPSchwierigkeit    
    # Variante von: OU Schwierigkeit
    VarianteVonWegPraedikatNameGrade, VarianteVon_OUSchwierigkeit = get_OUSchwierigekeit(VarianteVonWegPraedikatNameGrade)
    dict_VarianteVon['VarianteVon_OUSchwierigkeit'] = VarianteVon_OUSchwierigkeit    
    # Variante von: Schwierigkeit a.f. bzw. m.U.
    VarianteVonWegPraedikatNameGrade, VarianteVon_AfMuSchwierigkeit = get_AfmUSchwierigkeit(VarianteVonWegPraedikatNameGrade)
    dict_VarianteVon['VarianteVon_AfMuSchwierigkeit'] = VarianteVon_AfMuSchwierigkeit
    # Variante von: Sprungschwierigkeit
    VarianteVonWegPraedikatNameGrade, VarianteVon_Sprungschwierigkeit = get_SprungSchwierigkeit(VarianteVonWegPraedikatNameGrade)
    dict_VarianteVon['VarianteVon_Sprungschwierigkeit'] = VarianteVon_Sprungschwierigkeit
    # Variante von: Wegname --> Der Rest...
    VarianteVon_Wegname = VarianteVonWegPraedikatNameGrade
    dict_VarianteVon['VarianteVon_Wegname'] = VarianteVon_Wegname
    # Datum 
    VarianteVonErstbegher_Datum = VarianteVon.split('; ')[1].split(' – ')[0]
    # Variante von: Datum der Erstbegehung
    VarianteVon_DatumDerErstbegehung = ''
    m = re.search(r'(\d\d\.\d\d\.\d\d\d\d)$', VarianteVonErstbegher_Datum)
    if m:
        VarianteVon_DatumDerErstbegehung = m.group()
        VarianteVonErstbegher_Datum = VarianteVonErstbegher_Datum.replace(VarianteVon_DatumDerErstbegehung, '').strip()
    dict_VarianteVon['VarianteVon_DatumDerErstbegehung'] = VarianteVon_DatumDerErstbegehung
    if VarianteVonErstbegher_Datum.endswith(','):
        VarianteVonErstbegher_Datum = VarianteVonErstbegher_Datum[:-1].strip()
    VarianteGeführtVon = '' 
    VarianteNachgestiegenVon = ''
    VariantenBeherArray = VarianteVonErstbegher_Datum.split(',', maxsplit=1)
    if len(VariantenBeherArray) > 0 : 
        VarianteGeführtVon = VariantenBeherArray[0].strip()
    dict_VarianteVon['VarianteGeführtVon'] = VarianteGeführtVon
    if len(VariantenBeherArray) > 1 : 
        VarianteNachgestiegenVon = VariantenBeherArray[1].strip()
    dict_VarianteVon['VarianteNachgestiegenVon'] = VarianteNachgestiegenVon
    dict_VarianteVon['VarianteVon_Sprungschwierigkeit'] = VarianteVon_Sprungschwierigkeit
   
    return dict_VarianteVon
def get_data_EinsortierungNach( EinsortierungImKletterführer_NachWelchemWeg: str) -> dict:
    dict_EinsortierungNach  = {'EinsortierungNach_Ausrufezeichen': '', 'EinsortierungNach_Wegname': '', 'EinsortierungNach_AfMuSchwierigkeit': '', \
                               'EinsortierungNach_RPSchwierigkeit': '', 'EinsortierungNach_OUSchwierigkeit': '', 'EinsortierungNach_Sprungschwierigkeit': '', \
                               'EinsortierungNach_WegNameVariante': ''}
        # Variante von: Sternchen & Ausrufezeichen
    EinsortierungImKletterführer_NachWelchemWeg, VarianteVon_Ausrufezeichen = get_Praedikate(EinsortierungImKletterführer_NachWelchemWeg)
    dict_EinsortierungNach['EinsortierungNach_Ausrufezeichen'] = VarianteVon_Ausrufezeichen    
    while True:
        # Variante von: RP Schwierigkeit
        ''' manchmal gibt es eine UIAA artige Bewertung der RP-Schwierigkeit.... '''
        EinsortierungImKletterführer_RPchwierigkeit = ''
        m = re.search(REGEX_UIAA_GRADES_AT_END, EinsortierungImKletterführer_NachWelchemWeg) 
        if m: 
            EinsortierungImKletterführer_NachWelchemWeg = re.sub(REGEX_UIAA_GRADES_AT_END, get_RPSchwierigkeit_from_UIAA(m.group()), EinsortierungImKletterführer_NachWelchemWeg)
        EinsortierungImKletterführer_NachWelchemWeg, EinsortierungImKletterführer_RPchwierigkeit = get_RPSchwierigkeit(EinsortierungImKletterführer_NachWelchemWeg)
        if EinsortierungImKletterführer_RPchwierigkeit != '':
            dict_EinsortierungNach['EinsortierungNach_RPSchwierigkeit'] = EinsortierungImKletterführer_RPchwierigkeit    
        # es kann vor dem RP die Sprungschwierigkeit stehen
        VarianteVon_Sprungschwierigkeit = ''
        m = re.search(r'\,\s(\d)\/$', EinsortierungImKletterführer_NachWelchemWeg) 
        if m: 
            VarianteVon_Sprungschwierigkeit = m.group(1)
            EinsortierungImKletterführer_NachWelchemWeg = re.sub(r'\,\s(\d)\/$', '', EinsortierungImKletterführer_NachWelchemWeg)
            dict_EinsortierungNach['EinsortierungNach_Sprungschwierigkeit'] = VarianteVon_Sprungschwierigkeit
        # Variante von: OU Schwierigkeit
        EinsortierungImKletterführer_NachWelchemWeg, VarianteVon_OUSchwierigkeit = get_OUSchwierigekeit(EinsortierungImKletterführer_NachWelchemWeg)
        if VarianteVon_OUSchwierigkeit != '':
            dict_EinsortierungNach['EinsortierungNach_OUSchwierigkeit'] = VarianteVon_OUSchwierigkeit
        # Variante von: Schwierigkeit a.f. bzw. m.U.
        EinsortierungImKletterführer_NachWelchemWeg, VarianteVon_AfMuSchwierigkeit = get_AfmUSchwierigkeit(EinsortierungImKletterführer_NachWelchemWeg)
        if VarianteVon_AfMuSchwierigkeit != '':
            dict_EinsortierungNach['EinsortierungNach_AfMuSchwierigkeit'] = VarianteVon_AfMuSchwierigkeit
        if EinsortierungImKletterführer_NachWelchemWeg.endswith(','): EinsortierungImKletterführer_NachWelchemWeg= EinsortierungImKletterführer_NachWelchemWeg[:-1].strip()
        # Variante von: Sprungschwierigkeit
        EinsortierungImKletterführer_NachWelchemWeg, VarianteVon_Sprungschwierigkeit = get_SprungSchwierigkeit(EinsortierungImKletterführer_NachWelchemWeg)
        if VarianteVon_Sprungschwierigkeit != '':
            dict_EinsortierungNach['EinsortierungNach_Sprungschwierigkeit'] = VarianteVon_Sprungschwierigkeit
        m = re.search(REGEX_UIAA_GRADES_AT_END, EinsortierungImKletterführer_NachWelchemWeg) 
        if not bool(re.search(REGEX_UIAA_GRADES_AT_END, EinsortierungImKletterführer_NachWelchemWeg)): break
    # Variante von: Wegname --> Der Rest...
    EinsortierungImKletterführer_NachWelchemWeg = re.sub('\s\(.*\)','', EinsortierungImKletterführer_NachWelchemWeg).strip()
    EinsortierungNach_Wegname = EinsortierungImKletterführer_NachWelchemWeg
    dict_EinsortierungNach['EinsortierungNach_Wegname'] = EinsortierungNach_Wegname
    return dict_EinsortierungNach

if __name__ == "__main__":
    save_dir = run_dir("full1")
    climbing_routes = []
    # os.remove(save_dir + "/data.sqlite")
    db = sqlite3.connect(save_dir + "/data.sqlite")
    dbCursor = db.cursor()
    dbCursor.execute("SELECT a.* FROM data a WHERE Gipfel = 'Geyergucke' or Gipfel = 'Steinbruchturm' OR Gipfel = 'Khedive' ORDER BY gipfel ")
    rows = dbCursor.fetchall ( )

    for row in rows :
        climbing_routes.append(dict(zip([c[0] for c in dbCursor.description], row)))
    # Accessing the information for the forty-sixth route
    assert len(climbing_routes) == 68, "not the expected number of entries fetched...!"
    assert climbing_routes[67]['Wegname'] == 'Sternschnuppe', "not the expected route at last position...!"

    for i in range(0, len(climbing_routes)):
        sub_element_dict = climbing_routes[i]
        if sub_element_dict['Wegname'] == 'Feder':
            print(sub_element_dict)
        # Alle Einträge 'Variante von' auswerten
        VarianteVon = sub_element_dict['Variante von']
        climbing_routes[i] = {**sub_element_dict, **get_data_Variante_von(VarianteVon)}
        # Alle Einträge 'Einsortierung im Kletterführer (nach welchem Weg?)' auswerten
        EinsortierungImKletterführer_NachWelchemWeg =  sub_element_dict['Einsortierung im Kletterführer (nach welchem Weg?)']
        if 'keine Angabe' == EinsortierungImKletterführer_NachWelchemWeg or '' == EinsortierungImKletterführer_NachWelchemWeg:
            continue
        # print(EinsortierungImKletterführer_NachWelchemWeg)
        climbing_routes[i] = {**sub_element_dict, **get_data_EinsortierungNach(sub_element_dict['Einsortierung im Kletterführer (nach welchem Weg?)'])}
'''
example_climbing_routes = [
    {
        'Wegname': 'AW',
        'Datum der Erstbegehung': '08.05.1951',
        'Geführt von': 'Paul Müller',
        'Nachgestiegen von': 'K. Bendel',
        'Wegbeschreibung': 'ΝO-Kante zG.',
        'Einsortierung im Kletterführer (nach welchem Weg?)': 'keine Angabe',
        'Variante von': '-',
        'Schwierigkeit a.f. bzw. m.U.': 'V',
        'Schwierigkeit o.U.': '-',
        'Schwierigkeit RP': '-',
        'Sprungschwierigkeit': '-',
        'Sternchen & Ausrufezeichen': '*'
    },
    {
        'Wegname': 'O-Wand',
        'Datum der Erstbegehung': '08.07.1951',
        'Geführt von': 'Hans Michael',
        'Nachgestiegen von': 'G. Geppert, W. Gedlich, Eugen Loos, Werner Donhof',
        'Wegbeschreibung': 'Etwa 3 m Ɩi. vom AW Wand zu Band. Linksanst. (R) zur seichten Rinne des „SO-Weges“. Diesen zG.',
        'Einsortierung im Kletterführer (nach welchem Weg?)': '* AW V',
        'Variante von': 'VIIb',
        'Schwierigkeit a.f. bzw. m.U.': '-',
        'Schwierigkeit o.U.': 'VIIb',
        'Schwierigkeit RP': 'VIIb',
        'Sprungschwierigkeit': '-',
        'Sternchen & Ausrufezeichen': '!'
    },
    {
        'Wegname': 'Direkte O-Wand',
        'Datum der Erstbegehung': '06.08.1972',
        'Geführt von': 'Gisbert Ludewig',
        'Nachgestiegen von': 'H. Maatz, H. J. Höne',
        'Wegbeschreibung': '1 m re. vom R Wand ger. zG.',
        'Einsortierung im Kletterführer (nach welchem Weg?)': '! O-Wand VIIb RP VIIb',
        'Variante von': '! O-Wand VIIb RP VIIb; Hans Michael, G. Geppert, W. Gedlich, E. Loos, W. Donhof, 08.07.1951 – Etwa 3 m li. vom AW Wand zu Band. Linksanst. (R) zur seichten Rinne des „SO-Weges“. Diesen zG.',
        'Schwierigkeit a.f. bzw. m.U.': 'VIIb',
        'Schwierigkeit o.U.': '-',
        'Schwierigkeit RP': '-',
        'Sprungschwierigkeit': '!*',
        'Sternchen & Ausrufezeichen': '*'
     },
    {
        'Wegname': 'Kurz und Schmerzlos',
        'Datum der Erstbegehung': '31.03.1973',
        'Geführt von': 'Hans Michael',
        'Nachgestiegen von': 'Rainer Walther, Klaus Richter',
        'Wegbeschreibung': '6 m Ɩi. der UG-Route zG.',
        'Einsortierung im Kletterführer (nach welchem Weg?)': 'keine Angabe',
        'Variante von': '-',
        'Schwierigkeit a.f. bzw. m.U.': 'VIIc',
        'Schwierigkeit o.U.': '-',
        'Schwierigkeit RP': '-',
        'Sprungschwierigkeit': '-',
        'Sternchen & Ausrufezeichen': '*'
    },
    {
        'Wegname': 'Südwestwand',
        'Datum der Erstbegehung': '11.04.1959',
        'Geführt von': 'Hans Michael',
        'Nachgestiegen von': 'H. Grösch, R. Wittmann',
        'Wegbeschreibung': '5 m Ɩi. der UG-Route zG.',
        'Einsortierung im Kletterführer (nach welchem Weg?)': 'keine Angabe',
        'Variante von': '-',
        'Schwierigkeit a.f. bzw. m.U.': '-',
        'Schwierigkeit o.U.': '-',
        'Schwierigkeit RP': 'VI',
        'Sprungschwierigkeit': '-',
        'Sternchen & Ausrufezeichen': '*'
    }
    # Add more entries as needed
]

# Accessing the information for the first route
#print(climbing_routes[0]['Gipfel'])  # Output: Geyergucke
'''