import re
from datetime import datetime
from enum import Enum
import  EnumSachsenSchwierigkeitsGrad
import tt_route_comment_object as TT_WegeKommentar
import re
from datetime import datetime
from typing import List, Optional
from enum import Enum

class TT_Gipfel:
    def __init__(self, gipfel_nr):
        self.gipfel_nr = gipfel_nr

    def getIntGipfelNr(self):
        return self.gipfel_nr

class TT_WegeKommentar:
    def __init__(self, kletterweg, kommentar):
        self.kletterweg = kletterweg
        self.kommentar = kommentar

class TT_KletterWeg:
    lstAlleKletterWege: List['TT_KletterWeg'] = []  # Class-level list

    def __init__(self, aParent: TT_Gipfel, aIntWegNr: int, strWegeBewertungen: str) -> None:
        self.intTTWegNr: int = aIntWegNr
        self.intTTGipfelNr: int = aParent.getIntGipfelNr()
        self.myGipfelParent: TT_Gipfel = aParent
        self.strWegName: str = ""
        self.strSchwierigkeitsGrad: str = ""
        self.blnAusrufeZeichen: bool = False
        self.intSterne: int = 0
        self.sachsenSchwierigkeitsGrad: EnumSachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na
        self.ohneUnterstuetzungSchwierigkeitsGrad: EnumSachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na
        self.rotPunktSchwierigkeitsGrad: EnumSachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na
        self.intSprungSchwierigkeitsGrad: int = float('inf')
        self.strErstbegeher: str = ""
        self.strErstbegehungsdatum: str = ""
        self.strWegbeschreibung: str = ""
        self.lstKommentare: List[TT_WegeKommentar] = []
        
        # eigene Werte
        self.myIsBestiegen: bool = False
        self.myDatumBestiegen: datetime = datetime.max
        self.myLongDatumBestiegen: int = float('inf')
        self.myStrKommentar: str = ""
        
        self.parse_wegebewertungen(strWegeBewertungen)

    def parse_wegebewertungen(self, strWegeBewertungen: str) -> None:
        strWegeBewertungen = re.sub(r"\r\n", ". ", strWegeBewertungen)
        strWegeBewertungen = re.sub(r"<table", "\r\n<table", strWegeBewertungen)
        strWegeBewertungen = re.sub(r"</tr>", "</tr>\r\n", strWegeBewertungen)

        self.intSprungSchwierigkeitsGrad = float('inf')
        self.myLongDatumBestiegen = float('inf')

        # Extract WegName
        weg_name_pattern = re.compile(r'<font face="Tahoma" size="3"><font color="#FFFFFF">(.*?)</font>',
                                       re.UNICODE | re.IGNORECASE | re.DOTALL)
        weg_name_match = weg_name_pattern.search(strWegeBewertungen)
        if weg_name_match:
            self.strWegName = weg_name_match.group(1).strip()

        # Extract Schwierigkeit
        schwierigkeitsgrad_pattern = re.compile(r'<font face="Tahoma" size="2">\[(.*?)\]<br>',
                                                re.UNICODE | re.IGNORECASE | re.DOTALL)
        schwierigkeitsgrad_match = schwierigkeitsgrad_pattern.search(strWegeBewertungen)
        if schwierigkeitsgrad_match:
            self.strSchwierigkeitsGrad = schwierigkeitsgrad_match.group(1).strip()

        # Check for Ausrufezeichen
        if "!" in self.strSchwierigkeitsGrad:
            self.blnAusrufeZeichen = True

        # Count Sterne
        self.intSterne = self.strSchwierigkeitsGrad.count('*')
        self.strSchwierigkeitsGrad = re.sub(r'\*+', '', self.strSchwierigkeitsGrad).strip()

        # Extract ohne Unterstützung Schwierigkeitsgrad
        ohne_unterstuetzung_pattern = re.compile(r'\((.*[IVXabc]*?)\)', re.UNICODE | re.IGNORECASE | re.DOTALL)
        ohne_unterstuetzung_match = ohne_unterstuetzung_pattern.search(self.strSchwierigkeitsGrad)
        if ohne_unterstuetzung_match:
            try:
                self.ohneUnterstuetzungSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad[ohne_unterstuetzung_match.group(1).strip()]
            except KeyError:
                self.ohneUnterstuetzungSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na

            self.strSchwierigkeitsGrad = re.sub(r'\(.*[IVXabc]*?\)', '', self.strSchwierigkeitsGrad).strip()

        # Extract Rotpunkt Schwierigkeitsgrad
        rotpunkt_pattern = re.compile(r'RP(.*[IVXabc]*?)', re.UNICODE | re.IGNORECASE | re.DOTALL)
        rotpunkt_match = rotpunkt_pattern.search(self.strSchwierigkeitsGrad)
        if rotpunkt_match:
            try:
                self.rotPunktSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad[rotpunkt_match.group(1).strip()]
            except KeyError:
                self.rotPunktSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na

            self.strSchwierigkeitsGrad = re.sub(r'RP.*[IVXabc]*?', '', self.strSchwierigkeitsGrad).strip()

        # Extract Sprung Schwierigkeitsgrad
        sprungschwierigkeitsgrad_pattern = re.compile(r'(\d+)', re.UNICODE | re.IGNORECASE | re.DOTALL)
        sprungschwierigkeitsgrad_match = sprungschwierigkeitsgrad_pattern.search(self.strSchwierigkeitsGrad)
        if sprungschwierigkeitsgrad_match:
            self.intSprungSchwierigkeitsGrad = int(sprungschwierigkeitsgrad_match.group(1).strip())
            self.strSchwierigkeitsGrad = re.sub(r'\d+', '', self.strSchwierigkeitsGrad).strip()

        # Extract Sachsen Schwierigkeitsgrad
        sachsen_schwierigkeitsgrad_pattern = re.compile(r'^[\s*/]*(.*[IVXabc]*?)', re.UNICODE | re.IGNORECASE | re.DOTALL)
        sachsen_schwierigkeitsgrad_match = sachsen_schwierigkeitsgrad_pattern.search(self.strSchwierigkeitsGrad)
        if sachsen_schwierigkeitsgrad_match:
            if sachsen_schwierigkeitsgrad_match.group(1).strip() == "":
                self.sachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na
            else:
                try:
                    self.sachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad[sachsen_schwierigkeitsgrad_match.group(1).strip()]
                except KeyError:
                    self.sachsenSchwierigkeitsGrad = EnumSachsenSchwierigkeitsGrad.na

        # Extract Erstbegeher
        erstbegeher_pattern = re.compile(r'<td width="10%" valign="top"><font face="Tahoma" size="2">Erstbegeher:</font></td><td><font color="#FFFFFF" face="Tahoma" size="2">(.*)</font></td>',
                                          re.UNICODE | re.IGNORECASE)
        erstbegeher_match = erstbegeher_pattern.search(strWegeBewertungen)
        if erstbegeher_match:
            self.strErstbegeher = erstbegeher_match.group(1).strip() or ""

        # Extract Erstbegehungsdatum
        erstbegehungsdatum_pattern = re.compile(r'<td width="10%" valign="top"><font face="Tahoma" size="2">Erstbegehungsdatum:</font></td><td><font color="#FFFFFF" face="Tahoma" size="2">(.*)</font></td>',
                                                 re.UNICODE | re.IGNORECASE)
        erstbegehungsdatum_match = erstbegehungsdatum_pattern.search(strWegeBewertungen)
        if erstbegehungsdatum_match:
            self.strErstbegehungsdatum = erstbegehungsdatum_match.group(1).strip() or ""

        # Extract Wegbeschreibung
        wegbeschreibung_pattern = re.compile(r'<td width="10%" valign="top"><font face="Tahoma" size="2">Wegbeschreibung:</font></td><td><font color="#FFFFFF" face="Tahoma" size="2">(.*)</font></td>',
                                              re.UNICODE | re.IGNORECASE)
        wegbeschreibung_match = wegbeschreibung_pattern.search(strWegeBewertungen)
        if wegbeschreibung_match:
            self.strWegbeschreibung = wegbeschreibung_match.group(1).strip() or ""

        # Extract Kommentare
        kommentar_pattern = re.compile(r'<tr>    <td width="10%" bgcolor="#274C8C" valign="top">(.*?)</tr>',
                                       re.UNICODE | re.IGNORECASE | re.DOTALL)
        kommentar_matches = kommentar_pattern.findall(strWegeBewertungen)
        for kommentar in kommentar_matches:
            self.lstKommentare.append(TT_WegeKommentar(self, kommentar.strip()))

    def __str__(self) -> str:
        return f"{self.strWegName} | {self.strSchwierigkeitsGrad} | {self.intTTWegNr} | {self.intTTGipfelNr}"

    def get_wet_data(self) -> dict:
        return {
            'weg_name': self.strWegName,
            'schwierigkeitsgrad': self.strSchwierigkeitsGrad,
            'erstbegeher': self.strErstbegeher,
            'erstbegehungsdatum': self.strErstbegehungsdatum,
            'wegbeschreibung': self.strWegbeschreibung,
            'sterne': self.intSterne,
            'sachsen_schwierigkeitsgrad': self.sachsenSchwierigkeitsGrad.name,
            'sprung_schwierigkeitsgrad': self.intSprungSchwierigkeitsGrad,
        }

# Example usage
# writer = ... # Some writer instance that implements write method
# gipfel = TT_Gipfel(1)
# kletterweg = TT_KletterWeg(gipfel, 1, "<table>...</table>", writer)
# print(kletterweg)
