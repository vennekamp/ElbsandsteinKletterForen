import re
from datetime import datetime
import logging

class TT_WegeKommentar:
    def __init__(self, aTT_KletterWeg, strTTKommentar, writer):
        self.myTT_KletterWeg = aTT_KletterWeg
        self.strEntryUser = None
        self.longEntryDatum = None
        self.entryDatum = None
        self.strEntryKommentar = None
        self.entryBewertung = None

        # Regular expression to extract entry user
        user_pattern = re.compile(r'<font color="#FFFFFF" size="2" face="Tahoma"><b>(.*?)</font>',
                                  re.UNICODE | re.IGNORECASE | re.DOTALL)
        user_match = user_pattern.search(strTTKommentar)
        if user_match:
            self.strEntryUser = user_match.group(1).strip()

        # Regular expression to extract entry date
        date_pattern = re.compile(r'<br><br>(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2})</b></font>',
                                  re.UNICODE | re.IGNORECASE | re.DOTALL)
        date_match = date_pattern.search(strTTKommentar)
        if date_match:
            date_str = date_match.group(1).replace('<br>', '').strip()
            try:
                self.entryDatum = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
                self.longEntryDatum = int(self.entryDatum.timestamp() * 1000)
            except Exception as ex:
                logging.error("Date parsing error: %s", ex)

        # Regular expression to extract entry comment
        comment_pattern = re.compile(r'<font size="2" face="Tahoma">      (.*?)</font>',
                                     re.UNICODE | re.IGNORECASE | re.DOTALL)
        comment_match = comment_pattern.search(strTTKommentar)
        if comment_match:
            self.strEntryKommentar = comment_match.group(1).strip()
            # Replace smileys and break tags
            self.strEntryKommentar = self.strEntryKommentar.replace('<img src="/img/smileys/smile.gif">', ":-)")
            self.strEntryKommentar = self.strEntryKommentar.replace('<img src="/img/smileys/wink.gif">', ";-)")
            self.strEntryKommentar = self.strEntryKommentar.replace('<img src="/img/smileys/frown.gif">', ":-(")
            self.strEntryKommentar = re.sub(r'<br\s*/?>', '\r\n', self.strEntryKommentar)

        # Regular expression to extract entry rating
        rating_pattern = re.compile(r'<font size="2" face="Tahoma">(' +
                                    r'--- \(Kamikaze\)|' +
                                    r'-- \(sehr schlecht\)|' +
                                    r'- \(schlecht\)|' +
                                    r'\(Normal\)|' +
                                    r'\+ \(gut\)|' +
                                    r'\+\+ \(sehr gut\)|' +
                                    r'\+\+\+ \(Herausragend\)' +
                                    r')</font>',
                                    re.UNICODE | re.IGNORECASE | re.DOTALL)
        rating_match = rating_pattern.search(strTTKommentar)
        if rating_match:
            strMatcher = rating_match.group(1).strip()
            self.entryBewertung = EnumTT_WegBewertung.toTT_Bewertung(strMatcher)

        # If no rating is found, default to NONE
        if self.entryBewertung is None:
            self.entryBewertung = EnumTT_WegBewertung.NONE

    def get_my_tt_kletterweg(self):
        return self.myTT_KletterWeg

    def get_str_entry_user(self):
        return self.strEntryUser

    def get_long_entry_datum(self):
        return self.longEntryDatum

    def get_str_entry_kommentar(self):
        return self.strEntryKommentar

    def get_entry_bewertung(self):
        return self.entryBewertung


# Enum to mimic the behavior of EnumTT_WegBewertung
class EnumTT_WegBewertung:
    NONE = 'NONE'
    KAMIKAZE = '--- (Kamikaze)'
    VERY_BAD = '-- (sehr schlecht)'
    BAD = '- (schlecht)'
    NORMAL = '(Normal)'
    GOOD = '+ (gut)'
    VERY_GOOD = '++ (sehr gut)'
    OUTSTANDING = '+++ (Herausragend)'

    @staticmethod
    def toTT_Bewertung(value):
        mapping = {
            "--- (Kamikaze)": EnumTT_WegBewertung.KAMIKAZE,
            "-- (sehr schlecht)": EnumTT_WegBewertung.VERY_BAD,
            "- (schlecht)": EnumTT_WegBewertung.BAD,
            "(Normal)": EnumTT_WegBewertung.NORMAL,
            "+ (gut)": EnumTT_WegBewertung.GOOD,
            "++ (sehr gut)": EnumTT_WegBewertung.VERY_GOOD,
            "+++ (Herausragend)": EnumTT_WegBewertung.OUTSTANDING
        }
        return mapping.get(value, EnumTT_WegBewertung.NONE)
