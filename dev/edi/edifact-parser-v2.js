/*====================================================
  Edifact parser for S2000M Chapter 1A
  Author: rey.olivier@gmail.com
  Date: November 2025
 ====================================================*/

//========================================= Constants
//end of segment
const EOS = "'";
//data element separator
const DES = "+";
//data element data separator
const DAT = ":"

// Constants for data element identification in grammar
const DATA_ELEMENT = 1;
const COMPOSITE = 2;
const COMPOSITE_DATA_ELEMENT = 3;


//========================================= Utils
// Warning: the space is not a regular alphanumeric character!
function isAlphaNumeric(str) {
    //return str.match(/^[a-z0-9]+$/i) !== null;
    return str.match(/^[\w\-\s]+$/) != null
}

function isAlpha(str) {
  return str.match(/^[a-z]+$/i) !== null;
}

function isNumeric(str) {
  return str.match(/^[0-9]+$/i) !== null;
}

function testStrings(){
    testcases = [
        "123456",
        "AzertuiopZZ",
        "12azerY",
        "_gsf-'",
        "kgshfs%$£",
        "Le vierge le vivace et le bel aujourd'hui",
        "Le vierge le vivace et le bel aujourd hui"
    ];
    for (let test of testcases) {
        console.log("Test case for '" + test + "'");
        console.log("isAlphaNumeric? " + isAlphaNumeric(test));
        console.log("isNumeric? " + isNumeric(test));
        console.log("isAlpha? " + isAlpha(test));
    }
}


