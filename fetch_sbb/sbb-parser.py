from bs4 import BeautifulSoup
# importing the pandas library
import pandas as pd
import sqlite3
import os
from sbb_expand_variante_Einsortierung import get_data_EinsortierungNach, get_data_Variante_von
from sbb_downloader import get_files_dir

def clean_dict(sub_element_dict: dict) -> dict:
    if 'offene Schadensmeldungen' in sub_element_dict: 
        sub_element_dict['offene Schadensmeldungen'] = sub_element_dict['offene Schadensmeldungen'].replace('Es liegen derzeit keine Schadensmeldungen vor.', '')
    else:
        sub_element_dict['offene Schadensmeldungen'] =''
    if 'offene Umstufungsvorschläge' in sub_element_dict: 
        sub_element_dict['offene Umstufungsvorschläge'] = sub_element_dict['offene Umstufungsvorschläge'].replace('Es liegen derzeit keine Vorschläge zur Umstufung der Schwierigkeit oder zur Änderung der Prädikate vor. Die angezeigten Schwierigkeiten und Eigenschaften wurden jedoch in der Vergangenheit angepasst.','')
    else:
        sub_element_dict['offene Umstufungsvorschläge'] = ''
    sub_element_dict["Anstrengend"] = sub_element_dict["Anstrengend"].apply(lambda x: 1 if x == "Ja" else 0)
    sub_element_dict["Brüchig"] = sub_element_dict["Brüchig"].apply(lambda x: 1 if x == "Ja" else 0)
    sub_element_dict["Sternchen & Ausrufezeichen"] = sub_element_dict["Sternchen & Ausrufezeichen"].apply(lambda x: "-" if x == "ohne" else x)
    sub_element_dict["Erstbegehung im Rotpunkt"] = sub_element_dict["Erstbegehung im Rotpunkt"].apply(lambda x: 1 if x == "Ja" else 0)
    sub_element_dict["Sprungschwierigkeit"] = sub_element_dict["Sprungschwierigkeit"].apply(lambda x: x.replace("Sprung", ""))
    return sub_element_dict


def getGesamtschwierigkeit(sub_element_dict: dict) -> str:
    rtnValue = ''
    stern = sub_element_dict['Sternchen & Ausrufezeichen']
    af = sub_element_dict['Schwierigkeit a.f. bzw. m.U.']
    oU = sub_element_dict['Schwierigkeit o.U.']
    rp = sub_element_dict['Schwierigkeit RP']
    spr = sub_element_dict['Sprungschwierigkeit']
    if (stern != '-' and  stern != 'ohne'):  rtnValue += stern + ' '
    if (af != '-'):     rtnValue += af + ' '
    if (oU != '-'):     rtnValue += '(' + oU + ') '
    if (rp != '-'):     rtnValue += 'RP ' + rp + ' '
    if (spr != '-'):    rtnValue += spr.replace('Sprung ', '')
    return rtnValue.strip()

