import sqlite3
from bottle import route, get, put, post, run, redirect, debug, template, request, static_file, error


from pathlib import Path
from bottle import TEMPLATE_PATH
from constants import *
import os
dirname = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(dirname, 'views')
STATIC_DIR = os.path.join(dirname, 'static')
DATABASE_FILE = os.path.join(dirname, '..', 'all_together_data.sqlite')

TEMPLATE_PATH.append(TEMPLATE_DIR)
aSummit = ''

@get('/summit')
def submit():
    # grab data from form
    cutoffCoerr = request.query['cutoffCoerr']
    filter_summit = summit_no_to_string(request.query['filter_summit'])
    if filter_summit == '':
        filter_summit = aSummit
    print('Hello World! ' + cutoffCoerr + '; ' + filter_summit)
    # return template("bottlepy_Formtest_html.tpl") #rebase from layout.tpl
    return redirect('/summit/' + filter_summit + ">" + cutoffCoerr)

@route('/summit/<filepath:re:.*\\.css>')
@route('/summit/<filepath:re:.*\\.js>')
def server_static(filepath):
    print(static_file(filepath, root=STATIC_DIR))
    return static_file(filepath, root=STATIC_DIR)

@route('/summit/<summit_coeff>')
def summit(summit_coeff):
    summit_and_coeff = summit_coeff.split('>')
    aSummit = summit_and_coeff[0]
    if len(summit_and_coeff) == 2:
        aCorrCoeffLimit = summit_and_coeff[1].replace('>','')
        try:
            aCorrCoeffLimit = str(int(aCorrCoeffLimit))
        except (TypeError, ValueError):
            aCorrCoeffLimit = '70.0'
    else:
        aCorrCoeffLimit = '70.0'
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
 SELECT   sbb._id AS sbb_id,
           sbb.sbb_gipfel || ' - ' || sbb.sbb_Gebiet || ' #' || CAST(sbb.sbb_gipfel_ID AS INTEGER) AS sbb_gipfel,
           sbb.Wegname AS [sbb_Wegname], 
           sbb.[Gesamtschwierigkeit] AS sbb_Schwierigkeit, 
           CASE
               WHEN sbb.[Geführt von] || sbb.[Nachgestiegen von] IS '' THEN null
               ELSE sbb.[Geführt von] || '/' || sbb.[Nachgestiegen von]
           END sbb_erstbegeher,
           sbb.Wegbeschreibung AS sbb_Wegbeschreibung,
           sbb.[Einsortierung im Kletterführer (nach welchem Weg?)], 
           sbb.VarianteVon_Wegname, 
             
           CAST(linkss.Corr_Coeff AS FLOAT) AS [Corr. Coeff. sbb-ss],
           
           ss.weg_ID AS ss_id,           
           ss.gipfelname_d || ' - ' || ss.sektorname_d || ' #' || CAST(ss.gipfelid AS INTEGER) AS ss_gipfel,
           ss.WegName_d AS [ss_wegname],
           ss.schwierigkeit AS ss_Schwierigkeit, 
           CASE
               WHEN ss.[erstbegvorstieg] || ss.[erstbegnachstieg] IS '' THEN null
               ELSE ss.[erstbegvorstieg] || '/' || ss.[erstbegnachstieg]
           END ss_erstbegeher,
           ss.wegbeschr_d AS ss_Wegbeschreibung,           
           
           CAST(linktt.Corr_Coeff AS FLOAT) AS [Corr. Coeff. sbb-tt],
           
           tt.intTTWegNr AS tt_id, 
           tt.strName || ' - ' || tt.strGebiet || ' #' || CAST(tt.intTTGipfelNr AS INTEGER) AS tt_gipfel,
           tt.WegName AS [tt_wegname],
           tt.strSchwierigkeitsGrad AS tt_Schwierigkeit,
           NULL AS tt_erstbegeher, --- tt_erstbegeher,
           NULL AS tt_Wegbeschreibung --- tt_Wegbeschreibung
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ssk WHERE Corr_Coeff >= "''' + aCorrCoeffLimit + '''") AS linkss  ON sbb._id = linkss.sbb_id
        FULL OUTER JOIN  (SELECT * FROM link_sbb2tt WHERE Corr_Coeff >= "''' + aCorrCoeffLimit + '''") AS linktt  ON sbb._id = linktt.sbb_id
        FULL OUTER JOIN  route_data_ssk ss ON ss.weg_ID = linkss.ss_id 
        FULL OUTER JOIN  route_data_TT tt ON tt.intTTWegNr = linktt.tt_id         
        WHERE sbb.sbb_gipfel = "''' + aSummit + '''" COLLATE NOCASE
    UNION
      SELECT NULL AS sbb_id,
             NULL AS sbb_gipfel,
             NULL AS [sbb_Wegname], 
             NULL AS sbb_Schwierigkeit, 
             NULL sbb_erstbegeher,
             NULL AS sbb_Wegbeschreibung,
             NULL AS [Einsortierung im Kletterführer (nach welchem Weg?)], 
             NULL AS [VarianteVon_Wegname], 
             
             'NONE' AS [Corr. Coeff. sbb-ss],
      
             ss.weg_ID AS ss_id,           
             ss.gipfelname_d || ' - ' || ss.sektorname_d || ' #' || CAST(ss.gipfelid AS INTEGER) AS ss_gipfel,
             ss.WegName_d AS [ss_wegname],
             ss.schwierigkeit AS ss_Schwierigkeit, 
             CASE
                 WHEN ss.[erstbegvorstieg] || ss.[erstbegnachstieg] IS '' THEN null
                 ELSE ss.[erstbegvorstieg] || '/' || ss.[erstbegnachstieg]
             END ss_erstbegeher,
             ss.wegbeschr_d AS ss_Wegbeschreibung,   
      
             'NONE' AS [Corr. Coeff. sbb-tt],
             
             NULL AS tt_id, 
             NULL AS tt_gipfel,
             NULL AS [tt_wegname],
             NULL AS tt_Schwierigkeit,
             NULL AS tt_erstbegeher, 
             NULL AS tt_Wegbeschreibung 
      FROM route_data_ssk ss  
      WHERE ss.gipfelname_d = "''' + aSummit + '''"
      AND ss.weg_ID NOT IN (SELECT DISTINCT(ss.weg_ID)
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ssk WHERE Corr_Coeff >= "''' + aCorrCoeffLimit + '''") AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN  route_data_ssk ss ON ss.weg_ID = link.ss_id 
        WHERE sbb.sbb_gipfel = "''' + aSummit + '''" COLLATE NOCASE AND ss.weg_ID NOT NULL
        ORDER BY sbb._id 
        )
    UNION
      SELECT NULL AS sbb_id,
             NULL AS sbb_gipfel,
             NULL AS [sbb_Wegname], 
             NULL AS sbb_Schwierigkeit, 
             NULL sbb_erstbegeher,
             NULL AS sbb_Wegbeschreibung,
             NULL AS [Einsortierung im Kletterführer (nach welchem Weg?)], 
             NULL AS [VarianteVon_Wegname], 
             
             NULL AS [Corr. Coeff. sbb-ss],
      
             NULL AS ss_id,           
             NULL AS ss_gipfel,
             NULL AS ss_wegname,
             NULL AS ss_Schwierigkeit, 
             NULL AS ss_erstbegeher,
             NULL AS ss_Wegbeschreibung,   
      
             NULL AS [Corr. Coeff. sbb-tt],
             

             tt.intTTWegNr AS tt_id, 
             tt.strName || ' - ' || tt.strGebiet || ' #' || CAST(tt.intTTGipfelNr AS INTEGER) AS tt_gipfel,
             tt.WegName AS [tt_wegname],
             tt.strSchwierigkeitsGrad AS tt_Schwierigkeit,
             NULL AS tt_erstbegeher, --- tt_erstbegeher,
             NULL AS tt_Wegbeschreibung --- tt_Wegbeschreibung
      FROM route_data_TT tt  
      WHERE tt.strName = "''' + aSummit + '''"
      AND tt.intTTWegNr NOT IN (SELECT DISTINCT(tt.intTTWegNr)
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2tt WHERE Corr_Coeff >= "''' + aCorrCoeffLimit + '''") AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN route_data_TT tt ON tt.intTTWegNr = link.tt_id 
        WHERE sbb.sbb_gipfel = "''' + aSummit + '''" COLLATE NOCASE AND tt.intTTWegNr NOT NULL
        ORDER BY tt.intTTWegNr
        )
      ORDER BY sbb._id NULLS LAST
  ;
            ''')
    result = c.fetchall()
    c.close()
    _summit_no = summit_name_to_summit_no(aSummit)
    print(_summit_no)
    output = template('make_route_table_3', rows=result, cutOff=aCorrCoeffLimit, summit_no=_summit_no)
    return output


@route('/help')
def help():

    static_file('help.html', root='.')


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

if __name__ == "__main__":
    run(host='127.0.0.1', port=5050, debug=True, reloader=True)
    # remember to remove reloader=True and debug(True) when you move your
    # application from development to a productive environment