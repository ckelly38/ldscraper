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

    #actual scraper methods begin here
    @classmethod
    def getpage(cls, murl):
        if (type(murl) == str and 5 < len(murl)): pass;
        else: raise ValueError("invalid URL used here!");
        doc = BeautifulSoup(requests.get(murl).text, "html.parser");
        return doc;

    @classmethod
    def getBaseURL(cls): return "https://local.churchofjesuschrist.org/";
    @classmethod
    def getBaseUSURL(cls): return cls.getBaseURL() + "en/us/";
    
    @classmethod
    def getAllUSAStatesURLs(cls):
        baseurl = cls.getBaseUSURL();
        abbrvs = cls.getAbbreviations();
        return ["" + baseurl + abbrv + "/" for abbrv in abbrvs];
    
    #now we need to get the counties for each state
    @classmethod
    def getCountiesForStateURL(cls, sturl):
        doc = cls.getpage(sturl);
        docbody = doc.body.select("#reactele")[0].select("div")[2].select("ul")[0];
        mylis = docbody.select("li");
        #print(str(mylis));
        #print("");
        cntynms = [];
        for mli in mylis:
            mhrefurl = mli.select("a")[0]["href"];
            cntynm = mhrefurl[mhrefurl.rindex("/") + 1:];
            cntynms.append(cntynm);
            #print(cntynm);
        return cntynms;
    
    @classmethod
    def getCountyUrlFromStateAndCounty(cls, sturl, cnty):
        if (type(sturl) == str and 5 < len(sturl)): pass;
        else: raise ValueError("invalid state URL used here!");
        if (type(cnty) == str and 0 < len(cnty)): pass;
        else: raise ValueError("invalid county used here!");
        return "" + sturl + "/" + cnty + "/";

    @classmethod
    def myStripText(cls, val):
        if (val == None): return "";
        else:
            if (type(val) == str): return val.strip();
            else: raise ValueError("the val must be a string!");

    #now on each county we need to get the information from the cards...
    #NOT DONE YET NEED TO SOMEHOW SAVE THE DATA...
    @classmethod
    def getInfoFromCounty(cls, cntyurl):
        doc = cls.getpage(cntyurl);
        docbody = doc.body.select("#reactele")[0].select("div")[2].select("ul")[0];
        mylis = docbody.select("li");
        #print(str(mylis));
        #print("");
        for mli in mylis:
            mncntnr = mli.select("div")[0];#DirectoryCard
            cntynm = mncntnr.select("h3")[0].select("a")[0].select("div")[1].text;
            print(mncntnr);
            print("cntynm = " + cntynm);
            #we could get the hours, but there are different hours on the days
            #so maybe skip that for now
            #hrscntnr = mncntnr.select("div")[0];
            #print("");
            #print(dir(mncntnr));#lists object methods and attributes
            
            #name returns the tag name
            #children gets the child elements of an HTML node or tag
            mcntnrdivs = [kid for kid in mncntnr.children if kid.name == "div"];
            print("the container has " + str(len(mcntnrdivs)) + " div(s):");
            for mdivobj in mcntnrdivs: print(mdivobj);
            print("");
            #print(mcntnrdivs[1]);
            #print(mli.select("div")[0].select("div")[1]);#selects something wrong
            
            #get the address and its container here
            addrcntnr = mcntnrdivs[1].select("div")[0];
            #print(addrcntnr);

            strt = cls.myStripText(addrcntnr.select("div")[0].select("span")[0].text);
            cty = cls.myStripText(addrcntnr.select("div")[2].select("span")[0].text);
            st = cls.myStripText(addrcntnr.select("div")[2].select("span")[2].text);
            zp = cls.myStripText(addrcntnr.select("div")[2].select("span")[3].text);
            print("strt = " + strt);
            print("cty = " + cty);
            print("st = " + st);
            print("zp = " + zp);

            #telephone number
            telcntnr = mcntnrdivs[2].select("a")[0];
            telnumstr = telcntnr["href"];#includes tel+ so may want to strip
            teltxt = cls.myStripText(telcntnr.text);
            print("teltxt = " + teltxt);
            print("telnumstr = " + telnumstr);

            #need the maps url
            mpsurlcntnr = mcntnrdivs[3].select("a")[0];
            mpsurltxt = mpsurlcntnr["href"]; 
            #print(mpsurlcntnr);
            print("mpsurltxt = " + mpsurltxt);
        print("");
        raise ValueError("NOT DONE YET 9-22-2025 3:45 AM MST!");

if (__name__ == '__main__'):
    print("states = " + str(MyScraper.getStates()));
    print("abbrvs = " + str(MyScraper.getAbbreviations()));
    print("both = " + str(MyScraper.getStateNameAndAbreviationsObjects()));
    baseurl = MyScraper.getBaseUSURL();
    print("base url = " + baseurl);
    #countries -> USA ->
    #states -> CO ->
    #county -> denver
    #
    #everywhere else:
    #country -> ? ->
    #county -> ? ->
    #city -> ?
    print("all state urls = " + str(MyScraper.getAllUSAStatesURLs()));
    print("");
    #print("cnties = " + str(MyScraper.getCountiesForStateURL(baseurl + "co")));
    print("info = " + str(MyScraper.getInfoFromCounty(baseurl + "co/denver/")));
