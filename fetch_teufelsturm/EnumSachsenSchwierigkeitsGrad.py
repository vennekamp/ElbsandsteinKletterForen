from enum import Enum

class EnumSachsenSchwierigkeitsGrad(Enum):
    # Difficulty levels multiplied by 10
    na = float('-inf')
    I = 10
    II = 20
    III = 30
    IV = 40
    V = 50
    VI = 60
    VIIa = 71
    VIIb = 72
    VIIc = 73
    VIIIa = 81
    VIIIb = 82
    VIIIc = 83
    IXa = 91
    IXb = 92
    IXc = 93
    Xa = 101
    Xb = 102
    Xc = 103
    XIa = 111
    XIb = 112
    XIc = 113
    XIIa = 121
    XIIb = 122
    XIIc = 123
    XIIIa = 130
    Sprung1 = 151
    Sprung2 = 152
    Sprung3 = 153
    Sprung4 = 154

    def get_value(self):
        return self.value
    
    @staticmethod
    def to_string_from_scale_ordinal(valueI):
        # Mapping ordinal values to strings
        scale_ordinal_mapping = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
            7: "VIIa", 8: "VIIb", 9: "VIIc", 10: "VIIIa", 11: "VIIIb", 12: "VIIIc",
            13: "IXa", 14: "IXb", 15: "IXc", 16: "Xa", 17: "Xb", 18: "Xc",
            19: "XIa", 20: "XIb", 21: "XIc", 22: "XIIa", 23: "XIIb", 24: "XIIc",
            25: "XIIIa", 26: "Spr. 1", 27: "Spr. 2", 28: "Spr. 3", 29: "Spr. 4"
        }
        return scale_ordinal_mapping.get(valueI, "")
    
    @staticmethod
    def to_string(valueInt):
        # Mapping difficulty levels to their string representations
        difficulty_mapping = {
            10: "I", 20: "II", 30: "III", 40: "IV", 50: "V", 60: "VI",
            71: "VIIa", 72: "VIIb", 73: "VIIc", 81: "VIIIa", 82: "VIIIb", 83: "VIIIc",
            91: "IXa", 92: "IXb", 93: "IXc", 101: "Xa", 102: "Xb", 103: "Xc",
            111: "XIa", 112: "XIb", 113: "XIc", 121: "XIIa", 122: "XIIb", 123: "XIIc",
            130: "XIIIa", 151: "1", 152: "2", 153: "3", 154: "4"
        }
        return difficulty_mapping.get(valueInt, "")
    
    @staticmethod
    def from_value(valueInt):
        # Returns EnumSachsenSchwierigkeitsGrad based on int value
        value_mapping = {
            10: EnumSachsenSchwierigkeitsGrad.I, 20: EnumSachsenSchwierigkeitsGrad.II, 30: EnumSachsenSchwierigkeitsGrad.III,
            40: EnumSachsenSchwierigkeitsGrad.IV, 50: EnumSachsenSchwierigkeitsGrad.V, 60: EnumSachsenSchwierigkeitsGrad.VI,
            71: EnumSachsenSchwierigkeitsGrad.VIIa, 72: EnumSachsenSchwierigkeitsGrad.VIIb, 73: EnumSachsenSchwierigkeitsGrad.VIIc,
            81: EnumSachsenSchwierigkeitsGrad.VIIIa, 82: EnumSachsenSchwierigkeitsGrad.VIIIb, 83: EnumSachsenSchwierigkeitsGrad.VIIIc,
            91: EnumSachsenSchwierigkeitsGrad.IXa, 92: EnumSachsenSchwierigkeitsGrad.IXb, 93: EnumSachsenSchwierigkeitsGrad.IXc,
            101: EnumSachsenSchwierigkeitsGrad.Xa, 102: EnumSachsenSchwierigkeitsGrad.Xb, 103: EnumSachsenSchwierigkeitsGrad.Xc,
            111: EnumSachsenSchwierigkeitsGrad.XIa, 112: EnumSachsenSchwierigkeitsGrad.XIb, 113: EnumSachsenSchwierigkeitsGrad.XIc,
            121: EnumSachsenSchwierigkeitsGrad.XIIa, 122: EnumSachsenSchwierigkeitsGrad.XIIb, 123: EnumSachsenSchwierigkeitsGrad.XIIc,
            130: EnumSachsenSchwierigkeitsGrad.XIIIa, 151: EnumSachsenSchwierigkeitsGrad.Sprung1,
            152: EnumSachsenSchwierigkeitsGrad.Sprung2, 153: EnumSachsenSchwierigkeitsGrad.Sprung3,
            154: EnumSachsenSchwierigkeitsGrad.Sprung4
        }
        return value_mapping.get(valueInt, None)
    
    @staticmethod
    def from_scale_ordinal(rangeSliderValue):
        # Returns EnumSachsenSchwierigkeitsGrad based on ordinal scale value
        ordinal_mapping = {
            1: EnumSachsenSchwierigkeitsGrad.I, 2: EnumSachsenSchwierigkeitsGrad.II, 3: EnumSachsenSchwierigkeitsGrad.III,
            4: EnumSachsenSchwierigkeitsGrad.IV, 5: EnumSachsenSchwierigkeitsGrad.V, 6: EnumSachsenSchwierigkeitsGrad.VI,
            7: EnumSachsenSchwierigkeitsGrad.VIIa, 8: EnumSachsenSchwierigkeitsGrad.VIIb, 9: EnumSachsenSchwierigkeitsGrad.VIIc,
            10: EnumSachsenSchwierigkeitsGrad.VIIIa, 11: EnumSachsenSchwierigkeitsGrad.VIIIb, 12: EnumSachsenSchwierigkeitsGrad.VIIIc,
            13: EnumSachsenSchwierigkeitsGrad.IXa, 14: EnumSachsenSchwierigkeitsGrad.IXb, 15: EnumSachsenSchwierigkeitsGrad.IXc,
            16: EnumSachsenSchwierigkeitsGrad.Xa, 17: EnumSachsenSchwierigkeitsGrad.Xb, 18: EnumSachsenSchwierigkeitsGrad.Xc,
            19: EnumSachsenSchwierigkeitsGrad.XIa, 20: EnumSachsenSchwierigkeitsGrad.XIb, 21: EnumSachsenSchwierigkeitsGrad.XIc,
            22: EnumSachsenSchwierigkeitsGrad.XIIa, 23: EnumSachsenSchwierigkeitsGrad.XIIb, 24: EnumSachsenSchwierigkeitsGrad.XIIc,
            25: EnumSachsenSchwierigkeitsGrad.XIIIa, 26: EnumSachsenSchwierigkeitsGrad.Sprung1,
            27: EnumSachsenSchwierigkeitsGrad.Sprung2, 28: EnumSachsenSchwierigkeitsGrad.Sprung3,
            29: EnumSachsenSchwierigkeitsGrad.Sprung4
        }
        return ordinal_mapping.get(rangeSliderValue, None)
