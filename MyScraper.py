from bs4 import BeautifulSoup;
import requests;
class MyScraper:
    @classmethod
    def getStateNameAndAbreviationsObjects(cls):
        return [{"state": "Alabama", "abbreviation": "al"},
            {"state": "Alaska", "abbreviation": "ak"},
            {"state": "Arizona", "abbreviation": "az"},
            {"state": "Arkansas", "abbreviation": "ar"},
            {"state": "California", "abbreviation": "ca"},
            {"state": "Colorado", "abbreviation": "co"},
            {"state": "Connecticut", "abbreviation": "ct"},
            {"state": "Delaware", "abbreviation": "de"},
            {"state": "Florida", "abbreviation": "fl"},
            {"state": "Georgia", "abbreviation": "ga"},
            {"state": "Hawaii", "abbreviation": "hi"},
            {"state": "Idaho", "abbreviation": "id"},
            {"state": "Illinois", "abbreviation": "il"},
            {"state": "Indiana", "abbreviation": "in"},
            {"state": "Iowa", "abbreviation": "ia"},
            {"state": "Kansas", "abbreviation": "ks"},
            {"state": "Kentucky", "abbreviation": "ky"},
            {"state": "Louisiana", "abbreviation": "la"},
            {"state": "Maine", "abbreviation": "me"},
            {"state": "Maryland", "abbreviation": "md"},
            {"state": "Massachusetts", "abbreviation": "ma"},
            {"state": "Michigan", "abbreviation": "mi"},
            {"state": "Minnesota", "abbreviation": "mn"},
            {"state": "Mississippi", "abbreviation": "ms"},
            {"state": "Missouri", "abbreviation": "mo"},
            {"state": "Montana", "abbreviation": "mt"},
            {"state": "Nebraska", "abbreviation": "ne"},
            {"state": "Nevada", "abbreviation": "nv"},
            {"state": "New Hampshire", "abbreviation": "nh"},
            {"state": "New Jersey", "abbreviation": "nj"},
            {"state": "New Mexico", "abbreviation": "nm"},
            {"state": "New York", "abbreviation": "ny"},
            {"state": "North Carolina", "abbreviation": "nc"},
            {"state": "North Dakota", "abbreviation": "nd"},
            {"state": "Ohio", "abbreviation": "oh"},
            {"state": "Oklahoma", "abbreviation": "ok"},
            {"state": "Oregon", "abbreviation": "or"},
            {"state": "Pennsylvania", "abbreviation": "pa"},
            {"state": "Rhode Island", "abbreviation": "ri"},
            {"state": "South Carolina", "abbreviation": "sc"},
            {"state": "South Dakota", "abbreviation": "sd"},
            {"state": "Tennessee", "abbreviation": "tn"},
            {"state": "Texas", "abbreviation": "tx"},
            {"state": "Utah", "abbreviation": "ut"},
            {"state": "Vermont", "abbreviation": "vt"},
            {"state": "Virginia", "abbreviation": "va"},
            {"state": "Washington", "abbreviation": "wa"},
            {"state": "Washington DC", "abbreviation": "dc"},
            {"state": "West Virginia", "abbreviation": "wv"},
            {"state": "Wisconsin", "abbreviation": "wi"},
            {"state": "Wyoming", "abbreviation": "wy"}];
    
    @classmethod
    def getNameForAbbreviationOrAbbreviationForState(cls, val, usestate=True):
        if (type(usestate) == bool): pass;
        else: raise ValueError("usestate must be a bool!");
        snmsobjs = cls.getStateNameAndAbreviationsObjects();
        for mobj in snmsobjs:
            if (mobj[("state" if usestate else "abbreviation")] == val):
                return mobj[("abbreviation" if usestate else "state")];
        raise ValueError("Invalid " + ("State" if usestate else "Abbreviation") + " name (" +
            val + ")!");
    @classmethod
    def getAbbreviationForName(cls, val):
        return cls.getNameForAbbreviationOrAbbreviationForState(val, usestate=True);
    @classmethod
    def getNameForAbbreviation(cls, val):
        return cls.getNameForAbbreviationOrAbbreviationForState(val, usestate=False);

    @classmethod
    def getStatesOrAbbreviations(cls, usestate=True):
        if (type(usestate) == bool): pass;
        else: raise ValueError("usestate must be a bool!");
        snmsobjs = cls.getStateNameAndAbreviationsObjects();
        return [mobj[("state" if usestate else "abbreviation")] for mobj in snmsobjs];
    @classmethod
    def getStates(cls): return cls.getStatesOrAbbreviations(usestate=True);
    @classmethod
    def getAbbreviations(cls): return cls.getStatesOrAbbreviations(usestate=False);

if (__name__ == '__main__'):
    print("states = " + str(MyScraper.getStates()));
    print("abbrvs = " + str(MyScraper.getAbbreviations()));
    print("both = " + str(MyScraper.getStateNameAndAbreviationsObjects()));
