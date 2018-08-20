import csv, sys, getopt, calendar

#--------------------------------------
#-- Constants
#--------------------------------------
class CONSTANTS:
    """
    Defining constants for the module
    """
    CARRIER = 'ANL'
    SOURCE = 'DIVA'
    operatorCode2ShipCompCodeMap = {'CMA': '0001', 'ANL' : '0002', 'CNC' : '0003', 'MDV': '0004'}
    shipCompCode2OperatorCodeMap = {'0001' : 'CMA', '0002' : 'ANL', '0003' : 'CNC', '0004' : 'MDV'}

#--------------------------------------
#-- operatorCode2ShipCompCode
#--------------------------------------
def operatorCode2ShipCompCode(opcode):
    try:
        shipCompCode = CONSTANTS.operatorCode2ShipCompCodeMap[opcode]
    except KeyError:
        print "Unknown Operator Code in data file. Please add mapping to carrierMap."
        print "Exiting"
        sys.exit()
    return shipCompCode

#--------------------------------------
#-- shipCompCode2OperatorCode
#--------------------------------------
def shipCompCode2OperatorCode(sccode):
    try:
        opcode = CONSTANTS.shipCompCode2OperatorCodeMap[sccode]
    except KeyError:
        print "Unknown Ship Comp Code in data file:. Please add mapping to carrierMap."
        print "Exiting"
        sys.exit()
    return opcode

#--------------------------------------
#-- IntragroupContainer
#--------------------------------------
class IntragroupContainer:
    """
    Root class for intragroupe containers.
    """
    def __init__(self, row):
        self.row = row
        self.key = None
        self.invoicingElements = None
    def printRow(self):
        print self.row
    def getKey(self):
        return self.key
    def getInvoicingElements(self):
        return self.invoicingElements
    def getMMALineFormat(self, currency, price):
        return

#--------------------------------------
#-- IntragroupContainerBayplan
#--------------------------------------
class IntragroupContainerBayplan(IntragroupContainer):
    """
    This class is containing a mapping of the POO002 report fields.
    """
    def __init__(self, row):
        self.row = row
        self.BookingNumber = row[0]
        self.LoadDate = row[1]
        self.BLNumber = row[2]
        self.ContainerNumber = row[3]
        self.ContainerSizeType = row[4]
        self.ISOCode = row[5]
        self.CommercialVoyageNumber = row[6]
        self.OperationalVoyageNumber = row[7]
        self.PointLoad = row[8]
        self.PointDish = row[9]
        self.OperatorCode = row[10]
        self.Weight = row[11]
        self.ReeferFlag = row[12]
        self.HazardousFlag = row[13]
        self.BookingPOR = row[14]
        self.BookingPOL = row[15]
        self.BookingPOD = row[16]
        self.BookingFPD = row[17]
        self.key = (self.BookingPOL,
                    self.BookingPOD,
                    operatorCode2ShipCompCode(self.OperatorCode),
                    self.ReeferFlag,
                    self.HazardousFlag,
                    self.ContainerSizeType)
    def getMMALineFormat(self, currency, price):
        return (CONSTANTS.CARRIER, #Company
                '', #Vessel
                self.CommercialVoyageNumber, #Voyage
                self.BookingPOL, #POL
                self.BookingPOD, #POD
                self.LoadDate, #CALL_DATE
                self.BLNumber, #BL_NUMBER
                currency, #Currency,
                price, #USDRate
                '1', #Count
                '', #RateType
                '', #RateName
                self.OperatorCode, #IssueShipper
                CONSTANTS.SOURCE, #Source
                '', #BusinessUnit
                price) #Amount

#--------------------------------------
#-- getIntragroupContainerBayplanFreightedHeader
#--------------------------------------
def getIntragroupContainerBayplanFreightedHeader():
    return ('Booking Number','Load Date','B/L Number','Container Number (ID)','Container Size/Type',
            'ISO Code','Commercial Voyage Number','Operational Voyage Number','Point Load',
            'Point Dish','Operator Code','Weight','Reefer Flag','Hazardous Flag','Booking POR',
            'Booking POL','Booking POD','Booking FPD','Currency','Amount')


