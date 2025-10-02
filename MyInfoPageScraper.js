//let mdivs = document.getElementById("reactele").
//getElementsByTagName("div")[2].getElementsByTagName("ul")[0].getElementsByTagName("li");
function valIsNullOrUndefined(val) { return (val === null || val === undefined); }
function valIsEmptyNullOrUndefined(val)
{
    return (this.valIsNullOrUndefined(val) || val.length < 1);
}
function valMustNotBeNullOrUndefined(val, varnm="varnm")
{
    if (this.valIsEmptyNullOrUndefined(varnm))
    {
        return this.valMustNotBeNullOrUndefined(val, "varnm");
    }
    const merrmsg = "" + varnm + " must not be null or undefined, but it was!";
    if (this.valIsNullOrUndefined(val)) throw new Error(merrmsg);
    else return true;
}
function valMustNotBeEmptyOrNull(val, varnm="varnm")
{
    if (this.valIsEmptyNullOrUndefined(varnm)) return this.valMustNotBeEmptyOrNull(val, "varnm");
    const merrmsg = "" + varnm + " must not be empty, undefined, or null, but it was!";
    if (this.valIsEmptyNullOrUndefined(val)) throw new Error(merrmsg);
    else return true;
}

function myIsDigit(mc)
{
    return (mc === '0' || mc === '1' || mc === '2' || mc === '3' || mc === '4' ||
          mc === '5' || mc === '6' || mc === '7' || mc === '8' || mc === '9');
}

//the times themselves are AM PM and not military... (might need converted)...
//00 is midnight 12 AM; 01 is 1 AM, ... 11 is 11 AM. 12 is 12 PM,
//13 = 1 PM, 14 = 2, 15 = 3, 16 = 4, ... 23 is 11 PM. Basically if PM add 12.
//if AM it is as is except for 12 AM that becomes 0.
function convertAMPMToMilitaryTime(tmstr)
{
    //the specific time string is going to be formatted #or##:## AM/PM
    //12 AM is 00:00 on military time otherwise AM is not converted...
    //12 PM stays as is but 1 to 12 not including 12 add 12 to it...
    //assume the time string is in uppercase and the correct format...
    //1 AM is the shortest valid time string with 4 characters...
    //12:00 PM is the longest valid time string with 8 characters...
    this.valMustNotBeEmptyOrNull(tmstr, "tmstr");
    const merrmsga = "the time string was either too short or too long!";
    const merrmsgb = "THE STRING MUST HAVE AM OR PM ON IT AND IT CANNOT HAVE BOTH!";
    
    let clnfnd = false;
    let clni = -1;
    if (tmstr.length < 4 || 8 < tmstr.length) throw new Error(merrmsga);
    else
    {
        let spcfnd = false;
        let afnd = false;
        let pfnd = false;
        let mfnd = false;
        let nmdgts = 0;
        for (let i = 0; i < tmstr.length; i++)
        {
            if (this.myIsDigit(tmstr.charAt(i)) && !mfnd && nmdgts < 2)
            {
                if (nmdgts < 0) throw new Error("numdgts must be at least zero!");
                else nmdgts++;
            }
            else if (tmstr.charAt(i) === ':' && !clnfnd && !mfnd&& 0 < i)
            {
                clnfnd = true;
                clni = i;
                nmdgts = 0;
            }
            else if (tmstr.charAt(i) === ' ' && !mfnd && !spcfnd && 0 < i) spcfnd = true;
            else if (((tmstr.charAt(i) === 'A') || (tmstr.charAt(i) === 'P')) && !mfnd &&
                !afnd && !pfnd && 0 < i && (tmstr.charAt(i - 1) === ' '))
            {
                if (tmstr.charAt(i) === 'A') afnd = true;
                else pfnd = true;
            }
            else if (tmstr.charAt(i) === 'M' && !mfnd && 0 < i &&
                ((afnd && tmstr.charAt(i - 1) === 'A') || (pfnd && tmstr.charAt(i - 1) === 'P')))
            {
                mfnd = true;
            }
            else throw new Error("illegal character found in the time string at i = " + i + "!");
        }//end of i for loop
    }

    const ami = tmstr.indexOf(" AM");
    const pmi = tmstr.indexOf(" PM");
    const isnoam = (ami < 0 || tmstr.length - 3 < ami);
    const isnopm = (pmi < 0 || tmstr.length - 3 < pmi);
    if (isnoam === isnopm) throw new Error(merrmsgb);
    
    //need to get the hour num
    //use the colon if we have one to get the hour num
    //if we do not have a colon but we use the ami or pmi
    const ei = (clnfnd ? clni : (isnoam ? pmi: ami));
    const hrnum = Number(tmstr.substring(0, ei));
    const finhrnum = ((isnoam && hrnum < 12) ? hrnum + 12 :
        ((isnoam && hrnum === 12) ? 12 : ((isnopm && hrnum < 12) ? hrnum : 0)));
    return "" + finhrnum + (clnfnd ? tmstr.substring(clni, (isnoam ? pmi: ami)): "");
}

