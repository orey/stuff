import freighter

#--------------------
#-- WebADI
#--------------------
class CONSTANTS:
	"""
	Constants of the WebADI module
	"""
	CARRIER_CODES = ('ANLS':'266', 'ANLC':'260', 'CNC':'261', 'CMACGM':'001', 'DELMAS':'006')
	SITES_CODES = ('ANLS':'SIN', 'ANLC':'TBD', 'CNC':'TBD', 'CMACGM':'TBD', 'DELMAS':'TBD')

#--------------------
#-- WebADI
#--------------------
class WebADI:
    """
    This class is managing the output in WebADI.
    """
    def __init__(self, company, year, month, verbose):
        try:
			assert company in CONSTANTS.CARRIER_CODES, "Unknown company code"
		except AssertionError, ae:
			print str(ae)
		self.company = company
		self.year
		self.verbose = verbose
		
	def createAccountingDate(self):
		lastdayofthemonth = calendar.monthrange(self.year, self.month)[1]
		self.accountingdate =  lastdayofthemonth
								+ '/' 
								+ self.month
								+ '/'
								+ self.year
		if self.verbose
			print self.accountingdate
	

	
	# The line is taking the P&L account as a basis
	def createLine(self, PLaccount, BSaccount, nature, BU, currency, amount):
		batchname = 'MMA-INTRAGROUP-' + accountingdate.replace('/', '')
		if (amount>0):
			positivePL = true
		else:
			positivePL = false
		#Writing main row
		self.mainrow = (
			'MMA-INTRAGROUP-GL-', 									#CATEGORY ; MMA-PROVISION-GL-
			'Spreadsheet', 											#SOURCE ;Spreadsheet
			self.accountingdate,									#ACCOUNTING_DATE;31/07/2009
			'USD',													#CURRENCY;USD
			'Reuters',												#CONVERSION TYPE;Reuters
			self.accountingdate,									#CONVERSION DATE;31/07/2009
			'',														#CONVERSION RATE;
			CONSTANTS.CARRIER_CODES[self.company],					#COMPANY;266
			CONSTANTS.SITE_CODES[self.company], 					#SITE;SIN
			PLaccount, 												#IFRS ACCOUNT;468600L00000
			nature,													#NATURE;C4103
			BU, 													#BUSINESS UNIT;S-AANAANL
			XXXXXXX, 												#INTERCOMPANY;-
			'-', 													#AGENT;-
			'I',													#JOURNAL TYPE;I
			'-',													#SPARE1;-
			'-',													#SPARE2;-
			'-',													#SPARE3;-
			if_else(not positivePL,amount,''),						#DEBIT;11525,2
			if_else(positivePL,amount,''),							#CREDIT;
			'',														#DEBIT CONVERTED USD;
			'', 													#CREDIT CONVERTED USD;
			batchname, 												#BATCH NAME;MMA-PROVISION-31072009
			batchname, 												#BATCH DESCRIPTION;MMA-PROVISION-31072009
			batchname, 												#JOURNAL NAME;MMA-PROVISION-31072009
			batchname,												#JOURNAL DESCRIPTION;MMA-PROVISION-31072009
			batchname, 												#LINE DESCRIPTION;MMA-PROVISION-31072009
			'PL',													#LINE DFF CONTEXT;PL
			'PL.' + self.accountingdate + '..AUADL............',	#FILTER;PL.31/07/2009..AUADL............
			'',														#MANAGEMENT PERIOD;
			'',														#VOYAGE;
			'',														#PORT;
			'',														#PORT OF DISCHARGE;
			'',														#VESSEL;
			'',														#BL NUMBER;
			'',														#BALANCE BL STATUS;
			'',														#PAYMENT METHOD;
			'',														#CALL DATE;
			'',														#DUE DATE;
			'',														#TARIFF CURRENCY;
			'',														#TARIFF AMOUNT DT;
			'',														#TARIFF AMOUNT CT;
			'',														#GAP STATUS;
			'',														#LARA INVOICE NUMBER;
			'',														#FREIGHT INVOICED DATE;
			''														#LARA PARTNER CODE;
			)
		#Writing counterpart row
		self.couterpartrow = (
			'MMA-INTRAGROUP-GL-', 									#CATEGORY ; MMA-PROVISION-GL-
			'Spreadsheet', 											#SOURCE ;Spreadsheet
			self.accountingdate,									#ACCOUNTING_DATE;31/07/2009
			'USD',													#CURRENCY;USD
			'Reuters',												#CONVERSION TYPE;Reuters
			self.accountingdate,									#CONVERSION DATE;31/07/2009
			'',														#CONVERSION RATE;
			CONSTANTS.CARRIER_CODES[self.company],					#COMPANY;266
			CONSTANTS.SITE_CODES[self.company], 					#SITE;SIN
			BSaccount, 												#IFRS ACCOUNT;468600L00000
			nature,													#NATURE;C4103
			BU, 													#BUSINESS UNIT;S-AANAANL
			XXXXXXX, 												#INTERCOMPANY;-
			'-', 													#AGENT;-
			'I',													#JOURNAL TYPE;I
			'-',													#SPARE1;-
			'-',													#SPARE2;-
			'-',													#SPARE3;-
			if_else(positivePL,amount,''),							#DEBIT;11525,2
			if_else(not positivePL,amount,''),						#CREDIT;
			'',														#DEBIT CONVERTED USD;
			'', 													#CREDIT CONVERTED USD;
			batchname, 												#BATCH NAME;MMA-PROVISION-31072009
			batchname, 												#BATCH DESCRIPTION;MMA-PROVISION-31072009
			batchname, 												#JOURNAL NAME;MMA-PROVISION-31072009
			batchname,												#JOURNAL DESCRIPTION;MMA-PROVISION-31072009
			batchname, 												#LINE DESCRIPTION;MMA-PROVISION-31072009
			'PL',													#LINE DFF CONTEXT;PL
			'PL.' + self.accountingdate + '..AUADL............',	#FILTER;PL.31/07/2009..AUADL............
			'',														#MANAGEMENT PERIOD;
			'',														#VOYAGE;
			'',														#PORT;
			'',														#PORT OF DISCHARGE;
			'',														#VESSEL;
			'',														#BL NUMBER;
			'',														#BALANCE BL STATUS;
			'',														#PAYMENT METHOD;
			'',														#CALL DATE;
			'',														#DUE DATE;
			'',														#TARIFF CURRENCY;
			'',														#TARIFF AMOUNT DT;
			'',														#TARIFF AMOUNT CT;
			'',														#GAP STATUS;
			'',														#LARA INVOICE NUMBER;
			'',														#FREIGHT INVOICED DATE;
			''														#LARA PARTNER CODE;
			)


#--------------------
#-- Ternary operator
#--------------------
def if_else(condition, trueVal, falseVal):
if condition:
    return trueVal
else:
    return falseVal

#--------------------
#-- Calling main
#--------------------
def main():			
	"""
	This function tests the WebADI mapping
	"""
	
			
#--------------------
#-- Calling main
#--------------------
if __name__ == "__main__":
    main()
