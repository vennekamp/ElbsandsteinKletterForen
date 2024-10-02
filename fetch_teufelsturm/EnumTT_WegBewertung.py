from enum import Enum

class EnumTT_WegBewertung(Enum):
    NONE = -1
    KAMIKAZE = 0
    SEHR_SCHLECHT = 1
    SCHLECHT = 2
    NORMAL = 3
    GUT = 4
    SEHR_GUT = 5
    HERAUSRAGEND = 6

    def __init__(self, value):
        self.value = value

    @staticmethod
    def getMinInteger():
        return -1

    @staticmethod
    def getMaxInteger():
        return 6

    def getValue(self):
        return self.value

    def __str__(self):
        if self == EnumTT_WegBewertung.NONE:
            return "??? (fehlerhafte Abfrage)"
        elif self == EnumTT_WegBewertung.KAMIKAZE:
            return "--- (Kamikaze)"
        elif self == EnumTT_WegBewertung.SEHR_SCHLECHT:
            return "-- (sehr schlecht)"
        elif self == EnumTT_WegBewertung.SCHLECHT:
            return "- (schlecht)"
        elif self == EnumTT_WegBewertung.NORMAL:
            return "(Normal)"
        elif self == EnumTT_WegBewertung.GUT:
            return "+ (gut)"
        elif self == EnumTT_WegBewertung.SEHR_GUT:
            return "++ (sehr gut)"
        elif self == EnumTT_WegBewertung.HERAUSRAGEND:
            return "+++ (Herausragend)"
        else:
            return super().__str__()

    @staticmethod
    def toTT_Bewertung(description):
        if description == "--- (Kamikaze)":
            return EnumTT_WegBewertung.KAMIKAZE
        elif description == "-- (sehr schlecht)":
            return EnumTT_WegBewertung.SEHR_SCHLECHT
        elif description == "- (schlecht)":
            return EnumTT_WegBewertung.SCHLECHT
        elif description == "(Normal)":
            return EnumTT_WegBewertung.NORMAL
        elif description == "+ (gut)":
            return EnumTT_WegBewertung.GUT
        elif description == "++ (sehr gut)":
            return EnumTT_WegBewertung.SEHR_GUT
        elif description == "+++ (Herausragend)":
            return EnumTT_WegBewertung.HERAUSRAGEND
        else:
            raise ValueError(f"Unknown Wegbewertung in Comments: {description}")
