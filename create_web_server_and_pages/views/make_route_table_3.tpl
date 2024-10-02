%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js" charset="utf-8"></script>
    <link rel="stylesheet" type="text/css" href="make_route_table.css" charset="utf-8">
</head>
<body>
<div style="position: sticky; top: 0px; z-index: 1;">
	<table border="1" id="container-table">
	<thead>
		<tr>
			<th>SBB-Database</th>
			<th>Corr. Coeff.</th>
			<th>Sandsteinklettern</th>
			<th>Corr. Coeff.</th>
			<th>Teufelsturm</th>
		</tr>
	</thead>
			<tbody></tbody>
	</table>
</div>
<div style="position:relative;">
<div style="width: 33%; float: left;">
		<form method="PUT" action="/summit">
		<button id="addRow" type="button" class="button">Create a new empty Row</button>
		<button id="removeRow" type="button" class="button">Remove an empty Row</button>
        <input type="submit" value="Neu laden..!" class="submit"/>
				<select id="filter_summit" name="filter_summit">
					<option value="">Bitte Gipfel wählen</option>
					<optgroup label="Bielatal">
						<option value="126">Brausenstein (1)</option>
						<option value="127">Topograph (2)</option>
						<option value="128">Gnom (3)</option>
						<option value="129">Waldkapelle (4)</option>
						<option value="131">Vorderer Bielaturm (5)</option>
						<option value="132">Hinterer Bielaturm (6)</option>
						<option value="133">Schweizermühlenturm (7)</option>
						<option value="134">Kapuziner (8)</option>
						<option value="135">Zerklüftete Wand (9)</option>
						<option value="136">Pumpenwärter (10)</option>
						<option value="137">Herkuleskopf (11)</option>
						<option value="138">Schluchtnadel (12)</option>
						<option value="140">Herkuleswand (13)</option>
						<option value="141">Kleiner Herkulesstein (14)</option>
						<option value="142">Herkulesstein (15)</option>
						<option value="143">Herkulessohn (16)</option>
						<option value="144">Kleine Herkulessäule (17)</option>
						<option value="145">Große Herkulessäule (18)</option>
						<option value="146">Vorderer Schroffer Stein (19)</option>
						<option value="147">Hinterer Schroffer Stein (20)</option>
						<option value="148">Schraubenkopf (21)</option>
						<option value="149">Wegelagerer (22)</option>
						<option value="150">Leichte Zacke (23)</option>
						<option value="151">Schwere Zacke (24)</option>
						<option value="152">Schiefe Zacke (25)</option>
						<option value="153">Schiefer Turm (26)</option>
						<option value="154">Hallenkopf (27)</option>
						<option value="155">Hallenstein (28)</option>
						<option value="156">Sonnenwendstein (29)</option>
						<option value="1360">Sonny (30)</option>
						<option value="157">Chinesischer Turm (31)</option>
						<option value="158">Mandarin (32)</option>
						<option value="159">Bewachsener Fels (33)</option>
						<option value="160">Trautmannsfels (34)</option>
						<option value="161">Nasser Stein (35)</option>
						<option value="163">Glück-Auf-Turm (36)</option>
						<option value="164">Raupe (37)</option>
						<option value="165">Puppe (38)</option>
						<option value="166">Kanzelturm (39)</option>
						<option value="168">Schildkrötenturm (40)</option>
						<option value="171">Gesuchter Turm (41)</option>
						<option value="169">Kuchenturm (42)</option>
						<option value="172">Ringelturm (43)</option>
						<option value="173">Zarathustra Junior (44)</option>
						<option value="174">Zarathustra (45)</option>
						<option value="175">Daxkopf (46)</option>
						<option value="176">Daxenstein (47)</option>
						<option value="177">Ottostein (48)</option>
						<option value="178">Großer Mühlenwächter (49)</option>
						<option value="179">Kleiner Mühlenwächter (50)</option>
						<option value="180">Rosenthaler Turm (51)</option>
						<option value="181">Großvaterstuhl (52)</option>
						<option value="1479">Waldhorn (53)</option>
						<option value="183">Stumpfer Turm (54)</option>
						<option value="184">Stumpfe Keule (55)</option>
						<option value="187">Stumpfer Kegel (56)</option>
						<option value="188">Prometheus (57)</option>
						<option value="189">Fledermausturm (58)</option>
						<option value="190">Siebenschläferturm (59)</option>
						<option value="191">Siebenschläferkeule (60)</option>
						<option value="192">Waldschratt (61)</option>
						<option value="193">Felix (62)</option>
						<option value="194">Felicitas (63)</option>
						<option value="195">Spannagelturm (64)</option>
						<option value="196">Rabenturm (65)</option>
						<option value="198">Kleiner Eislochturm (66)</option>
						<option value="199">Großer Eislochturm (67)</option>
						<option value="201">Papusspitze (68)</option>
						<option value="202">Troika (69)</option>
						<option value="203">Waldscheibe (70)</option>
						<option value="1481">Sonnenturm (71)</option>
						<option value="204">Turm am Wege (72)</option>
						<option value="205">Unke (73)</option>
						<option value="206">Pfingstturm (74)</option>
						<option value="1482">Morgenstern (75)</option>
						<option value="207">Jupiterturm (76)</option>
						<option value="208">Fichtenkegel (77)</option>
						<option value="209">Bonze (78)</option>
						<option value="210">Bonzenzahn (79)</option>
						<option value="211">Verlassene Wand (80)</option>
						<option value="212">Felsensportnadel (81)</option>
						<option value="213">Wolfskopf (82)</option>
						<option value="214">Versteckte Wand (83)</option>
						<option value="215">Verlassene Spitze (84)</option>
						<option value="216">Birkenturm (85)</option>
						<option value="217">Großer Glücksturm (86)</option>
						<option value="218">Kleiner Glücksturm (87)</option>
						<option value="219">Würfel (88)</option>
						<option value="220">Hilfssheriff (89)</option>
						<option value="221">Sheriff (90)</option>
						<option value="222">Vergessene Spitze (91)</option>
						<option value="223">Sultan (92)</option>
						<option value="224">Morscher Kopf (93)</option>
						<option value="225">Kalif (94)</option>
						<option value="226">Scheitan (95)</option>
						<option value="227">Zwerg Alberich (96)</option>
						<option value="228">Stiller Kegel (97)</option>
						<option value="229">Bielazwerg (98)</option>
						<option value="230">Gnomkönig (99)</option>
						<option value="231">Troll (100)</option>
						<option value="232">Dürrebielezahn (101)</option>
						<option value="233">Vorderer Dürrebielewächter (102)</option>
						<option value="234">Bewachsene Spitze (103)</option>
						<option value="235">Falkenturm (104)</option>
						<option value="237">Falkenwand (105)</option>
						<option value="238">Hinterer Dürrebielewächter (106)</option>
						<option value="239">Kiebitz (107)</option>
						<option value="240">Nymphe (108)</option>
						<option value="241">Gespaltener Turm (109)</option>
						<option value="242">Glatter Kegel (110)</option>
						<option value="243">Pfifferling (111)</option>
						<option value="244">Stinkmorchel (112)</option>
						<option value="245">Waldkauz (113)</option>
						<option value="246">Zwei Horzel (114)</option>
						<option value="247">Schildbürger (115)</option>
						<option value="248">Blatt (116)</option>
						<option value="249">Planspitze (117)</option>
						<option value="250">Pokal (118)</option>
						<option value="251">Mittelwandnadel (119)</option>
						<option value="252">Mittelwand (120)</option>
						<option value="253">Mittelwandscheibe (121)</option>
						<option value="254">Schiefe Nadel (122)</option>
						<option value="255">Schwarzbeerturm (123)</option>
						<option value="125">Setzling (124)</option>
						<option value="256">Nussknacker (125)</option>
						<option value="257">Dürrebielenadel (126)</option>
						<option value="258">Dürrebielewand (127)</option>
						<option value="259">Ringelspitze (128)</option>
						<option value="260">Elisabethspitze (129)</option>
						<option value="261">Falkenspitze (130)</option>
						<option value="262">Fraktur (131)</option>
						<option value="263">Schwarze Wand (132)</option>
						<option value="264">Sommerstein (133)</option>
						<option value="265">Dürrebieleturm (134)</option>
						<option value="266">Ameisenstein (135)</option>
						<option value="267">Gralsburg, NO-Zinne (136)</option>
						<option value="268">Gralsburg, SW-Zinne (137)</option>
						<option value="269">Waldtorturm (138)</option>
						<option value="270">Nördliche Waldtornadel (139)</option>
						<option value="271">Turm der Felsenbrüder (140)</option>
						<option value="272">Südliche Waldtornadel (141)</option>
						<option value="273">Hansenstein (142)</option>
						<option value="274">Akropolis (143)</option>
						<option value="275">Archimedes (144)</option>
						<option value="276">Praxedis (145)</option>
						<option value="277">Euklid (146)</option>
						<option value="279">Sokrates (147)</option>
						<option value="278">Perikles (148)</option>
						<option value="280">Xerxes (149)</option>
						<option value="281">Grenzwegwächter (150)</option>
						<option value="284">Waldpfeiler (151)</option>
						<option value="285">Kleiner Grenzturm (152)</option>
						<option value="286">Grenzkegel (153)</option>
						<option value="287">Grenznadel (154)</option>
						<option value="288">Großer Grenzturm (155)</option>
						<option value="289">Einsame Nadel (156)</option>
						<option value="292">Titan (157)</option>
						<option value="294">Goliath (158)</option>
						<option value="1480">David (159)</option>
						<option value="295">Cima (160)</option>
						<option value="296">Castello (161)</option>
						<option value="297">Burgenerturm (162)</option>
						<option value="298">Adam und Eva (163)</option>
						<option value="299">Falkennadel (164)</option>
						<option value="300">Adlerkopf (165)</option>
						<option value="301">Wachsamer Förster (166)</option>
						<option value="302">Kastenturm (167)</option>
						<option value="303">Waldkegel (168)</option>
						<option value="304">Liebespaar, Südturm (169)</option>
						<option value="305">Liebespaar, Nordturm (170)</option>
						<option value="1347">Liebesknochen (171)</option>
						<option value="306">Schneespitze (172)</option>
						<option value="307">Schneewand (173)</option>
						<option value="308">Bielascheibe (174)</option>
						<option value="309">Waldnadel (175)</option>
						<option value="310">Osterkegel (176)</option>
						<option value="311">Bielazinne (177)</option>
						<option value="312">Herbstturm (178)</option>
						<option value="313">Grüne Zinne (179)</option>
						<option value="314">Herbstspitze (180)</option>
						<option value="315">Grauer Turm (181)</option>
						<option value="317">Waldturm (182)</option>
						<option value="318">Juliturm (183)</option>
						<option value="326">Schwarzmühlenspitze (184)</option>
						<option value="327">Schwarzmühlenwächter (185)</option>
						<option value="328">Kubulus (186)</option>
						<option value="329">Arnsteiner Turm (187)</option>
						<option value="330">Harmonienadel (188)</option>
						<option value="331">Rumpelstilz (189)</option>
						<option value="332">Harmoniekopf (190)</option>
						<option value="333">Kleine Zinne (191)</option>
						<option value="334">Große Zinne (192)</option>
						<option value="335">Südwestliche Zinne (193)</option>
						<option value="336">Pagode (194)</option>
						<option value="337">Mäuseturm (195)</option>
						<option value="338">Glasergrundwand (196)</option>
						<option value="339">Glasergrundwarte (197)</option>
						<option value="340">Glatte Keule (198)</option>
						<option value="341">Krallenturm (199)</option>
						<option value="342">Glasergrundnadel (200)</option>
						<option value="343">Wilde Zacke (201)</option>
						<option value="344">Lochsteinwächter (202)</option>
						<option value="345">Lochstein (203)</option>
						<option value="346">Unbenannter Turm (204)</option>
						<option value="347">Glasergrundwächter (205)</option>
						<option value="348">Adlerstein (206)</option>
						<option value="349">Himmelfahrtsturm (207)</option>
						<option value="350">Bär (208)</option>
						<option value="351">Wigwam (209)</option>
						<option value="352">Wormsbergwächter (210)</option>
						<option value="353">Glasergrundspitze (211)</option>
						<option value="354">Schaftwaldturm (212)</option>
						<option value="355">Nadel im Abseits (213)</option>
						<option value="356">Horzelbub (214)</option>
						<option value="357">Lausbub (215)</option>
						<option value="358">Semperhexe (216)</option>
						<option value="1344">Bergstation (217)</option>
						<option value="359">Schöne Nadel (218)</option>
						<option value="360">Glasergrundscheibe (219)</option>
						<option value="361">Totenkopf (220)</option>
						<option value="362">Waldwächter (221)</option>
						<option value="363">Uhustein (222)</option>
						<option value="364">Waldzahn (223)</option>
						<option value="365">Südlicher Wiesenstein (224)</option>
						<option value="366">Mittlerer Wiesenstein (225)</option>
						<option value="367">Wiesenturm (226)</option>
						<option value="368">Hauptwiesenstein (227)</option>
						<option value="369">Nördlicher Wiesenstein (228)</option>
						<option value="371">Hinterer Wiesenstein (229)</option>
						<option value="374">Wiesenkopf (230)</option>
						<option value="375">Zauberberg (231)</option>
						<option value="376">Pötzschturm (232)</option>
						<option value="377">Johanniskegel (233)</option>
						<option value="378">Johannisturm (234)</option>
						<option value="379">Friederike (235)</option>
						<option value="380">Fritziturm (236)</option>
						<option value="381">Mauerblümchen (237)</option>
						<option value="382">Johannismauer (238)</option>
						<option value="383">Johanniskopf (239)</option>
						<option value="384">Morsche Wand (240)</option>
						<option value="385">Artariastein (241)</option>
						<option value="386">Schusterturm (242)</option>
						<option value="387">Bielawächter (243)</option>
						<option value="388">Sachsenspitze (244)</option>
						<option value="389">Baumschulenturm (245)</option>
						<option value="390">Baumschulenwächter (246)</option>
						<option value="391">Baumschulenwarte (247)</option>
						<option value="392">Doggenturm (248)</option>
						<option value="393">Backfisch (249)</option>
					</optgroup>
					<optgroup label="Erzgebirgsgrenzgebiet">
						<option value="395">Dieb (1)</option>
						<option value="397">Pascher (2)</option>
						<option value="398">Grenzwächter (3)</option>
						<option value="400">Grenzspitze (4)</option>
						<option value="401">Hellendorfer Nadel (5)</option>
						<option value="402">Mordspitze (6)</option>
						<option value="404">Bahratalwand (7)</option>
						<option value="406">Spitzbub (8)</option>
						<option value="407">Vierkant (9)</option>
						<option value="408">Gendarm (10)</option>
						<option value="409">Kuckuckstein (11)</option>
						<option value="412">Östlicher Berggießhübler Turm (12)</option>
						<option value="413">Westlicher Berggießhübler Turm (13)</option>
						<option value="1478">Felsenbrückenturm (14)</option>
						<option value="414">Giesensteinwand (15)</option>
						<option value="416">Brandstein (16)</option>
					</optgroup>
					<optgroup label="Wehlener Gebiet">
						<option value="1157">Buch (1)</option>
						<option value="1158">Postakegel (2)</option>
						<option value="1162">Buschholzturm (3)</option>
						<option value="1163">Bergfalkenturm (4)</option>
						<option value="1164">Einsamer Turm (5)</option>
						<option value="1165">Kehllochscheibe (6)</option>
						<option value="1166">Versteckte Spitze (7)</option>
						<option value="1167">Steinerner Bär (8)</option>
						<option value="1168">Höllengrundscheibe (9)</option>
						<option value="1169">Zwölfer (10)</option>
						<option value="1170">Tümpelgrundturm (11)</option>
						<option value="1171">Tümpelgrundwächter (12)</option>
						<option value="1172">Gelbe Wand (13)</option>
						<option value="1173">Tümpelgrundwand (14)</option>
						<option value="1174">Erikascheibe (15)</option>
						<option value="1175">Wetterwarte (16)</option>
						<option value="1176">Elbgucke (17)</option>
						<option value="1177">Griesgrundwächter (18)</option>
					</optgroup>
					<optgroup label="Rathener Gebiet">
						<option value="656">Kraxelbrüderscheibe (1)</option>
						<option value="657">Querkopf (2)</option>
						<option value="658">Hirschgrundscheibe (3)</option>
						<option value="659">Doktor (4)</option>
						<option value="660">Patient (5)</option>
						<option value="661">Assistent (6)</option>
						<option value="662">Hinterer Hirschgrundturm (7)</option>
						<option value="663">Wilddieb (8)</option>
						<option value="664">Mittlerer Hirschgrundturm (9)</option>
						<option value="665">Vorderer Hirschgrundturm (10)</option>
						<option value="666">Hirschgrundkegel (11)</option>
						<option value="667">Scherge (12)</option>
						<option value="668">Lochturm (13)</option>
						<option value="669">Hirschgrundwarte (14)</option>
						<option value="670">Adolf-Hermann-Fels (15)</option>
						<option value="671">Wartturm (16)</option>
						<option value="672">Torsteiner Turm (17)</option>
						<option value="673">Margaretenspitze (18)</option>
						<option value="674">Musketier (19)</option>
						<option value="675">Bergpirat (20)</option>
						<option value="676">Basteiturm (21)</option>
						<option value="677">Sieberturm (22)</option>
						<option value="678">Jahrhundertturm (23)</option>
						<option value="679">Steinschleuder (24)</option>
						<option value="680">Neurathener Felsentor (25)</option>
						<option value="681">Tiedgestein (26)</option>
						<option value="682">Mönch (27)</option>
						<option value="683">Biene (28)</option>
						<option value="684">Verlorener Turm (29)</option>
						<option value="685">Reh (30)</option>
						<option value="686">Langer Israel (31)</option>
						<option value="687">Rudolf-Holtz-Turm (32)</option>
						<option value="688">Basteischluchtturm (33)</option>
						<option value="689">Wehlkopf (34)</option>
						<option value="690">Kleiner Wehlturm (35)</option>
						<option value="691">Mittlerer Wehlturm (36)</option>
						<option value="692">Grosser Wehlturm (37)</option>
						<option value="693">Taufstein (38)</option>
						<option value="694">Pate (39)</option>
						<option value="695">Ferdinandturm (40)</option>
						<option value="696">Schwarze Säule (41)</option>
						<option value="697">Aschelochturm (42)</option>
						<option value="700">Zugvogelspitze (43)</option>
						<option value="701">Felsensportturm (44)</option>
						<option value="698">Felsensternscheibe (45)</option>
						<option value="702">Basteiwächter (46)</option>
						<option value="703">Wehlhorn (47)</option>
						<option value="704">Höhlenturm (48)</option>
						<option value="705">Doppelkopf (49)</option>
						<option value="706">Wehlkegel (50)</option>
						<option value="707">Hinterer Basteiturm (51)</option>
						<option value="708">Schneider Wibbel (52)</option>
						<option value="709">Zitronenkopf (53)</option>
						<option value="710">Witzbold (54)</option>
						<option value="711">Wehlscheibe (55)</option>
						<option value="712">Wehlgrundspitze (56)</option>
						<option value="713">Wehlgrundwächter (57)</option>
						<option value="714">Grafenspitze (58)</option>
						<option value="715">Grenadierturm (59)</option>
						<option value="716">Wassermann (60)</option>
						<option value="717">Bierturm (61)</option>
						<option value="718">Axelturm (62)</option>
						<option value="719">Pavillonwächter (63)</option>
						<option value="720">Kanzelscheibe (64)</option>
						<option value="722">Echse (65)</option>
						<option value="723">Habicht (66)</option>
						<option value="724">Statist (67)</option>
						<option value="725">Schalk (68)</option>
						<option value="726">Bergfreund (69)</option>
						<option value="727">Wehlnadel (70)</option>
						<option value="728">Bergfreundeturm (71)</option>
						<option value="729">Souffleur (72)</option>
						<option value="730">Gänseei (73)</option>
						<option value="731">Plattenstein (74)</option>
						<option value="732">Hinterer Gansfels (75)</option>
						<option value="733">Mittlerer Gansfels (76)</option>
						<option value="734">Vorderer Gansfels (77)</option>
						<option value="735">Ganskopf (78)</option>
						<option value="736">Gansriff (79)</option>
						<option value="737">Gansscheibe (80)</option>
						<option value="738">Gansturm (81)</option>
						<option value="739">Suleika (82)</option>
						<option value="740">Emir (83)</option>
						<option value="741">Raaber Turm (84)</option>
						<option value="742">Scheich (85)</option>
						<option value="743">Trockener Turm (86)</option>
						<option value="744">Raaber Säule (87)</option>
						<option value="745">Raaber Scheibe (88)</option>
						<option value="746">Raaber Kegel (89)</option>
						<option value="747">Kulisse (90)</option>
						<option value="748">Raaber Wand (91)</option>
						<option value="749">Raaber Nadel (92)</option>
						<option value="750">Eule (93)</option>
						<option value="751">Höllenhundscheibe (94)</option>
						<option value="752">Höllenhund (95)</option>
						<option value="753">Hinterer Höllenhundturm (96)</option>
						<option value="754">Mittlerer Höllenhundturm (97)</option>
						<option value="755">Vorderer Höllenhundturm (98)</option>
						<option value="756">Sechserturm (99)</option>
						<option value="757">Höllenhundwächter (100)</option>
						<option value="758">Maitürmchen (101)</option>
						<option value="759">Mücke (102)</option>
						<option value="760">Krümel (103)</option>
						<option value="761">Struppi (104)</option>
						<option value="762">Große-Gans-Wächter (105)</option>
						<option value="763">Flax (106)</option>
						<option value="764">Westlicher Turm der Jugend (107)</option>
						<option value="765">Östlicher Turm der Jugend (108)</option>
						<option value="766">Luginsland (109)</option>
						<option value="767">Dresdner Turm (110)</option>
						<option value="768">Rathener Warte (111)</option>
						<option value="769">Maxl (112)</option>
						<option value="770">Amselspitze (113)</option>
						<option value="771">Vexiernadel (114)</option>
						<option value="772">Vexierturm (115)</option>
						<option value="773">Amselgrundnadel (116)</option>
						<option value="774">Admiral (117)</option>
						<option value="775">Klabautermann (118)</option>
						<option value="776">Totenkirchl (119)</option>
						<option value="777">Amselgrundturm (120)</option>
						<option value="778">Schwedenscheibe (121)</option>
						<option value="779">Schwedenturm (122)</option>
						<option value="780">Storchnest (123)</option>
						<option value="781">Bienenkorb (124)</option>
						<option value="782">Lokomotive-Dom (125)</option>
						<option value="783">Lokomotive-Esse (126)</option>
						<option value="784">Lamm (127)</option>
						<option value="785">Lammscheibe (128)</option>
						<option value="786">Honigsteinnadel (129)</option>
						<option value="787">Honigsteinturm (130)</option>
						<option value="788">Honigstein (131)</option>
						<option value="789">Imker (132)</option>
						<option value="790">Maiturm (133)</option>
						<option value="791">Honigsteinscheibe (134)</option>
						<option value="792">Honigsteinkopf (135)</option>
						<option value="793">Lithostein (136)</option>
						<option value="794">Talwächter (137)</option>
						<option value="795">Westlicher Feldkopf (138)</option>
						<option value="796">Östlicher Feldkopf (139)</option>
						<option value="797">Türkenkopf (140)</option>
						<option value="798">Feldwand (141)</option>
						<option value="799">Gamrigwächter (142)</option>
						<option value="800">Heidestein (143)</option>
						<option value="801">Gamrigkegel (144)</option>
						<option value="802">Gamrigscheibe (145)</option>
						<option value="803">Waltersdorfer Horn (146)</option>
						<option value="804">Heidebrüderturm (147)</option>
						<option value="805">Ziegenrückenturm (148)</option>
					</optgroup>
					<optgroup label="Schrammsteine">
						<option value="945">Hüttenwart (1)</option>
						<option value="946">Zahnsgrundwächter (2)</option>
						<option value="947">Götze (3)</option>
						<option value="948">Zahnsgrundturm (4)</option>
						<option value="949">Schießgrundscheibe (5)</option>
						<option value="950">Hirschzahn (6)</option>
						<option value="952">Rübezahl (7)</option>
						<option value="951">Rübezahlkeule (8)</option>
						<option value="953">Steinschluchtwand (9)</option>
						<option value="955">Obrigenwand (10)</option>
						<option value="957">Vorderer Torstein (11)</option>
						<option value="958">Meurerturm (12)</option>
						<option value="959">Kesselturm (13)</option>
						<option value="960">Kelch (14)</option>
						<option value="961">Flasche (15)</option>
						<option value="962">Bierdeckel (16)</option>
						<option value="963">Viererturm (17)</option>
						<option value="964">Spitzer Turm (18)</option>
						<option value="965">Unbenannte Spitze (19)</option>
						<option value="966">Max und Moritz (20)</option>
						<option value="967">Zackenkrone (21)</option>
						<option value="968">Schrammtorwächter (22)</option>
						<option value="969">Schrammtorfreund (23)</option>
						<option value="970">Ostervorturm (24)</option>
						<option value="971">Südlicher Osterturm (25)</option>
						<option value="972">Nördlicher Osterturm (26)</option>
						<option value="973">Fotografenspitze (27)</option>
						<option value="974">Südlicher Schrammturm (28)</option>
						<option value="975">Westlicher Schrammturm (29)</option>
						<option value="976">Östlicher Schrammturm (30)</option>
						<option value="977">Nördlicher Schrammturm (31)</option>
						<option value="978">Dreifingerturm (32)</option>
						<option value="979">Jubiläumsturm (33)</option>
						<option value="980">Torsteinscheibe (34)</option>
						<option value="981">Schrammsteinnadel (35)</option>
						<option value="982">Schrammsteinkegel (36)</option>
						<option value="983">Golem (37)</option>
						<option value="984">Schrammsteinscheibe (38)</option>
						<option value="985">Nichte (39)</option>
						<option value="986">Schrammsteinwächter (40)</option>
						<option value="987">Neffe (41)</option>
						<option value="988">Wetterhaube (42)</option>
						<option value="989">Mädel (43)</option>
						<option value="990">Eunuch (44)</option>
						<option value="991">Jungfer (45)</option>
						<option value="992">Wildschützenkopf (46)</option>
						<option value="993">Wildschützennadel (47)</option>
						<option value="994">Säule (48)</option>
						<option value="995">Satan (49)</option>
						<option value="996">Schrammsteinturm (50)</option>
						<option value="997">Sonnenspitze (51)</option>
						<option value="999">Neptun (52)</option>
						<option value="1000">Wandwächter (53)</option>
						<option value="1001">Regenturm (54)</option>
						<option value="1002">Hinterer Torsteinkegel (55)</option>
						<option value="1003">Gespaltener Kegel (56)</option>
						<option value="1004">Saurier (57)</option>
						<option value="1005">Baustein (58)</option>
						<option value="1006">Müllerstein (59)</option>
						<option value="1007">Mittelturm (60)</option>
						<option value="1008">Sonnenwendkegel (61)</option>
						<option value="1009">Schwager (62)</option>
						<option value="1010">Onkel (63)</option>
						<option value="1011">Tante (64)</option>
						<option value="1012">Vorderer Torsteinkegel (65)</option>
						<option value="1013">Bergfex (66)</option>
						<option value="1014">Drohne (67)</option>
						<option value="1015">Mittlerer Torstein (68)</option>
						<option value="1016">Hoher Torstein (69)</option>
						<option value="1017">Falkenstein (70)</option>
						<option value="1018">Turnernadel (71)</option>
						<option value="1019">Zinne (72)</option>
						<option value="1020">Knabe (73)</option>
						<option value="1021">Oberer Lagerwächter (74)</option>
						<option value="1022">Mittlerer Lagerwächter (75)</option>
						<option value="1023">Unterer Lagerwächter (76)</option>
						<option value="1024">Kirnitzschturm (77)</option>
						<option value="1025">Kladderadatsch (78)</option>
						<option value="1026">Kirnitzschwand (79)</option>
						<option value="1027">Schweinskopf (80)</option>
					</optgroup>
					<optgroup label="Schmilkaer Gebiet">
						<option value="809">Bismarckfels (1)</option>
						<option value="810">Elbtalwächter (2)</option>
						<option value="811">Elbtalhorn (3)</option>
						<option value="813">Spitzkegel (4)</option>
						<option value="814">Teufelsturm (5)</option>
						<option value="815">Hohe Wand (6)</option>
						<option value="816">Breite-Kluft-Wand (7)</option>
						<option value="817">Breite-Kluft-Turm (8)</option>
						<option value="818">Rauschenspitze (9)</option>
						<option value="819">Rauschenkuppe (10)</option>
						<option value="820">Westlicher Rauschenturm (11)</option>
						<option value="821">Östlicher Rauschenturm (12)</option>
						<option value="822">Eckzahn (13)</option>
						<option value="823">Schützelkopf (14)</option>
						<option value="824">Nachbar (15)</option>
						<option value="825">Rauschentorwächter (16)</option>
						<option value="826">Klimmerstein (17)</option>
						<option value="827">Südwestlicher Wachturm (18)</option>
						<option value="828">Nordöstlicher Wachturm (19)</option>
						<option value="829">Rauschenstein (20)</option>
						<option value="830">Winklerturm (21)</option>
						<option value="831">Rauschengrundkegel (22)</option>
						<option value="832">Bergkristall (23)</option>
						<option value="833">Stülpner (24)</option>
						<option value="834">Doppelturm (25)</option>
						<option value="835">Rauschengrundnadel (26)</option>
						<option value="836">Rauschenkopf (27)</option>
						<option value="837">Großer Falknerturm (28)</option>
						<option value="838">Kleiner Falknerturm (29)</option>
						<option value="839">Pionierturm (30)</option>
						<option value="840">Rotkehlchenturm (31)</option>
						<option value="841">Stiegenwächter (32)</option>
						<option value="842">Ülmtülp (33)</option>
						<option value="843">Nebelturm (34)</option>
						<option value="844">Turm am Verborgenen Horn (35)</option>
						<option value="845">Heringsschwanz (36)</option>
						<option value="846">Heringsgrundnadel (37)</option>
						<option value="847">Muschelkopf (38)</option>
						<option value="848">Brechstange (39)</option>
						<option value="849">Windspitze (40)</option>
						<option value="850">Heiliger Wenzel (41)</option>
						<option value="851">Alter Bock (42)</option>
						<option value="852">Bussard (43)</option>
						<option value="853">Bussardwand (44)</option>
						<option value="854">Hinterer Bussardturm (45)</option>
						<option value="855">Mittlerer Bussardturm (46)</option>
						<option value="856">Vorderer Bussardturm (47)</option>
						<option value="857">Rauschensteiner Turm (48)</option>
						<option value="858">Flohspitze (49)</option>
						<option value="859">Heringsgrundwächter (50)</option>
						<option value="860">Heringsgrundscheibe (51)</option>
						<option value="861">Dorn (52)</option>
						<option value="862">Gerbingspitze (53)</option>
						<option value="863">Bonbon (54)</option>
						<option value="864">Fluchtwand (55)</option>
						<option value="865">Flüchtling (56)</option>
						<option value="866">Pfadfinder (57)</option>
						<option value="867">Neue Wenzelwand (58)</option>
						<option value="868">Schneeberger Spitze (59)</option>
						<option value="869">Schneeberger Nadel (60)</option>
						<option value="870">Hinterer Schneeberger Turm (61)</option>
						<option value="871">Vorderer Schneeberger Turm (62)</option>
						<option value="872">Kleiner Schartenkopf (63)</option>
						<option value="874">Großer Schartenkopf (64)</option>
						<option value="875">Frühlingsturm (65)</option>
						<option value="876">Püschnerturm (66)</option>
						<option value="877">Schwarzes Horn (67)</option>
						<option value="878">Abendturm (68)</option>
						<option value="879">Märchenturm (69)</option>
						<option value="880">Heringsgrundhorn (70)</option>
						<option value="881">Hirschquellenturm (71)</option>
						<option value="882">Heringsgrundturm (72)</option>
						<option value="884">Feldschmiede (73)</option>
						<option value="887">Sprunghorn (74)</option>
						<option value="888">Lehnnadel (75)</option>
						<option value="889">Lärchenturm (76)</option>
						<option value="890">Böser Turm (77)</option>
						<option value="891">II. Lehnsteigturm (78)</option>
						<option value="892">III. Lehnsteigturm (79)</option>
						<option value="893">Lolaturm (80)</option>
						<option value="894">Lehnwand (81)</option>
						<option value="895">Urvieh (82)</option>
						<option value="896">Lehnsteignadel (83)</option>
						<option value="897">Lehnscheibe (84)</option>
						<option value="898">Lehnkuppel (85)</option>
						<option value="899">Lehnriff (86)</option>
						<option value="900">Großer Gratturm (87)</option>
						<option value="901">Steinlochwächter (88)</option>
						<option value="902">Fünf Gipfel, Südturm (89)</option>
						<option value="903">Fünf Gipfel, NW-Turm (90)</option>
						<option value="904">Fünf Gipfel, NO-Turm (91)</option>
						<option value="905">Böhmeturm (92)</option>
						<option value="906">Steinlochturm (93)</option>
						<option value="907">Siamesische Zwillinge, Doof (94)</option>
						<option value="908">Siamesische Zwillinge, Dick (95)</option>
						<option value="909">Vorderer Verborgener Turm (96)</option>
						<option value="910">Mittlerer Verborgener Turm (97)</option>
						<option value="911">Hinterer Verborgener Turm (98)</option>
						<option value="912">Totensteiner Nadel (99)</option>
						<option value="913">Verborgenes Riff (100)</option>
						<option value="914">Verborgene Zinne (101)</option>
						<option value="915">Schadeturm (102)</option>
						<option value="916">Kleiner Gratturm (103)</option>
						<option value="917">Wurzelkopf (104)</option>
						<option value="918">Gamsturm (105)</option>
						<option value="919">Kapellenwandwächter (106)</option>
						<option value="920">Dornröschen (107)</option>
						<option value="921">Kulissenwächter (108)</option>
						<option value="922">Wurzelturm (109)</option>
						<option value="923">Wurzelnadel (110)</option>
						<option value="924">Unteres Buchentürmchen (111)</option>
						<option value="925">Oberes Buchentürmchen (112)</option>
						<option value="926">Bachturm (113)</option>
						<option value="927">Wurzelwarte (114)</option>
						<option value="928">Hennefels (115)</option>
						<option value="929">Coschrylenturm (116)</option>
						<option value="930">Sommerturm (117)</option>
						<option value="931">Winterturm (118)</option>
						<option value="932">Poblätzschturm (119)</option>
						<option value="933">Poblätzschspitze (120)</option>
						<option value="935">Poblätzschwand (121)</option>
						<option value="936">Lange Wand (122)</option>
						<option value="937">Vorderer Spätling (123)</option>
						<option value="938">Hinterer Spätling (124)</option>
						<option value="939">Wand am Kipphorn (125)</option>
						<option value="940">Kipphornwächter (126)</option>
						<option value="941">Zufallsturm (127)</option>
					</optgroup>
					<optgroup label="Affensteine">
						<option value="1">Vagabund (1)</option>
						<option value="2">Hallodri (2)</option>
						<option value="3">Lehnhorn (3)</option>
						<option value="4">Lehnwächter (4)</option>
						<option value="5">Lorenzsporn (5)</option>
						<option value="6">Lorenzwand (6)</option>
						<option value="7">Lorenzriff (7)</option>
						<option value="8">Lorenznadel (8)</option>
						<option value="9">Vorderer Lorenzturm (9)</option>
						<option value="10">Hinterer Lorenzturm (10)</option>
						<option value="11">Toter Turm (11)</option>
						<option value="12">Dickwanst (12)</option>
						<option value="13">Spieß (13)</option>
						<option value="14">Promenadenturm (14)</option>
						<option value="15">Promenadenspitze (15)</option>
						<option value="16">Promenadensäule (16)</option>
						<option value="17">Wackerzacke (17)</option>
						<option value="18">Wilder-Grund-Turm (18)</option>
						<option value="19">Affenwand (19)</option>
						<option value="20">Domerker (20)</option>
						<option value="21">Domkanzel (21)</option>
						<option value="22">Domwächter (22)</option>
						<option value="23">Rohnspitze (23)</option>
						<option value="24">Küster (24)</option>
						<option value="25">Dompfeiler (25)</option>
						<option value="26">Trabant (26)</option>
						<option value="27">1. Zerborstener Turm (27)</option>
						<option value="28">Zerborstene Nadel (28)</option>
						<option value="29">2. Zerborstener Turm (29)</option>
						<option value="30">Gespaltener Kopf (30)</option>
						<option value="31">Zerborstener Stein (31)</option>
						<option value="32">Zerborstene Wand (32)</option>
						<option value="33">Furz (33)</option>
						<option value="34">Steinmetz (34)</option>
						<option value="35">Zerborstene Scheibe (35)</option>
						<option value="36">Weißhorn (36)</option>
						<option value="37">Domnadel (37)</option>
						<option value="38">Däumling (38)</option>
						<option value="39">Dompfaff (39)</option>
						<option value="40">Domspitze (40)</option>
						<option value="41">Zitadelle (41)</option>
						<option value="42">Sandlochturm (42)</option>
						<option value="44">Sandlochscheibe (43)</option>
						<option value="45">Sandlochwächter (44)</option>
						<option value="46">Insel (45)</option>
						<option value="47">Vandale (46)</option>
						<option value="48">Höllenwand (47)</option>
						<option value="49">Höllenturm (48)</option>
						<option value="50">Ameisenturm (49)</option>
						<option value="51">Hähnelspitze (50)</option>
						<option value="52">Beelzebub (51)</option>
						<option value="53">Hauptdrilling (52)</option>
						<option value="54">Härtelturm (53)</option>
						<option value="55">Schuellernadel (54)</option>
						<option value="56">Höllentor (55)</option>
						<option value="57">Friensteiner Zacken (56)</option>
						<option value="58">Wilde Zinne (57)</option>
						<option value="59">Wilder Kopf (58)</option>
						<option value="61">Rokokoturm (59)</option>
						<option value="62">Glatze (60)</option>
						<option value="63">Friseur (61)</option>
						<option value="64">Partisan (62)</option>
						<option value="65">Panoramaturm (63)</option>
						<option value="66">Freier Turm (64)</option>
						<option value="67">Freie Wand (65)</option>
						<option value="68">Flachsköpfe (66)</option>
						<option value="69">Brosinnadel (67)</option>
						<option value="70">Amboss (68)</option>
						<option value="71">Teufelsspitze (69)</option>
						<option value="72">Brückenturm (70)</option>
						<option value="73">Jammerspitze (71)</option>
						<option value="74">Leuchterweibchen-Vorkopf (72)</option>
						<option value="75">Vorderes Leuchterweibchen (73)</option>
						<option value="76">Hinteres Leuchterweibchen (74)</option>
						<option value="77">Veteran (75)</option>
						<option value="79">Dämon (76)</option>
						<option value="78">Wotan (77)</option>
						<option value="80">Gipfelbubenkopf (78)</option>
						<option value="81">Bauerlochturm (79)</option>
						<option value="82">Nonnengärtner (80)</option>
						<option value="83">Bloßstock (81)</option>
						<option value="84">Kreuzturm (82)</option>
						<option value="85">Morsche Zinne (83)</option>
						<option value="86">Falsche Zinne (84)</option>
						<option value="87">Klosterwächter (85)</option>
						<option value="88">Nordstern (86)</option>
						<option value="89">Affenhorn (87)</option>
						<option value="90">Knochenturm (88)</option>
						<option value="91">Wolfsturm (89)</option>
						<option value="92">Wolfsnadel (90)</option>
						<option value="93">Backzahn (91)</option>
						<option value="94">Affenstein (92)</option>
						<option value="95">Wolfsspitze (93)</option>
						<option value="96">Wolfsfalle (94)</option>
						<option value="97">Gamshornspitze (95)</option>
						<option value="98">Hentzschelturm (96)</option>
						<option value="99">Gamshornwächter (97)</option>
						<option value="100">Satanskopf (98)</option>
						<option value="104">Turm der Freundschaft (99)</option>
						<option value="105">Greenhorn (100)</option>
						<option value="106">Heidelbeerturm (101)</option>
						<option value="107">Verwitterter Turm (102)</option>
						<option value="108">Kleiner Amboss (103)</option>
						<option value="109">Frienstein (104)</option>
						<option value="110">Friensteinwächter (105)</option>
						<option value="111">Untertan (106)</option>
						<option value="112">Friensteinwarte (107)</option>
						<option value="113">Grottenwart (108)</option>
						<option value="114">Friensteinkegel (109)</option>
						<option value="115">Vergessener Kegel (110)</option>
						<option value="116">Schandauer Turm (111)</option>
						<option value="117">Rollenturm (112)</option>
						<option value="118">Siegfried (113)</option>
						<option value="119">Bergfried (114)</option>
						<option value="120">Bergfriednadel (115)</option>
						<option value="121">Wespenturm (116)</option>
						<option value="122">Winterbergbarbarine (117)</option>
						<option value="123">Rauschensteiner Nadel (118)</option>
						<option value="124">Rübezahlturm (119)</option>
					</optgroup>
					<optgroup label="Kleiner Zschand">
						<option value="608">Doppeltürmchen (1)</option>
						<option value="609">Obere Winterbergspitze (2)</option>
						<option value="610">Untere Winterbergspitze (3)</option>
						<option value="611">Winterbergscheibe (4)</option>
						<option value="612">Winterbergwächter (5)</option>
						<option value="613">Nördlicher Gleitmannsturm (6)</option>
						<option value="614">Südlicher Gleitmannsturm (7)</option>
						<option value="616">Sammlerwand (8)</option>
						<option value="617">Winterbergnadel (9)</option>
						<option value="618">Vorderer Versteckter Turm (10)</option>
						<option value="619">Hinterer Versteckter Turm (11)</option>
						<option value="620">Heringsteinkegel (12)</option>
						<option value="621">Prinz Karneval (13)</option>
						<option value="622">Sprotte (14)</option>
						<option value="623">Heringstein (15)</option>
						<option value="624">Bewachsener Turm (16)</option>
						<option value="625">Heringsturm (17)</option>
						<option value="626">Heringshorn (18)</option>
						<option value="628">Friedensturm (19)</option>
						<option value="629">Kleines Bärenhorn (20)</option>
						<option value="630">Großes Bärenhorn (21)</option>
						<option value="631">Herbertfels (22)</option>
						<option value="632">Seife (23)</option>
						<option value="635">Elfiturm (24)</option>
						<option value="636">Kathinkaturm (25)</option>
						<option value="637">Meilensäule (26)</option>
						<option value="638">Bärfangkanzel (27)</option>
						<option value="639">Frühlingswand (28)</option>
						<option value="640">Vorderes Pechofenhorn (29)</option>
						<option value="641">Hexenspitze (30)</option>
						<option value="642">Pechschluchtturm (31)</option>
						<option value="643">Sumpfporstkegel (32)</option>
						<option value="644">Pechofenscheibe (33)</option>
						<option value="645">Köhler (34)</option>
						<option value="646">Pechofenstein (35)</option>
						<option value="647">Pechofenwarte (36)</option>
						<option value="648">Pechofenspitze (37)</option>
						<option value="649">Hinteres Pechofenhorn (38)</option>
						<option value="650">Wartburg (39)</option>
						<option value="651">Wintersteinwächter (40)</option>
						<option value="652">Bärfangkegel (41)</option>
						<option value="653">Bärfangwarte (42)</option>
						<option value="654">Zauberstab (43)</option>
						<option value="655">Moses (44)</option>
					</optgroup>
					<optgroup label="Großer Zschand">
						<option value="417">Goldstein (1)</option>
						<option value="418">Kaaba (2)</option>
						<option value="419">Grosses Spitzes Horn (3)</option>
						<option value="420">Kleines Spitzes Horn (4)</option>
						<option value="421">Goldsteigsäule (5)</option>
						<option value="422">Spitzhübel (6)</option>
						<option value="423">Goldsteigwächter (7)</option>
						<option value="424">Meilerstein (8)</option>
						<option value="425">Waldgeist (9)</option>
						<option value="426">Goldsteighorn (10)</option>
						<option value="427">Richterschluchtkopf (11)</option>
						<option value="428">Richterschluchtkegel (12)</option>
						<option value="429">Richterschluchtturm (13)</option>
						<option value="430">Grottenwächter (14)</option>
						<option value="431">Grenzwand (15)</option>
						<option value="432">Schwarze Zinne (16)</option>
						<option value="433">Spätes Horn (17)</option>
						<option value="434">Kleines Jortanshorn (18)</option>
						<option value="435">Zschandgendarm (19)</option>
						<option value="436">Jortanshorn (20)</option>
						<option value="437">Oktoberspitze (21)</option>
						<option value="438">Jortansriff (22)</option>
						<option value="439">Jortansturm (23)</option>
						<option value="440">Gratwand (24)</option>
						<option value="441">Schartenturm (25)</option>
						<option value="442">Fensterturm (26)</option>
						<option value="443">Sporn (27)</option>
						<option value="444">Weberschluchtwächter (28)</option>
						<option value="445">Adventspitze (29)</option>
						<option value="446">Lößnitzturm (30)</option>
						<option value="447">Blaues Horn (31)</option>
						<option value="448">Zweifreundespitze (32)</option>
						<option value="449">Weberschluchtturm (33)</option>
						<option value="450">Weberschluchtkegel (34)</option>
						<option value="451">Zweikiefernturm (35)</option>
						<option value="453">Weberschluchtstein (36)</option>
						<option value="454">Sommerwand (37)</option>
						<option value="455">Portalturm (38)</option>
						<option value="456">Freundschaftsnadel (39)</option>
						<option value="457">Großlitzner (40)</option>
						<option value="458">Großes Seehorn (41)</option>
						<option value="459">Kleines Seehorn (42)</option>
						<option value="460">Zschandnadel (43)</option>
						<option value="461">Weißer Turm (44)</option>
						<option value="462">Weiße Spitze (45)</option>
						<option value="463">Sandschlüchtehorn (46)</option>
						<option value="464">Sandschlüchteturm (47)</option>
						<option value="465">Kampfturm (48)</option>
						<option value="466">Auerhahn (49)</option>
						<option value="467">Kampfturmwächter (50)</option>
						<option value="468">Bergfreundschaftsstein (51)</option>
						<option value="469">Bergfreundschaftskegel (52)</option>
						<option value="470">Auerhahnwand (53)</option>
						<option value="475">Christelschluchtnadel (54)</option>
						<option value="476">Zeichengrundspitze (55)</option>
						<option value="477">Zeichengrundturm (56)</option>
						<option value="478">Unterer Hickelturm (57)</option>
						<option value="479">Vorderer Hickelturm (58)</option>
						<option value="480">Langes Horn (59)</option>
						<option value="481">Hinterer Hickelturm (60)</option>
						<option value="482">Dreiblockstein (61)</option>
						<option value="483">Hickelkopf (62)</option>
						<option value="484">Kleiner Edelweißturm (63)</option>
						<option value="485">Großer Edelweißturm (64)</option>
						<option value="486">Klingermassiv (65)</option>
						<option value="488">Krampus (66)</option>
						<option value="490">Tarzan (67)</option>
						<option value="492">Reitsteigwächter (68)</option>
						<option value="493">Thorwalder Wächter (69)</option>
						<option value="494">Thorwalder Turm (70)</option>
						<option value="495">Brötchen (71)</option>
						<option value="496">Backofen (72)</option>
						<option value="497">Erreichtturm (73)</option>
						<option value="498">Gewitterstein (74)</option>
						<option value="499">Pfingststein (75)</option>
						<option value="500">Thorwaldstein (76)</option>
						<option value="501">Thorwaldwand (77)</option>
						<option value="502">Dreiwinkelgrundwächter (78)</option>
						<option value="503">Dreiwinkelgrundturm (79)</option>
						<option value="504">Schreckensteiner Turm (80)</option>
					</optgroup>
					<optgroup label="Hinterhermsdorf">
						<option value="505">Scheibe am Tellerhörnel (1)</option>
						<option value="506">Dorfbachstein (2)</option>
						<option value="507">Dorfbachwand (3)</option>
						<option value="508">Keule (4)</option>
						<option value="509">Wildkatzenspitze (5)</option>
						<option value="510">Gemeinschaftsturm (6)</option>
						<option value="511">Kirnitzschkegel (7)</option>
						<option value="512">Rabensteinturm (8)</option>
						<option value="513">Raubschütznadel (9)</option>
						<option value="514">Raubschützturm (10)</option>
						<option value="515">Gamskopf (11)</option>
						<option value="518">Hinterhermsdorfer Turm (12)</option>
						<option value="519">Grüner Wenzel (13)</option>
						<option value="520">Hollturm (14)</option>
						<option value="521">Eisenspitze (15)</option>
						<option value="522">Dreibrüderstein (16)</option>
						<option value="523">Unterer Dreibrüderstein (17)</option>
					</optgroup>
					<optgroup label="Wildensteiner Gebiet">
						<option value="1179">Heidematz (1)</option>
						<option value="1180">Steinbachturm (2)</option>
						<option value="1181">Heidewand (3)</option>
						<option value="1182">Wildensteinscheibe (4)</option>
						<option value="1183">Münzstein (5)</option>
						<option value="1185">Glocke (6)</option>
						<option value="1186">Glöckner (7)</option>
						<option value="1187">Wildspitze (8)</option>
						<option value="1188">Wilderer (9)</option>
						<option value="1189">Zyklopenmauer (10)</option>
						<option value="1190">Ochsenkopf (11)</option>
						<option value="1191">Wildensteinwand (12)</option>
						<option value="1192">Blasketurm (13)</option>
						<option value="1193">Hebamme (14)</option>
						<option value="1194">Kuhstallscheibe (15)</option>
						<option value="1195">Hohler Turm (16)</option>
						<option value="1196">Hausbergwächter (17)</option>
						<option value="1197">Yeti (18)</option>
						<option value="1198">Großsteinnadel (19)</option>
						<option value="1199">Rabentürmchen (20)</option>
						<option value="1200">Lorenzsteinnadel (21)</option>
						<option value="1201">Großer Lorenzstein (22)</option>
						<option value="1202">Kleiner Lorenzstein (23)</option>
						<option value="1203">Monolith (24)</option>
						<option value="1205">Germane (25)</option>
						<option value="1206">Zschandspitze (26)</option>
						<option value="1207">Teichsteinnadel (27)</option>
						<option value="1208">Teichsteinwächter (28)</option>
						<option value="1209">Dunkle Wand (29)</option>
						<option value="1211">Kanstein-Vorgipfel (30)</option>
						<option value="1212">Kansteinnadel (31)</option>
						<option value="1213">Regenstein (32)</option>
						<option value="1214">Keil (33)</option>
						<option value="1215">E-Flügel-Wand (34)</option>
						<option value="1216">Rätselturm (35)</option>
						<option value="1217">Störznerfels (36)</option>
						<option value="1218">Buschmühlenturm (37)</option>
						<option value="1219">Grünling (38)</option>
						<option value="1220">Städelschlüchteturm (39)</option>
						<option value="1221">Eremit (40)</option>
						<option value="1222">Kleinsteinwand (41)</option>
						<option value="1223">Zätzschenhornstein (42)</option>
					</optgroup>
					<optgroup label="Steine">
						<option value="1030">Pilzwand (1)</option>
						<option value="1031">Ratsleitenturm (2)</option>
						<option value="1032">Struppengrundkegel (3)</option>
						<option value="1035">Rhombus (4)</option>
						<option value="1036">Bärensteinscheibe (5)</option>
						<option value="1038">Bärensteinwächter (6)</option>
						<option value="1039">Thürmsdorfer Stein (7)</option>
						<option value="1040">Bärensteinwarte (8)</option>
						<option value="1041">Drei Bären (9)</option>
						<option value="1042">Bärensteinklotz (10)</option>
						<option value="1043">Berg-Heil-Scheibe (11)</option>
						<option value="1044">Bärensteinnadel (12)</option>
						<option value="1046">Bärensteinturm (13)</option>
						<option value="1048">Riegelkopf (14)</option>
						<option value="1049">Conradturm (15)</option>
						<option value="1050">Dreizack (16)</option>
						<option value="1051">Knöchel (17)</option>
						<option value="1052">Rauensteinkopf (18)</option>
						<option value="1053">Dreifreundestein (19)</option>
						<option value="1054">Khedive (20)</option>
						<option value="1055">Rauensteinspitze (21)</option>
						<option value="1056">Rauensteinturm (22)</option>
						<option value="1469">Panoramascheibe (23)</option>
						<option value="1057">Rauensteinwächter (24)</option>
						<option value="1058">Nonne (25)</option>
						<option value="1059">Laasenturm (26)</option>
						<option value="1060">Heini (27)</option>
						<option value="1062">Liliensteinwächter (28)</option>
						<option value="1063">Liliensteinnadel (29)</option>
						<option value="1064">Spanghornturm (30)</option>
						<option value="1065">Teichwächter (31)</option>
						<option value="1066">Kiefernturm (32)</option>
						<option value="1067">Labyrinthwächter (33)</option>
						<option value="1068">Schiefer Block (34)</option>
						<option value="1470">Pfingstnadel (35)</option>
						<option value="1069">Pfingstkegel (36)</option>
						<option value="1070">Nikolsdorfer Turm (37)</option>
						<option value="1071">Nikolsdorfer Nadel (38)</option>
						<option value="1073">Kubus (39)</option>
						<option value="1074">Frosch (40)</option>
						<option value="1075">Barriere (41)</option>
						<option value="1076">Vergessener Turm (42)</option>
						<option value="1471">Stelzchenkegel (43)</option>
						<option value="1078">Enkel (44)</option>
						<option value="1088">Quirlwächter (45)</option>
						<option value="1087">Dreikanter (46)</option>
						<option value="1089">Einsiedler (47)</option>
						<option value="1090">Bundesfels (48)</option>
						<option value="1091">Glatter Turm (49)</option>
						<option value="1092">Nordturm (50)</option>
						<option value="1094">Nordkopf (51)</option>
						<option value="1095">Raue Zinne (52)</option>
						<option value="1472">Haselmaus (53)</option>
						<option value="1097">Nördliche Pfaffenschluchtspitze (54)</option>
						<option value="1098">Dreimännerturm (55)</option>
						<option value="1099">Abendwand (56)</option>
						<option value="1473">Hintere Abendwand (57)</option>
						<option value="1100">Nasse-Schlucht-Turm (58)</option>
						<option value="1101">Ratte (59)</option>
						<option value="1102">Bilch (60)</option>
						<option value="1103">Einsamer Ritter (61)</option>
						<option value="1104">Wolfswand (62)</option>
						<option value="1105">Südliche Pfaffenschluchtspitze (63)</option>
						<option value="1106">Junggeselle (64)</option>
						<option value="1107">Julikopf (65)</option>
						<option value="1108">Berglerturm (66)</option>
						<option value="1109">Pfaffenkopf (67)</option>
						<option value="1474">Toter Zwerg (68)</option>
						<option value="1110">Peterskirche (69)</option>
						<option value="1111">Jäckelfels (70)</option>
						<option value="1113">Hafersack (71)</option>
						<option value="1475">Schildkröte (72)</option>
						<option value="1115">Wilder Turm (73)</option>
						<option value="1116">Orgelpfeifenwand (74)</option>
						<option value="1117">Fritschfels (75)</option>
						<option value="1118">Vierling (76)</option>
						<option value="1342">Stiller Turm (77)</option>
						<option value="1119">Königsspitze (78)</option>
						<option value="1345">Quader (79)</option>
						<option value="1120">Keilerturm (80)</option>
						<option value="1121">Förster (81)</option>
						<option value="1123">Zwillinge (82)</option>
						<option value="1124">Pfaffenhütchen (83)</option>
						<option value="1125">Klamotte (84)</option>
						<option value="1126">Steinerne Scheune (85)</option>
						<option value="1476">Gohrischwächter (86)</option>
						<option value="1127">Abgetrennte Wand (87)</option>
						<option value="1128">Narrenkappe (88)</option>
						<option value="1129">Zwergfels (89)</option>
						<option value="1130">Gohrischscheibe (90)</option>
						<option value="1131">Findling (91)</option>
						<option value="1132">Papst (92)</option>
						<option value="1133">Kleine Hunskirche (93)</option>
						<option value="1134">Grosse Hunskirche (94)</option>
						<option value="1135">Räuberhöhlenturm (95)</option>
						<option value="1137">Bruchwächter (96)</option>
						<option value="1140">Schmale Wand (97)</option>
						<option value="1141">Kleingießhübler Turm (98)</option>
						<option value="1142">Zschirnsteinwächter (99)</option>
						<option value="1061">Lilienstein-Westecke (M1)</option>
						<option value="1081">Königstein (M2)</option>
						<option value="1149">Großer Zschirnstein (M3)</option>
						<option value="1144">Zschirnsteinwarte (100)</option>
						<option value="1145">Winkelblock (101)</option>
						<option value="1146">Wackelstein (102)</option>
						<option value="1477">Rentnerturm (103)</option>
						<option value="1148">Kleiner Zschirnsteinturm (104)</option>
						<option value="1150">Großer Zschirnsteinturm (105)</option>
						<option value="1151">Rotsteinkegel (106)</option>
						<option value="1152">Maus (107)</option>
						<option value="1153">Dicke Berta (108)</option>
						<option value="1154">Cunnersdorfer Nadel (109)</option>
						<option value="1155">Lampertshorn (110)</option>
						<option value="1369">Khan (14a)</option>
					</optgroup>
					<optgroup label="Brandgebiet">
						<option value="524">Osterspitze (1)</option>
						<option value="525">Hocksteinnadel (2)</option>
						<option value="526">Hocksteinturm (3)</option>
						<option value="527">Bärengartenscheibe (4)</option>
						<option value="528">Grosser Halben (5)</option>
						<option value="529">Kleiner Halben (6)</option>
						<option value="530">Drachenkopf (7)</option>
						<option value="531">Riesenechse (8)</option>
						<option value="532">Brandpyramide (9)</option>
						<option value="533">Ameise (10)</option>
						<option value="534">Ameisenwand (11)</option>
						<option value="535">Steinbruchnadel (12)</option>
						<option value="536">Steinbruchturm (13)</option>
						<option value="537">Grüner Stein (14)</option>
						<option value="538">Berken-von-der-Duba-Wacht (15)</option>
						<option value="539">Elefant (16)</option>
						<option value="540">Nashorn (17)</option>
						<option value="541">Clementine (18)</option>
						<option value="542">Schluchtturm (19)</option>
						<option value="543">Kolosseum (20)</option>
						<option value="544">Polenzwacht (21)</option>
						<option value="545">Falkenwarte (22)</option>
						<option value="546">Auerhahnfels (23)</option>
						<option value="547">Anstand (24)</option>
						<option value="548">Pantinenturm (25)</option>
						<option value="549">Polenztalbarbarine (26)</option>
						<option value="550">Polenztalwächter (27)</option>
						<option value="551">Räumichtturm (28)</option>
						<option value="552">Archipel (29)</option>
						<option value="553">Gespaltene Zinne (30)</option>
						<option value="554">Panoramafels (31)</option>
						<option value="555">Begangsteigriff (32)</option>
						<option value="556">Kobold (33)</option>
						<option value="557">Neuwegwand (34)</option>
						<option value="558">Silvesterturm (35)</option>
						<option value="559">Saugrundspitze (36)</option>
						<option value="560">Neuwegkanzel (37)</option>
						<option value="561">Saugrundwächter (38)</option>
						<option value="562">Schwarzwildturm (39)</option>
						<option value="563">Verlassener Turm (40)</option>
						<option value="564">Einsamer Stein (41)</option>
						<option value="565">Glatter Steinturm (42)</option>
						<option value="566">Tonne (43)</option>
						<option value="567">Spund (44)</option>
						<option value="568">Drillingsturm (45)</option>
						<option value="569">Dezemberturm (46)</option>
						<option value="570">Geyergucke (47)</option>
						<option value="571">Hans-Arno-Stein (48)</option>
						<option value="572">Winkelturm (49)</option>
						<option value="573">Tiefblickspitze (50)</option>
						<option value="574">Spanische Wand (51)</option>
						<option value="575">Loriturm (52)</option>
						<option value="576">Brandscheibe (53)</option>
						<option value="577">Kleine Brandscheibe (54)</option>
						<option value="578">Hexe (55)</option>
						<option value="579">Zeigefinger (56)</option>
						<option value="580">Kleine Barbarine (57)</option>
						<option value="581">Viermännerturm (58)</option>
						<option value="582">Ahornspitze (59)</option>
						<option value="583">Hafersackkrone (60)</option>
						<option value="584">Brandkegel (61)</option>
						<option value="585">Brandkopf (62)</option>
						<option value="586">Brandturm (63)</option>
						<option value="587">Auguste (64)</option>
						<option value="588">August (65)</option>
						<option value="589">Hunskirchlerspitze (66)</option>
						<option value="590">Dastellochturm (67)</option>
						<option value="591">Tiefer-Grund-Turm (68)</option>
						<option value="592">Tiefer-Grund-Wächter (69)</option>
						<option value="593">Tiefe Wand (70)</option>
						<option value="594">Forstgrabenwand (71)</option>
						<option value="595">Forstgrabenturm (72)</option>
						<option value="596">Waitzdorfer Zinne (73)</option>
						<option value="597">Lärmchenturm (74)</option>
						<option value="598">Michaelistagstein (75)</option>
						<option value="599">Ochelscheibe (76)</option>
						<option value="600">Ochelturm (77)</option>
						<option value="601">Popanz (78)</option>
						<option value="602">Ochelspitze (79)</option>
						<option value="603">Bonifaz (80)</option>
						<option value="604">Berg-Frei-Turm (81)</option>
						<option value="605">Schinderkopf (82)</option>
						<option value="606">Promon (83)</option>
						<option value="607">Bahnhofswächter (84)</option>
					</optgroup>
					<optgroup label="SBB Klettergärten">
						<option value="1425">Klettergarten Liebethal</option>
						<option value="1426">Klettergarten Cunnersdorf</option>
						<option value="1484">Klettergarten Rochlitz</option>
						<option value="1485">Rochlitz Klettergarten - Seidelbruch Hauptwand</option>
						<option value="1486">Rochlitz Klettergarten - Bruchwächter</option>
						<option value="1488">Rochlitz Klettergarte - Schattenwand</option>
					</optgroup>
				</select>
			
			<div class="rangeLabel">
				<nobr><label for="cutoffCoerr">Min. Corr.Coeff.</label>[<output>70</output>%]:</nobr>
				<input type="range" id="cutoffCoerr" name="cutoffCoerr" min="0" max="100" step="1" value="70" oninput="this.previousElementSibling.querySelector('output').value=this.value" list="my-detents"/>
				<datalist id="my-detents">
					<option value="0" label="0"/>
					<option value="10" label="10"/>
					<option value="20" label="20"/>
					<option value="30" label="30"/>
					<option value="40" label="40"/>
					<option value="50" label="50"/>
					<option value="60" label="60"/>
					<option value="70" label="70"/>
					<option value="80" label="80"/>
					<option value="90" label="90"/>
					<option value="100" label="100"/>
				</datalist>
			</div>
			</form>
		</div>
		<div id="myPlotlyDiv" style="margin-left: 600px;"/>
	</div>