//========================================= Dictionary of Data elements
const ELEMS = {
    "ADD": [DATA_ELEMENT, "ADD","ADDRESSEE","an5"],
    "ASP": [DATA_ELEMENT, "ASP","ATTACHING, STORAGE OR SHIPPING PART","n1"],
    "CAN": [DATA_ELEMENT, "CAN","CHANGE AUTHORITY NUMBER","an20"],
    "CHG": [DATA_ELEMENT, "CHG","CHANGE CODE","an1"],
    "CRT": [DATA_ELEMENT, "CRT","CONTRACTOR REPAIR TURNAROUND TIME","n3"],
    "CMK": [DATA_ELEMENT, "CMK","CALIBRATION MARKER","n1"],
    "CSN": [DATA_ELEMENT, "CSN","CATALOGUE SEQUENCE NUMBER","an13"],
    "CSR": [DATA_ELEMENT, "CRS","CONSUMPTION RATE","n3"],
    "CTL": [DATA_ELEMENT, "CTL","CATEGORY 1 CONTAINER LOCATION","an7"],
    "DFL": [DATA_ELEMENT, "DFL","DESCRIPTION FOR LOCATION","an130"],
    "DFP": [DATA_ELEMENT, "DFP","DESCRIPTION FOR PART","an130"],
    "DMC": [DATA_ELEMENT, "DMC","DOMESTIC MANAGEMENT CODE","an6"],
    "DRD": [DATA_ELEMENT, "DRD","DATA RELEASE DATE","n6"],
    "DRR": [DATA_ELEMENT, "DRR","DATA RELEASE REFERENCE","an8"],
    "DRS": [DATA_ELEMENT, "DRS","DATA RELEASE SEQUENCE NUMBER","n3"],
    "EFY": [DATA_ELEMENT, "EFY","EFFECTIVITY","an8"],
    "ESC": [DATA_ELEMENT, "ESC","ESSENTIALITY CODE","n1"],
    "ESD": [DATA_ELEMENT, "ESD","ELECTROSTATIC SENSITIVE DEVICE","n1"],
    "FID": [DATA_ELEMENT, "FID","FILE IDENTIFIER","a1"],
    "FTC": [DATA_ELEMENT, "FTC","FITMENT CODE","an1"],
    "HAZ": [DATA_ELEMENT, "HAZ","HAZARDOUS MATERIAL","an4"],
    "IAI": [DATA_ELEMENT, "IAI","ILLUSTRATION AFFECTED INDICATOR","a1"],
    "ICY": [DATA_ELEMENT, "ICY","INTERCHANGEABILITY","an2"],
    "ILS": [DATA_ELEMENT, "ILS","INTEGRATED LOGISTIC SUPPORT NUMBER","an20"],
    "INC": [DATA_ELEMENT, "INC","ITEM NAME CODE","an5"],
    "IND": [DATA_ELEMENT, "IND","INDENTURE","n1"],
    "IPP": [DATA_ELEMENT, "IPP","INITIAL PROVISIONING PROJECT NUMBER","an9"],
    "IPS": [DATA_ELEMENT, "IPS","INITIAL PROVISIONING PROJECT NUMBER SUBJECT","an19"],
    "ISN": [DATA_ELEMENT, "ISN","ITEM SEQUENCE NUMBER","an3"],
    "ISS": [DATA_ELEMENT, "ISS","ISSUE STANDARD","an2"],
    "LGE": [DATA_ELEMENT, "LGE","LANGUAGE CODE","a2"],
    "MAP": [DATA_ELEMENT, "MAP","MAINTENANCE PERCENT","n2"],
    "MFC": [DATA_ELEMENT, "MFC","NATO SUPPLY CODE FOR MANUFACTURERS","an5"],
    "MFM": [DATA_ELEMENT, "MFM","SELECT OR MANUFACTURE FROM RANGE","an40"],
    "MOI": [DATA_ELEMENT, "MOI","MODEL IDENTIFICATION","an2"],
    "MOV": [DATA_ELEMENT, "MOV","MODEL VERSION","an2"],
    "MTP": [DATA_ELEMENT, "MTP","MESSAGE TYPE","an6"],
    "NIL": [DATA_ELEMENT, "NIL","NOT ILLUSTRATED","an1"],
    "OBS": [DATA_ELEMENT, "OBS","OBSERVATION","an130"],
    "OSN": [DATA_ELEMENT, "OSN","OBSERVATION SEQUENCE NUMBER","n1"],
    "PCD": [DATA_ELEMENT, "PCD","PROCUREMENT CODE","an2"],
    "PIC": [DATA_ELEMENT, "PIC","POOL ITEM CANDIDATE","n1"],
    "PLC": [DATA_ELEMENT, "PLC","PACKAGING LEVEL CODE","an1"],
    "PLT": [DATA_ELEMENT, "PLT","PURCHASING LEAD TIME","n2"],
    "PNR": [DATA_ELEMENT, "PNR","PART NUMBER","an32"],
    "PSC": [DATA_ELEMENT, "PSC","PHYSICAL SECURITY/PILFERAGE CODE","an1"],
    "QNA": [DATA_ELEMENT, "QNA","QUANTITY PER NEXT HIGHER ASSEMBLY","an4"],
    "QUI": [DATA_ELEMENT, "QUI","QUANTITY PER UNIT OF ISSUE","n4"],
    "RFD": [DATA_ELEMENT, "RFD","REFERENCE DESIGNATOR","an7"],
    "RFS": [DATA_ELEMENT, "RFS","REASON FOR SELECTION","n1"],
    "RMF": [DATA_ELEMENT, "RMF","REPLACING NATO SUPPY CODE FOR MANUFACTURERS","an5"],
    "RMQ": [DATA_ELEMENT, "RMQ","RECOMMENDED MAINTENANCE QUANTITY","n5"],
    "RNC": [DATA_ELEMENT, "RNC","REFERENCE NUMBER CATEGORY CODE","an1"],
    "RNJ": [DATA_ELEMENT, "RNV","REFERENCE NUMBER JUSTIFICATION CODE","n1"],
    "RNV": [DATA_ELEMENT, "RNV","REFERENCE NUMBER VARIATION CODE","n1"],
    "RPP": [DATA_ELEMENT, "RPP","REPLACING PART NUMBER","an32"],
    "ROQ": [DATA_ELEMENT, "ROQ","RECOMMENDED OVERHAUL REPAIR QUANTITY","n5"],
    "RTX": [DATA_ELEMENT, "RTX","REFER TO","an16"],
    "SLC": [DATA_ELEMENT, "SLC","SHELF LIFE CODE","an1"],
    "SMF": [DATA_ELEMENT, "SMF","SELECT OR MANUFACTURE FROM IDENTIFIER","a1"],
    "SMR": [DATA_ELEMENT, "SMR","SOURCE MAINTENANCE RECOVERABILITY","an6"],
    "SPC": [DATA_ELEMENT, "SPC","SPARE PARTS CLASSIFICATION","n1"],
    "SPU": [DATA_ELEMENT, "SPU","SIZE OF PACKAGED UNIT","an14"],
    "SPQ": [DATA_ELEMENT, "SPQ","STANDARD PACKAGE QUANTITY","n4"],
    "SRA": [DATA_ELEMENT, "SRA","SCRAP RATE","n2"],
    "SRV": [DATA_ELEMENT, "SRV","SERVICE","an3"],
    "STR": [DATA_ELEMENT, "STR","SPECIAL STORAGE","n1"],
    "SUU": [DATA_ELEMENT, "SUU","SIZE OF UNPACKAGED UNIT","an14"],
    "TLF": [DATA_ELEMENT, "TLF","TOTAL LIFE","n3"],
    "TQL": [DATA_ELEMENT, "TQL","TOTAL QUANTITY PER LOCATION","an5"],
    "TOD": [DATA_ELEMENT, "TOD","TRANSMITTER OF DATA","an5"],
    "TOP": [DATA_ELEMENT, "TOP","TYPE OF PRICE","an2"],
    "TQY": [DATA_ELEMENT, "TQY","TOTAL QUANTITY","an5"],
    "UCA": [DATA_ELEMENT, "UCA","USABLE ON CODE ASSEMBLY","an6"],
    "UCE": [DATA_ELEMENT, "UCE","USABLE ON CODE EQUIPMENT","an8"],
    "UOI": [DATA_ELEMENT, "UOI","UNIT OF ISSUE","a2"],
    "UOM": [DATA_ELEMENT, "UOM","UNIT OF MEASURE","a2"],
    "WPU": [DATA_ELEMENT, "WPU","WEIGHT OF PACKAGED UNIT","an7"],
    "WUU": [DATA_ELEMENT, "WUU","WEIGHT OF UNPACKAGED UNIT","an7"],

    // Composites elements and composite data elements
    "aul": [COMPOSITE_DATA_ELEMENT,"aul","Authorised Life","n6"],
    "tca": [COMPOSITE_DATA_ELEMENT,"tca","Time/Cycle Indicator/AL","a2"],
    
    "ALI": ["ALI","AUTHORISED LIFE/TCIAL",["aul","tca"]],
    
    "mfc": [COMPOSITE_DATA_ELEMENT,"mfc","NATO Supply Code For Manufacturer","an5"],
    "pnr": [COMPOSITE_DATA_ELEMENT,"pnr","Part Number","an32"],
    
    "CTI": [COMPOSITE,"CTI","CATEGORY 1 CONTAINER IDENTIFICATION",["mfc","pnr"]],
    "SID": [COMPOSITE,"SID","SUBJECT IDENTIFICATION",["mfc","pnr"]],
    
    "tbf": [COMPOSITE_DATA_ELEMENT,"tbf","Mean Time Between Failures","n6"],
    "tcm": [COMPOSITE_DATA_ELEMENT,"tcm","Time/Cycle Indicator/MTBF","a2"],

    "MTI": [COMPOSITE, "MTI","MEAN TIME BETWEEN FAILURES/TCIBF",["tbf","tcm"]],

    "nsc": [COMPOSITE_DATA_ELEMENT,"nsc","NATO Supply Class","n4"],
    "nin": [COMPOSITE_DATA_ELEMENT,"nin","NATO Item Identification Number","n9"],
    
    "NSN": ["NSN","NATO STOCK NUMBER",["nsc","nin"]],
    "SNS": ["SNS","SUBJECT NATO STOCK NUMBER",["nsc","nin"]],

    "qty": [COMPOSITE_DATA_ELEMENT,"qty","Quantity","n5"],
    "upr": [COMPOSITE_DATA_ELEMENT,"upr","Unit Price","n12"],

    "PBD": [COMPOSITE,"PBD","PRICE BREAK DATA",["qty","qty","upr","qty","qty","upr","qty","qty","upr"]],

    "tbo": [COMPOSITE_DATA_ELEMENT,"tbo","Time Between Overhauls","n6"],
    "tco": [COMPOSITE_DATA_ELEMENT,"tco","Time/Cycle Indicator/TBO","a2"],

    "TBI": [COMPOSITE,"TBI","TIME BETWEEN OVERHAULS/TCIBO",["tbo","tco"]],

    "tsv": [COMPOSITE_DATA_ELEMENT,"tsv","Time Between Scheduled Shop Visits","n6"],
    "tcs": [COMPOSITE_DATA_ELEMENT,"tcs","Time/Cycle Indicator/TBSSV","a2"],

    "TSI": [COMPOSITE,"TSI","TIME BETW'N SCHED'D SHOP VISITS/TCISV",["tsv","tcs"]]
      
}

                        
/*-----------------------------------------------------------
 The segment class is supposed to be called by the segmentFactory
 *-----------------------------------------------------------*/