function testCNVTimeStr()
{
    console.log(this.convertAMPMToMilitaryTime("12 AM"));//0
    console.log(this.convertAMPMToMilitaryTime("1 AM"));//1
    console.log(this.convertAMPMToMilitaryTime("11 AM"));//11
    console.log(this.convertAMPMToMilitaryTime("12:01 AM"));//0:01
    console.log(this.convertAMPMToMilitaryTime("12 PM"));//12
    console.log(this.convertAMPMToMilitaryTime("4 PM"));//16
    console.log(this.convertAMPMToMilitaryTime("4:30 PM"));//16:30
}

function myGetElementsByTagNameList(domnode, tagnm)
{
    if (this.valIsNullOrUndefined(domnode) || this.valIsNullOrUndefined(domnode.children))
    {
        return null;
    }
    let mytpnds = [];
    for (let i = 0; i < domnode.children.length; i++)
    {
        let mkid = domnode.children[i];
        if (mkid.tagName.toUpperCase() === tagnm) mytpnds.push(mkid);
    }
    return mytpnds;
}

let myrelcntnr = document.getElementById("reactele");
let myrelcntnrdivs = this.myGetElementsByTagNameList(myrelcntnr, "DIV");
let mylistcntnr = myrelcntnrdivs[2].children[0];
let mylis = this.myGetElementsByTagNameList(mylistcntnr, "LI");
mylis.forEach((myli) => {
    let mydircardcntnr = myli.children[0];//dircard div...
    let mydircntnrdivs = this.myGetElementsByTagNameList(mydircardcntnr, "DIV");
    let hrstbldiv = mydircntnrdivs[0].children[0];
    console.log(hrstbldiv);
    //inside the hrstbldiv are 7 row divs for the days of the week
    //inside that is a span for the day name and another span as a time container.
    //that span container contains x number of spans... with the intervals as the textContent.
    //the times themselves are AM PM and not military... (might need converted)...
    //00 is midnight 12 AM; 01 is 1 AM, ... 11 is 11 AM. 12 is 12 PM,
    //13 = 1 PM, 14 = 2, 15 = 3, 16 = 4, ... 23 is 11 PM. Basically if PM add 12.
    //if AM it is as is except for 12 AM that becomes 0.
    
    //assume that hrstbldiv.children.length is 7
    //0 Sunday, 1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday
    if (hrstbldiv.children.length === 7);
    else throw new Error("the day container must have 7 kids for 7 days in the week!");
    for (let n = 0; n < hrstbldiv.children.length; n++)
    {
        //each row div kid
        let mdaydiv = hrstbldiv.children[n];
        let hrsdaycntnr = mdaydiv.children[1];
        for (let k = 0; k < hrsdaycntnr.children.length; k++)
        {
            let hrintrvalspn = hrsdaycntnr.children[k];
            //console.log(hrintrvalspn);
            console.log("dayi = n = " + n);
            console.log(hrintrvalspn.textContent);
            
            let delimi = hrintrvalspn.textContent.indexOf(" - ");
            let hrstra = hrintrvalspn.textContent.substring(0, delimi);
            let hrstrb = hrintrvalspn.textContent.substring(delimi + 3);
            let fintima = this.convertAMPMToMilitaryTime(hrstra);
            let fintimb = this.convertAMPMToMilitaryTime(hrstrb);
            //console.log("hrstra = " + hrstra);
            //console.log("hrstrb = " + hrstrb);
            console.log("fintima = " + fintima);
            console.log("fintimb = " + fintimb);
        }//end of k for loop
    }//end of n for loop

    //we can also get the other information here, the question is do we want to?
    //we need to store this information in a DB, but we also need to access that information.
    //if we are saving it to the DB we will need a building ID to associate this information
    //with a building already in the DB.
    //OR we can create the entire new DB entry here...
    //
    //but the problem is saving it hosting the DB is a problem...
    //now I can serve information from a static page hosted on something like GITHUB
    //but I cannot change the DB on GITHUB. IT COULD TELL ME THE LINK TO START WITH.
    //BUT WHERE TO SAVE OR HOST IT?
    //IF I HOST THE DB FROM LOCALHOST, I CAN FETCH ON CHROME DEVTOOLS WITHOUT CORS. 
});