if __name__ == '__main__':
    save_dir = get_files_dir("sbb_database")
    print ("Writing all data in SQLITE database in: " + str(save_dir))
    # os.remove(save_dir + "/data.sqlite")
    db = sqlite3.connect(save_dir + "/sbb_data.sqlite")
    db.execute('drop table if exists data')
    # Use os.listdir() to get a list of all files in the directory
    all_files = os.listdir( get_files_dir('sbb_HTMLfiles') )

    print ("Reading 'all_files': " + str(all_files.count))
    # all_files = ['page_no0044.html']
    # Filter files based on the specified file type
    file_list = [file for file in all_files if file.startswith("page_no")]
    print ("Extracted 'file_list': " + str(file_list.count))
    old_element_gipfel = ''
    summit_index = 0
    route_index = 10
    for file in file_list:
        print ("Reading: " + file)
        f = open( get_files_dir('sbb_HTMLfiles') + '\\' + file, "r", encoding="utf-8")
        content = f.read()
        f.close()
        soup = BeautifulSoup(content, features="lxml")
        element_list = soup.findAll("div", {"class": "panel panel-gray"})

        # creating the DataFrame
        wege = pd.DataFrame(columns = ['_id', 'Gipfel', 'Wegname', 'Datum der Erstbegehung', 'Geführt von', 'Nachgestiegen von', 'Wegbeschreibung', \
                        'Einsortierung im Kletterführer (nach welchem Weg?)', 'Variante von', \
                        'Gesamtschwierigkeit', 'Schwierigkeit a.f. bzw. m.U.', 'Schwierigkeit o.U.', 'Schwierigkeit RP', 'Sprungschwierigkeit',\
                        'Sternchen & Ausrufezeichen', 'Brüchig', 'Anstrengend', 'Erstbegehung im Rotpunkt', \
                        'offene Schadensmeldungen', 'offene Umstufungsvorschläge'])
        for element in element_list:
            element_title = element.findAll("div", class_="panel-title")
            element_gipfel = element_title[0].text.strip().split(' „')[0].strip()    
            if (element_gipfel != old_element_gipfel):
                summit_index += 10**9 # TODO: Exchange with summit_data.sbb_gipfel_ID
                route_index = 10
            old_element_gipfel = element_gipfel
            sub_element_list = element.findAll("div", {"class" : lambda L: L and L.startswith('col-')})
            sub_element_dict = {'_id': summit_index + route_index, 'Gipfel': element_gipfel, 'Wegname':'', 'Datum der Erstbegehung':'', 'Geführt von':'', 'Nachgestiegen von':'', \
                                    'Wegbeschreibung':'', 'Einsortierung im Kletterführer (nach welchem Weg?)':'keine Angabe', 'Variante von':'-', \
                                    'Gesamtschwierigkeit':'', 'Schwierigkeit a.f. bzw. m.U.':'-', 'Schwierigkeit o.U.':'-', 'Schwierigkeit RP':'-', 'Sprungschwierigkeit':'-',\
                                    'Sternchen & Ausrufezeichen':'-', 'Brüchig':'0', 'Anstrengend':'0', 'Erstbegehung im Rotpunkt':'0', \
                                    'offene Schadensmeldungen':'', 'offene Umstufungsvorschläge':''}
            route_index += 10
            for sub_element in sub_element_list:
                lines = sub_element.get_text().strip().splitlines()
                # lines = lines + [l for l in sub_element.get_text().splitlines() if l]
                while len(lines) < 2: 
                    lines.append('unbekannt')
                sub_element_dict[lines[0]] = str(lines[1])
            sub_element_dict['Gesamtschwierigkeit'] = getGesamtschwierigkeit(sub_element_dict=sub_element_dict)
            is_special = element.findAll("span" , class_="pull-right btn-group")
            if len(is_special) > 0 and len(is_special[0].text.strip()) > 0 and is_special[0].text.strip() == 'Projekt':
                project_wegname = 'Projekt: ' + (str( sub_element_dict["Wegname"]) if len(sub_element_dict["Wegname"]) > 0 else 'ohne Namen') \
                                                + str( '' if sub_element_dict['Bemerkungen der AGnW'] == '-' else '; Bemerkungen der AGnW: ' + sub_element_dict['Bemerkungen der AGnW'] ) \
                                                + '; Status: ' + sub_element_dict['Status']
                sub_element_dict['Wegname'] = project_wegname
                sub_element_dict['Datum der Erstbegehung'] = "Projekt aus dem Jahr " + sub_element_dict['Jahr']
                sub_element_dict['Geführt von'] = "Projektanmelder: " + sub_element_dict['Erstbegeher']
                sub_element_dict['Wegbeschreibung'] = "Geplanter Wegverlauf: " + sub_element_dict['Geplanter Wegverlauf']
                del sub_element_dict['Geplanter Wegverlauf']
                del sub_element_dict['Jahr']
                del sub_element_dict['Erstbegeher']
                del sub_element_dict['Bemerkungen der AGnW']
                del sub_element_dict['Status']
            elif len(is_special) > 0 and len(is_special[0].text.strip()) > 0 and is_special[0].text.strip() == 'Abgelehnte Erstbegehung':
                sub_element_dict["Wegname"] = 'Abgelehnte Erstbegehung: ' + sub_element_dict["Wegname"]
            elif len(is_special) > 0 and len(is_special[0].text.strip()) > 0 and 'Umstufungsvorschläge' in is_special[0].text.strip():
                umstufungsvorschlaege = soup.findAll("td")
                umstufungsvorschlaege_text = ''
                # Name
                if len(umstufungsvorschlaege[0]) != 0: umstufungsvorschlaege_text += 'Von: ' +  umstufungsvorschlaege[0].text
                # Datum
                if len(umstufungsvorschlaege[1]) != 0: umstufungsvorschlaege_text += '; am: ' +  umstufungsvorschlaege[1].text
                # a.f.
                if len(umstufungsvorschlaege[2]) != 0: umstufungsvorschlaege_text += '; a.f.: ' +  umstufungsvorschlaege[2].text
                # o.U.
                if len(umstufungsvorschlaege[3]) != 0: umstufungsvorschlaege_text += '; a.f.: ' +  umstufungsvorschlaege[3].text
                # RP
                if len(umstufungsvorschlaege[4]) != 0: umstufungsvorschlaege_text += '; rp: ' +  umstufungsvorschlaege[4].text
                #Sprung
                if len(umstufungsvorschlaege[5]) != 0: umstufungsvorschlaege_text += '; sprung: ' +  umstufungsvorschlaege[5].text
                # Präd.
                if len(umstufungsvorschlaege[6]) != 0: umstufungsvorschlaege_text += '; Präd.: ' +  umstufungsvorschlaege[6].text
                # anstr.
                if len(umstufungsvorschlaege[7]) != 0: umstufungsvorschlaege_text += '; anstr.: ' +  umstufungsvorschlaege[7].text
                # brüchig
                if len(umstufungsvorschlaege[8]) != 0: umstufungsvorschlaege_text += '; brüchig.: ' +  umstufungsvorschlaege[8].text
                sub_element_dict['offene Umstufungsvorschläge'] = 'offene Umstufungsvorschläge: ' + umstufungsvorschlaege_text
            if len(is_special) > 0 and len(is_special[0].text.strip()) > 0 and 'Schadensmeldungen' in is_special[0].text.strip():
                sub_element_dict['offene Schadensmeldungen'] = 'offene Schadensmeldungen: ' \
                        + '; Schadensart:' + sub_element_dict['Schadensart'] + '; Erstellungsdatum: ' + sub_element_dict['Erstellungsdatum'] \
                        + '; Beschreibung: ' + sub_element_dict['Beschreibung'] + '; Status: ' + sub_element_dict['Status'] 
                del sub_element_dict['Schadensart']
                del sub_element_dict['Erstellungsdatum']
                del sub_element_dict['Beschreibung']
                del sub_element_dict['Status']
                if 'Kommentar der klettertechnischen Abteilung' in sub_element_dict: 
                    sub_element_dict['offene Schadensmeldungen'] = sub_element_dict['offene Schadensmeldungen'] \
                        + '; Kommentar der klettertechnischen Abteilung: ' + sub_element_dict['Kommentar der klettertechnischen Abteilung']
                    del sub_element_dict['Kommentar der klettertechnischen Abteilung']
                while (len(sub_element_dict) > 19):
                    print(sub_element_dict.popitem())
            sub_element_dict.update(get_data_Variante_von(sub_element_dict['Variante von']))
            sub_element_dict.update(get_data_EinsortierungNach(sub_element_dict['Einsortierung im Kletterführer (nach welchem Weg?)']))
            df_dictionary = pd.DataFrame([sub_element_dict], dtype='string')
            wege = pd.concat([wege, clean_dict(df_dictionary).astype(wege.dtypes)], ignore_index=True)
        #print(wege)
        wege.to_sql("data", db, if_exists="append", index=False)