class Segment {
    //--- dataelements is an array
    constructor(code, sfunction, dataelements) {
        this.code = code;
        this.sfunction = sfunction;
        this.dataelements = dataelements; //array
        this.tyofsegment = "";
        this.applicability = null; //array
        this.values = null //array
    }
    //--- integrate applicability in message context
    setApplicability(typeofsegment) {
        this.typeofsegment = typeofsegment;
        let app = CONDS[typeofsegment];
        if (app.length != this.dataelements.length) {
            console.error("Inconsistent data error:"
                          + "\nStructure of segment: " + this.dataelements
                          + "\nApplicability" + app);
            return -1
        }
        this.applicability = app;
    }
    //--- getting the string of data of the segment
    setValues(chain){
        if (! chain.endsWith("'")) {
            console.error("Error: The segment string should end by the character '.");
            return -1;
        }
        let chunks = chain.substring(0,chain.length-1).split(DES);
        if (this.code != chunks[0]) {
            console.error("Data not inline with Segment type:"
                          + "\nData starting by: " + chunks[0]
                          + "\nSegment type: " + this.code);
            return -1;
        }
        let dataindex = 1; // skipping the segment name
        let deindex = 0
        // we have 3 arrays:
        // dataelements: ["IPP","MTP","ISS","TOD","ADD","FID","MOI","DRS","DRD","LGE","IPS","DRR"]
        // applicability: ["M","M","-","M","M","M","M","M","M","M","M","C"],
        // values: [to be filled if grammar is respected]
        for (let app of this.applicability) {
            switch(app) {
            case "M": //mandatory
                console.log("---")
                let fullde = chunks[dataindex].split(DAT);
                console.log("Expecting mandatory data element " + this.dataelements[deindex]
                            + "\nGetting: " + fullde[0]);
                //getting the value
                let value = fullde[1];
                console.log(fullde);
                console.log(value);
                //checking grammar compliance
                let result = checkDataElementGrammar(this.dataelements[deindex],value);
                if (result)
                    console.log("Data element is compliant with the grammar");
                else
                    console.error("Data element is not compliant with the grammar");
                deindex++;
                dataindex++;
                break;
            case "C":
                break;
            case "-":
                break;
            default:
                console.error("Grammar issue: Should not happen");
            }
            
        }
        

    }
}

   
function checkDataElementGrammar(dataelement,value) {
    /*
      Value should be a string
     */
    let elem = ELEMS[dataelement]; // elem is an array like ["ADD","ADDRESSEE","an5"]
    let gram = elem[2];
    let gtype = 0; //0 = alphanum, 1 = alpha, 2 = num
    let gsiz = 0;
    if (gram.startsWith("an")) {
        gtype = 0; //useless
        gsiz = parseInt(gram.replace("an",""));
    }
    else {
        if (gram.startsWith("a")) {
            gtype = 1;
            gsiz = parseInt(gram.replace("a",""));
        }
        else {
            if (gram.startsWith("n")){
                gtype = 2;
                gsiz = parseInt(gram.replace("n",""));
            }
            else {
                console.error("Unknown grammar pattern: " + gram);
                return -1;
            }
        }
    }
    //check length
    if (value.length > gsiz) {
        console.error("Grammar length violation. Grammar: " + gram
                      + "\nValue: " + value);
        return -1;
    }
    else
        console.log("Length of data element is compliant with the grammar")
    switch(gtype){
    case 0: //alphanum
        if (isAlphaNumeric(value)){
            console.log("Alphanumeric type compliant with the grammar")
            return true;
        }
        else {
            console.error("Error: Expecting alphanumeric type")
            return false;
        }
    case 1: //alpha
        if (isAlpha(value)){
            console.log("Alpha type compliant with the grammar")
            return true;
        }
        else {
            console.error("Error: Expecting alpha type")
            return false;
        }
    case 2:
        if (isNumeric(value)){
            console.log("Numeric type compliant with the grammar")
            return true;
        }
        else {
            console.error("Error: Expecting numeric type")
            return false;
        }
    default:
        console.error("This case should not happen!")
        return -1;
    } 
}