#--------------------------------------
#-- IntragroupContainerDocumentation
#--------------------------------------
class IntragroupContainerDocumentation(IntragroupContainer):
    """
    This class is containing ontaining a mapping of the POO003 report fields.
    """
    def __init__(self, row):
        self.row = row
        self.BookingNumber = row[0]
        self.JobStatus = row[1]
        self.BLNumber = row[2]
        self.ShipCompCode = row[3]
        self.ContainerNumber = row[4]
        self.ContainerSizeType = row[5]
        self.MainVoyageReference = row[6]
        self.PhysicalVoyageNumber = row[7]
        self.POR = row[8]
        self.POL = row[9]
        self.POD = row[10]
        self.FPD = row[11]
        self.PointOrigin = row[12]
        self.PointDestination = row[13]
        self.Weight = row[14]
        self.ReeferFlag = row[15]
        self.HazardousFlag = row[16]
        self.Over_Length_AFT = row[17]
        self.Over_Length_AFT_Imp = row[18]
        self.Over_Length_Fore = row[19]
        self.Over_Length_Fore_Imp = row[20]
        self.Over_Width_Left = row[21]
        self.Over_Width_Left_Imp = row[22]
        self.Over_Width_Right = row[23]
        self.Over_Width_Right_Imp = row[24]
        self.Height = row[25]
        self.Height_Imp = row[26]
        self.OogFlag = row[27]
        self.key = (self.POL,
                    self.POD,
                    self.ShipCompCode,
                    self.ReeferFlag,
                    self.HazardousFlag,
                    self.ContainerSizeType.replace('/', ''))
    def getMMALineFormat(self, currency, price):
        return (CONSTANTS.CARRIER, #Company
                '', #Vessel
                self.PhysicalVoyageNumber, #Voyage
                self.POL, #POL
                self.POD, #POD
                '', #CALL_DATE
                self.BLNumber, #BL_NUMBER
                currency, #Currency,
                price, #USDRate
                '1', #Count
                '', #RateType
                '', #RateName
                shipCompCode2OperatorCode(self.ShipCompCode), #IssueShipper
                CONSTANTS.SOURCE, #Source
                '', #BusinessUnit
                price) #Amount
    
#--------------------------------------
#-- getIntragroupContainerDocumentationFreightedHeader
#--------------------------------------
def getIntragroupContainerDocumentationFreightedHeader():
    return ('Booking Number','Job_Status','BL Number','Shipcomp Code','Container Number',
            'Container Size/Type','Main Voyage Reference','Physical Voyage Number','POR','POL',
            'POD','FPD','Point Origin','Point Destination','Weight','Reefer Flag','Hazardous Flag',
            'Over_Length_AFT','Over_Length_AFT_Imp','Over_Length_Fore','Over_Length_Fore_Imp',
            'Over_Width_Left','Over_Width_Left_Imp','Over_Width_Right','Over_Width_Right_Imp',
            'Height','Height_Imp','OogFlag','Currency','Amount')

#--------------------------------------
#-- getRateFileHeader
#--------------------------------------
def getRateFileHeader():
    return ('POL','POD','ShipCompCode','Refer','Hazardous','Size/Type','Currency','Price')


#--------------------------------------
#-- getMMAFileHeader
#--------------------------------------
def getMMAFileHeader():
    return ('Company','Vessel','Voyage','POL','POD','CALL_DATE','BL_NUMBER','Currency',
            'USDRate','Count','RateType','RateName','IssueShipper','Source','BusinessUnit','Amount')

#--------------------------------------
#-- Price
#--------------------------------------
class Price:
    def __init__(self,row):
        self.row = row
        self.key = (row[0], #POL
                    row[1], #POD
                    row[2], #ShipCompCode
                    row[3], #ReeferFlag
                    row[4], #HazardousFlag
                    row[5]) #ContainerSizeType
        self.value = (row[6], #Currency
                      row[7]) #Price
    def printPrice(self):
        print self.key
        print self.value

#--------------------
#-- PriceList
#--------------------
class PriceList:
    def __init__(self):
        self.dico = dict()
    def addElement(self, key, value):
        self.dico[key] = value
    def printPriceList(self):
        print "The dictionnary of prices is loaded: ", self.dico


