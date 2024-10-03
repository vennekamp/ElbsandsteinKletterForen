import sqlite3
from summit_table_helper import get_files_dir
## Nur zum Testen 
gipfel = "Eremit"
corr_coeff = str(70.0)
save_dir = get_files_dir("")
db_all_together_data = sqlite3.connect(save_dir + "/all_together_data.sqlite")
db_all_together_data.execute(
    '''    
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
           tt.strName || ' - ' || tt.strGebiet || ' #' || CAST(tt.intTTWegNr AS INTEGER) AS tt_gipfel,
           tt.WegName AS [tt_wegname],
           tt.strSchwierigkeitsGrad AS tt_Schwierigkeit,
           NULL AS tt_erstbegeher, --- tt_erstbegeher,
           NULL AS tt_Wegbeschreibung --- tt_Wegbeschreibung
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ssk WHERE Corr_Coeff >= "''' + corr_coeff + '''") AS linkss  ON sbb._id = linkss.sbb_id
        FULL OUTER JOIN  (SELECT * FROM link_sbb2tt WHERE Corr_Coeff >= "''' + corr_coeff + '''") AS linktt  ON sbb._id = linktt.sbb_id
        FULL OUTER JOIN  route_data_ssk ss ON ss.weg_ID = linkss.ss_id 
        FULL OUTER JOIN  route_data_tt tt ON tt.intTTWegNr = linktt.tt_id         
        WHERE sbb.sbb_gipfel = "''' + gipfel + '''" COLLATE NOCASE
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
      WHERE ss.gipfelname_d = "''' + gipfel + '''"
      AND ss.weg_ID NOT IN (SELECT DISTINCT(ss.weg_ID)
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2ssk WHERE Corr_Coeff >= "''' + corr_coeff + '''") AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN  route_data_ssk ss ON ss.weg_ID = link.ss_id 
        WHERE sbb.sbb_gipfel = "''' + gipfel + '''" COLLATE NOCASE AND ss.weg_ID NOT NULL
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
             NULL AS [ss_wegname],
             NULL AS ss_Schwierigkeit, 
             NULL AS ss_erstbegeher,
             NULL AS ss_Wegbeschreibung,   
      
             NULL AS [Corr. Coeff. sbb-tt],
             

             tt.intTTWegNr AS tt_id, 
             tt.strName || ' - ' || tt.strGebiet || ' #' || CAST(tt.intTTWegNr AS INTEGER) AS tt_gipfel,
             tt.WegName AS [tt_wegname],
             tt.strSchwierigkeitsGrad AS tt_Schwierigkeit,
             NULL AS tt_erstbegeher, --- tt_erstbegeher,
             NULL AS tt_Wegbeschreibung --- tt_Wegbeschreibung
      FROM route_data_tt tt  
      WHERE tt.strName = "''' + gipfel + '''"
      AND tt.intTTWegNr NOT IN (SELECT DISTINCT(tt.intTTWegNr)
        FROM route_data_sbb sbb
        FULL OUTER JOIN  (SELECT * FROM link_sbb2tt WHERE Corr_Coeff >= "''' + corr_coeff + '''") AS link  ON sbb._id = link.sbb_id
        FULL OUTER JOIN route_data_tt tt ON tt.intTTWegNr = link.tt_id 
        WHERE sbb.sbb_gipfel = "''' + gipfel + '''" COLLATE NOCASE AND tt.intTTWegNr NOT NULL
        ORDER BY tt.intTTWegNr
        )
      ORDER BY sbb._id NULLS LAST
  ;
    '''
)
rows_correlated_routes = [[ idx, routes] for  idx, routes in enumerate(db_all_together_data.fetchall())]
db_all_together_data.close()
print(rows_correlated_routes)