function segmentFactory(name) {
    // Name is expected to be 3 char for the segment name
    //+ one number for implementation
    let sname = name.substring(0,3);
    let seg = null;
    switch(sname){
    case "CAS":
        seg = new Segment("CAS","ITEM LOCATION",["CHG","CSN","ISN","IND","RFS","QNA","TQL","PNR","MFC","NSN"]);
        break;
    case "CBS":
        seg = new Segment("CBS","PART LOCATION DATA (1)",["ASP","NIL","RTX","SMF","MFM","DFL"]);
        break;
    case "CCS":
        seg = new Segment("CCS","APPLICABILITY",["UCE","UCA","ICY"]);
        break;
    case "CDS":
        seg = new Segment("CDS","PART LOCATION DATA (2)",["CTL","ESC","MAP","CSR"]);
        break;
    case "CES":
        seg = new Segment("CES","LOCATION RECOMMENDATIONS",["CHG","SRV","SMR","RMQ","ROQ"]);
        break;
    case "CFS":
        seg = new Segment("CFS","REFERENCE DESIGNATOR",["CHG","RFD"]);
        break;
    case "CGS":
        seg = new Segment("CGS","LOCATION CHANGE DATA",["IAI","CAN"]);
        break;
    case "CHS":
        seg = new Segment("CHS","LOCATION REFERENCE",["CSN"]);
        break;
    case "CIS":
        seg = new Segment("CIS","CROSS REFERENCE TO INTEGRATED LOGISTIC SUPPORT",["CHG","ILS"]);
        break;
    case "CJS":
        seg = new Segment("CJS","MODEL VERSION",["CHG","MOV"]);
        break;
    case "CKS":
        seg = new Segment("CKS","EFFECTIVITY",["CHG","EFY"]);
        break;
    case "IPH":
        seg = new Segment("IPH","HEADER",["IPP","MTP","ISS","TOD","ADD","FID","MOI","DRS","DRD","LGE","IPS","DRR"]);
        break;
    case "MAS":
        seg = new Segment("MAS","PROJECT CHANGE DATA",["CHG","IAI","CAN"]);
        break;
    case "OCS":
        seg = new Segment("OCS","LOCATION RELATED OBSERVATIONS",["CSN","ISN","OBS"]);
        break;
    case "OHS":
        seg = new Segment("OHS","PROJECT RELATED OBSERVATIONS",["OSN","OBS"]);
        break;
    case "OIS":
        seg = new Segment("OIS","ILLUSTRATION RELATED OBSERVATIONS",["CSN","OBS"]);
        break;
    case "OPS":
        seg = new Segment("OPS","PART RELATED OBSERVATIONS",["PNR","MFC","OBS"]);
        break;
    case "PAS":
        seg = new Segment("PAS","PART IDENTITY",["CHG","PNR","MFC","DFP","INC","NSN","RNC","RNV","RNJ"]);
        break;
    case "PBS":
        seg = new Segment("PBS","SPARABLE ITEM DATA",["UOI","SPQ","TOP","ITY","SPC","PLT","STR","SLC","PLC","PCD"]);
        break;
    case "PCS":
        seg = new Segment("PCS","UNIT OF ISSUE QUALIFICATION",["UOM","QUI"]);
        break;
    case "PDS":
        seg = new Segment("PDS","PRICE DATA",["UPR","CUR","MSQ","PBD"]);
        break;
    case "PES":
        seg = new Segment("PES","RELIABILITY AND MAINTAINABILITY DATA",["CRT","SRA","MTI","TBI","TSI","ALI","TLF"]);
        break;
    case "PFS":
        seg = new Segment("PFS","MISCELLANEOUS PARTS DATA",["DMC","HAZ","PIC","FTC","PSC","ESD","CMK"]);
        break;
    case "PGS":
        seg = new Segment("PGS","PHYSICAL CHARACTERISTICS",["SUU","SPU","WUU","WPU"]);
        break;
    case "PHS":
        seg = new Segment("PHS","CATEGORY I CONTAINER",["CTI"]);
        break;
    case "PIS":
        seg = new Segment("PIS","PART RECOMMENDATIONS",["CHG","SRV","TQY","RMQ","RQ"]);
        break;
    case "PJS":
        seg = new Segment("PJS","REPLACEMENT PART",["PNR","MFC","RPP","RMF"]);
        break;
    case "PKS":
        seg = new Segment("PKS","ICY 9 PART",["PNR","MFC"]);
        break;
    case "PMS":
        seg = new Segment("PMS","SUPPLY DATA",["UOI","UOM","QUI"]);
        break;
    case "VAS":
        seg = new Segment("VAS","SUBJECT VARIANT",["CHG","SID","SNS"]);
        break;
    default:
        console.error("Unknown segment: " + sname);
        return -1
    }
    seg.setApplicability(name);
    return seg;
}

