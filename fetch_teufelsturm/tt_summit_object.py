import re
import urllib.request
from urllib.error import URLError, HTTPError
import tt_route_object as TT_KletterWeg


class Coordinates:
    def __init__(self, latitude=float('nan'), longitude=float('nan')):
        self.latitude = latitude
        self.longitude = longitude

    def setLatitude(self, latitude):
        self.latitude = latitude

    def setLongitude(self, longitude):
        self.longitude = longitude

class TT_Gipfel:
    def __init__(self, aIntGipfelNr, aStrGipfelDetails, aStrWegeSuche):
        self.intGipfelNr = aIntGipfelNr
        self.tt_GipfelGPSKoordinaten = Coordinates()
        self.strName = None
        self.strGebiet = None
        self.lstBenachbarteGipfel = []
        self.lstIntKletterWeg = []
        self.lstObjKletterWeg = []
        self.strWegeBewertungen = ""

        # Search for Gipfelname
        myPattern = re.compile(r'<b><font face="Tahoma" color="#FFFFFF" size="3">(.*?)</font>', re.UNICODE | re.IGNORECASE | re.DOTALL)
        myMatcher = myPattern.search(aStrGipfelDetails)
        if myMatcher:
            self.strName = myMatcher.group(1)

        # Search for Gebiet
        myPattern = re.compile(r'</b> <b><font face="Tahoma" size="2">\[(.*?)\]</font>', re.UNICODE | re.IGNORECASE | re.DOTALL)
        myMatcher = myPattern.search(aStrGipfelDetails)
        if myMatcher:
            self.strGebiet = myMatcher.group(1)

        print(f"Gipfelnr. : {self.intGipfelNr}\t{self.strName} ({self.strGebiet})")

        # Search for Longitude
        myPattern = re.compile(r'Longitude</font></td><td width="70%"><font face="Tahoma" size="2">(.*?)</font>', re.UNICODE | re.IGNORECASE | re.DOTALL)
        myMatcher = myPattern.search(aStrGipfelDetails)
        if myMatcher:
            try:
                self.tt_GipfelGPSKoordinaten.setLatitude(float(myMatcher.group(1)))
            except ValueError as e:
                print(f"Fehler beim Lesen der GPS-Breite: {e}")

        # Search for Latitude
        myPattern = re.compile(r'Latitude</font></td><td width="70%"><font face="Tahoma" size="2">(.*?)</font>', re.UNICODE | re.IGNORECASE | re.DOTALL)
        myMatcher = myPattern.search(aStrGipfelDetails)
        if myMatcher:
            try:
                self.tt_GipfelGPSKoordinaten.setLongitude(float(myMatcher.group(1)))
            except ValueError as e:
                print(f"Fehler beim Lesen der GPS-Länge: {e}")

        # Search for neighboring peaks
        myPattern = re.compile(r'\[<a href="suche.php\?gipfelnr=(\d*)"', re.UNICODE | re.IGNORECASE | re.DOTALL)
        for match in myPattern.finditer(aStrWegeSuche):
            self.lstBenachbarteGipfel.append(int(match.group(1)))

        # Search for climbing paths
        myPattern = re.compile(r'<a href="/wege/bewertungen/anzeige.php\?wegnr=(\d*)"', re.UNICODE | re.IGNORECASE | re.DOTALL)
        for match in myPattern.finditer(aStrWegeSuche):
            strMatcher = match.group(1)
            try:
                strWegeBewertungen = self.get_url_source(f"http://www.teufelsturm.de/wege/bewertungen/anzeige.php?wegnr={strMatcher}")
            except URLError as ex:
                print(f"URL error occurred: {ex}")
            except HTTPError as ex:
                print(f"HTTP error occurred: {ex}")

            intWegNr = int(strMatcher)

            if intWegNr not in self.lstIntKletterWeg:
                self.lstIntKletterWeg.append(intWegNr)
                aTT_KletterWeg = TT_KletterWeg(self, intWegNr, strWegeBewertungen.replace("\n", ". "))
                self.lstObjKletterWeg.append(aTT_KletterWeg)

        lstAlleGipfel.append(self)

    def get_url_source(self, url):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as ex:
            raise RuntimeError(f"Failed to fetch data from {url}: {ex}")

# Usage of lstAlleGipfel must be declared globally or initialized somewhere
lstAlleGipfel = []

# Additional classes and methods like TT_KletterWeg should be defined similarly.