<table border="1" id="content-table">
<thead>
	<tr>
		<th>SBB-Database</th>
		<th>Corr. Coeff.</th>
		<th>Sandsteinklettern</th>
		<th>Corr. Coeff.</th>
		<th>Teufelsturm</th>
	</tr>
</thead>
        <tbody>
%for row in rows:
  <tr class="draggable" draggable="true">
<td data-column="1" class="draggable" draggable="true">
	<div class="right-column">
		<div class="row">
			<div class="field">
				<span class="field_label">sbb_id:</span>
				<span class="field_value">{{row[0]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="field">
				<span class="field_label">sbb_gipfel:</span>
				<span class="field_value">{{row[1]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="half-field">
				<span class="field_label">sbb_Weg::</span>
				<span class="emphasized_field_value">{{row[2]}}</span>
				<span class="field_label">sbb_grade:</span>
				<span class="emphasized_field_value">{{row[3]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="field">
				<span class="field_label">sbb_erstbegeher:</span>
				<span class="field_value">{{row[4]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="field">
				<span class="field_label">&#8226;</span>
				<span class="field_value">{{row[5]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="field">
				<span class="field_label">Im KleFü nach welchem Weg?:</span>
				<span class="unemphasized_field_value">{{row[6]}}</span>
			</div>
		</div>
		<div class="row">
			<div class="field">
				<span class="field_label">Variante von:</span>
				<span class="unemphasized_field_value">{{row[7]}}</span>
			</div>
		</div>
	</div>
</td>
    
    <td data-column="2" draggable="false">
        <div class="middle-column">
            <div class="row">
                <div class="field">
                    <span class="field_label">Corr. Coeff. zu SSK-Weg:</span><br>
                    <span class="field_value">{{row[8]}}</span>
                </div>
            </div>
        </div>
    </td>
    
    <td data-column="3" class="draggable" draggable="true">
        <div class="right-column">
            <div class="row">
                <div class="field">
                    <span class="field_label">ssk_id:</span>
                    <span class="field_value">
                        <a href="http://db-sandsteinklettern.gipfelbuch.de/komment.php?wegid={{row[9]}}">{{row[9]}}</a>
                    </span>
                </div>
            </div>
            <div class="row">
                <div class="field">
                    <span class="field_label">ssk_gipfel:</span>
                    <span class="field_value">{{row[10]}}</span>
                </div>
            </div>
            <div class="row">
                <div class="half-field">
                    <span class="field_label">ssk_Weg::</span>
                    <span class="emphasized_field_value">{{row[11]}}</span>
                    <span class="field_label">ssk_grade:</span>
                    <span class="emphasized_field_value">{{row[12]}}</span>
                </div>
                <div class="row">
                    <div class="field">
                        <span class="field_label">ssk_erstbegeher:</span>
                        <span class="field_value">{{row[13]}}</span>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="field">
                    <span class="field_label">&#8226;</span>
                    <span class="field_value">{{row[14]}}</span>
                </div>
            </div>
        </div>
    </td>
    
    <td  data-column="4" draggable="false">
        <div class="middle-column">
            <div class="row">
                <div class="field">
                    <span class="field_label">Corr. Coeff. zu TT-Weg:</span><br>
                    <span class="field_value">{{row[15]}}</span>
                </div>
            </div>
        </div>
    </td>
    
    <td data-column="5" class="draggable" draggable="true">
        <div class="right-column">
            <div class="row">
                <div class="field">
                    <span class="field_label">tt_id:</span>
                    <span class="field_value">
                        <a href="https://teufelsturm.de/wege/bewertungen/anzeige.php?wegnr={{row[16]}}">{{row[16]}}</a>
                    </span>
                </div>
            </div>
            <div class="row">
                <div class="field">
                    <span class="field_label">tt_gipfel:</span>
                    <span class="field_value">{{row[17]}}</span>
                </div>
            </div>
            <div class="row">
                <div class="half-field">
                    <span class="field_label">tt_Weg::</span>
                    <span class="emphasized_field_value">{{row[18]}}</span>
                    <span class="field_label">tt_grade:</span>
                    <span class="emphasized_field_value">{{row[19]}}</span>
                </div>
                <div class="row">
                    <div class="field">
                        <span class="field_label">tt_erstbegeher:</span>
                        <span class="field_value">{{row[20]}}</span>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="field">
                    <span class="field_label">&#8226;</span>
                    <span class="field_value">{{row[21]}}</span>
                </div>
            </div>
        </div>
    </td>
  </tr>
%end
</tbody>
</table>
</body>
    <script src="make_route_table.js" charset="utf-8"></script>

    <script>
		document.getElementsByTagName('input')[1].value = {{cutOff}};
		document.getElementsByTagName('input')[1].previousElementSibling.querySelector('output').value={{cutOff}};
		document.getElementsByTagName('select')[0].value = {{summit_no}}
    </script>
</html>