#--------------------
#-- usage
#--------------------
def usage():
    print "Usage:"
    print "For a POO002 report (bayplans):"
    print "  > freighter.py -b -f ContainerDataFile.csv -p PriceList.csv"
    print "For a POO003 report (documentations):"
    print "  > freighter.py -d -f DocumentationDataFile.csv -p PriceList.csv"
    print "Info: this tool will generate two files: the FreightedReport.csv and the MissingRates.csv file."

#--------------------
#-- main
#--------------------
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "bdf:p:hv", ["help"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    mode = 0
    dataFile = None
    priceFile = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-b"):
            mode = 1 #Bayplan
        elif o in ("-d"):
            mode = 2 #Documentation
        elif o in ("-f"):
            dataFile = a
        elif o in ("-p"):
            priceFile = a
        else:
            assert False, "unhandled option"

    if ((mode == 0) or (dataFile == None) or (priceFile == None)):
        usage()
        sys.exit()

    #-------------------------------------------------
    try:
        print "STEP 1: LOADING RATES"
        pricingReader = csv.reader(open(priceFile, "rb"), delimiter=';')
        i = 0
        dic = PriceList()
        for row in pricingReader:
            prix = Price(row)
            dic.addElement(prix.key, prix.value)
            i +=1
        print "STEP 1: %d prices loaded" % (i-1)
        if verbose:
            dic.printPriceList()

    except csv.Error, e:
        print "Error caught in loading price list"
        sys.exit('file %s, line %d: %s' % (priceFile, pricingReader.line_num, e))

    #-------------------------------------------------
    print "STEP 2: CREATING REPORTS"
    fl = None
    key = None
        
    #Freighter report writer creation
    try:
        if verbose:
            print "Creating FreightedReport.csv file"
        freightedReportWriter = csv.writer(open("FreightedReport.csv", "wb"), delimiter=';')
        if (mode ==1):
            freightedReportWriter.writerow(getIntragroupContainerBayplanFreightedHeader())
        else:
            freightedReportWriter.writerow(getIntragroupContainerDocumentationFreightedHeader())
        if verbose:
            print "Header FreightedReport.csv written"
    except csv.Error, e:
        print "Error caught in freighted writer manipulations"
        sys.exit('file %s : %s' % ("FreightedReport.csv", e))

    try:
        if verbose:
            print "Creating MissingRates.csv file"
        missingRatesWriter = csv.writer(open("MissingRates.csv", "wb"), delimiter=';')
        missingRatesWriter.writerow(getRateFileHeader())
        if verbose:
            print "Header MissingRates.csv written"
    except csv.Error, e:
        print "Error caught in missing rates writer manipulations"
        sys.exit('file %s : %s' % ("MissingRates.csv", e))
        
    try:
        if verbose:
            print "Creating FreightedReportForMMA.csv file"
        MMAReportWriter = csv.writer(open("FreightedReportForMMA.csv", "wb"), delimiter=';')
        MMAReportWriter.writerow(getMMAFileHeader())
        if verbose:
            print "Header FreightedReportForMMA.csv written"
    except csv.Error, e:
        print "Error caught in FreightedReportForMMA manipulations"
        sys.exit('file %s : %s' % ("FreightedReportForMMA.csv", e))
        
    try:
        #-------------------------------------------------
        print "STEP 3: PARSING SOURCE DATA (Diva report)"
        dataReader = csv.reader(open(dataFile, "rb"), delimiter=';')

        #main loop
        for row in dataReader:
            if (mode == 1):
                fl = IntragroupContainerBayplan(row)
            else:
                fl = IntragroupContainerDocumentation(row)

            try:
                key = fl.getKey()
                value = dic.dico[key]
                if verbose:
                    print "--> INTRAGROUP PRICE FOUND : key = ", key, "value = ", value

                #Freight the original report with adding two column at the end
                freightedReportWriter.writerow(tuple(row)+ value)

                #MMA report feeding
                MMAReportWriter.writerow(fl.getMMALineFormat(value[0], value[1]))

            except KeyError:
                if verbose:
                    print "No price found for container: ", key
                #write missing intragroup price in specific file
                missingRatesWriter.writerow(key)
                continue
        
    except csv.Error, e:
        print "Error caught !"
        sys.exit('file %s, line %d: %s' % (dataFile, dataReader.line_num, e))


#--------------------
#-- Calling main
#--------------------

if __name__ == "__main__":
    main()
