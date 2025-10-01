//let mdivs = document.getElementById("reactele").
//getElementsByTagName("div")[2].getElementsByTagName("ul")[0].getElementsByTagName("li");
function valIsNullOrUndefined(val) { return (val === null || val === undefined); }
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
    //
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
});