CONDS = {
    "CAS1": ["M","M","M","M","M","M","M","M","M","O-MC"],
    "CAS2": ["M","M","M","C","C","C","C","C","C","O-MC"],
    "CBS1": ["C","C","C","C","C","C"],
    "CCS1": ["C","C","C"],
    "CDS1": ["C","O","C","O"],
    "CES1": ["M","M","M","C","C"],
    "CES2": ["M","M","C","C","C"],
    "CFS1": ["M","M"],
    "CGS1": ["M","M"],
    "CGS2": ["C","C"],
    "CHS1": ["M"],
    "CIS1": ["M","M"],
    "CJS1": ["M","M"],
    "CKS1": ["M","M"],
    "IPH1": ["M","M","M","M","M","M","M","M","M","M","M","-"],
    "IPH2": ["M","M","-","M","M","M","M","M","M","M","M","C"],
    "IPH3": ["M","M","-","M","M","M","M","M","M","M","M","-"],
    "MAS1": ["M","M","M"],
    "MAS2": ["M","-","M"],
    "OCS1": ["M","M","M"],
    "OHS1": ["M","M"],
    "OIS1": ["M","M"],
    "OPS1": ["M","M","M"],
    "PAS1": ["M","M","M","M","C","C-MC","C","C","C"],
    "PAS2": ["M","M","M","M","M","M-MC","C","C","C"],
    "PAS3": ["M","M","M","C","C","C-CC","C","C","C"],
    "PAS4": ["M","M","M","-","-","-","-","-","-"],
    "PBS1": ["M","M","C","M","M","M","M","C","C","M"],
    "PBS2": ["M","M","M","M","M","M","M","M","M","M"],
    "PBS3": ["C","C","C","C","C","C","C","C","C","C"],
    "PCS1": ["M","M"],
    "PCS2": ["C","C"],
    "PDS1": ["M","M","C","C-MMMCCCCCC"],
    "PDS2": ["C","C","C","C-MMMCCCCCC"],
    "PES1": ["C","C","C-MM","C-MM","C-MM","C-MM","C"],
    "PES2": ["C","C","C-CC","C-CC","C-CC","C-CC","C"],
    "PFS1": ["C","C","O","C","O","C","O"],
    "PGS1": ["O","O","O","O"],
    "PHS1": ["M","M","M"],
    "PHS2": ["M","C","C"],
    "PIS1": ["M","M","M","C","C"],
    "PIS2": ["M","M","C","C","C"],
    "PJS1": ["M","M","M","M"],
    "PKS1": ["M","M"],
    "PMS1": ["M","C","C"],
    "VAS1": ["M","M-MM","C-MM"],
    "VAS2": ["M","M-MM","C-CC"]
}

// UPIPCO structures
const UPIPCO_GROUP4 = {
    "CJS1": "M1",
    "CKS1": "C99"
}

const UPIPCO_GROUP3 = {
    "CES2": "M1",
    "GROUP4": "C9"
}

const UPIPCO_GROUP1 = {
    "CAS2": "M1",
    "CBS1": "C1",
    "CCS1": "C1",
    "CDS1": "C1",
    "GROUP3": "C10",
    "CFS1": "C100",
    "CGS1": "C1",
    "CIS1": "C120"
}

const UPIPCO_GROUP2 = {
    "PAS3": "M1",
    "PBS3": "C1",
    "PCS2": "C1",
    "PDS2": "C1",
    "PES2": "C1",
    "PFS1": "C1",
    "PGS1": "C1"
}

const UPIPCO = {
    "IPH1": "M1",
    "VAS2": "C8",
    "OHS1": "C5",
    "MAS1": "M20",
    "GROUP1": "C100000",
    "GROUP2": "C10000"
}


/*
function checkDataElement(name,structure,applicability,data) {
    let tab = data.split(DAT);
    if (tab[0] != name){
        console.error("Data element name is incorrect. Expecting: "
                      + name + ", getting: " + tab[0]);
        return -1;
    }
    if (structure.length != applicability.length) {
        console.error("Inconsistent data error.\n"
                      + "Structure: " + structure
                      + "\nApplicability" + applicability);
        return -1;
    }
    

}*/



const testline = "IPH+IPP:A0126X001+MTP:UPIPCO+ISS:M1+TOD:FA2A5+ADD:5355B+FID:S+MOI:JA+DRS:010+DRD:171125+LGE:UK+IPS:HYDRAULIC POWER'";

let iph = segmentFactory("IPH1");
console.log(iph);
iph.setValues(testline);

testStrings();

