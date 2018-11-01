#============================================
# File name:      CI.py
# Author:         Olivier Rey
# Date:           November 2018
# License:        GPL v3
#============================================
import csv

class CI():
    def __init__(self, mid, row):
        self.mid = mid
        self.WBS = row[0]
        self.Doc_Type = row[1]
        self.Part_number = row[2]
        self.Issue = row[3]
        self.Father_parts = row[4]
        self.CI_before = row[5]
        self.Title = row[6]
        self.CI_type = row[7]
        self.Status = row[8]
        self.Creation_Date = row[9]
        self.Released_Date = row[10]
        self.Usage = row[11]
        self.CI_characteristic = row[12]
        self.Substitute = row[13]
        self.Des_group = row[14]
        self.MOE = row[15]
        self.SDU = row[16]
        self.APPLICABILITY = row[17]
        self.SMR = row[18]
        self.SAP = row[19]
        self.Conf = row[20]
        self.DE_below = row[21]
        self.ADU_Father = row[22]
        self.ECR = row[23]
        self.ECP = row[24]
        self.ECO_Fathers = row[25]
        self.ECO = row[26]
        self.ECO_links = row[27]
        self.NOT_ECO = row[28]
        self.Part_Effectivity_EC175_B = row[29]
        self.Part_Effectivity_Z15F = row[30]
        self.Part_Effectivity_Z15_Shipset = row[31]
        self.Part_Effectivity_EC175_B1 = row[32]
        self.EC175_B_from = row[33]
        self.EC175_B_to = row[34]
        self.EC175_B1_from = row[35]
        self.EC175_B1_to = row[36]
        self.Average_Weight = row[37]
        self.Weighed_Weight_1 = row[38]
        self.Weighed_Weight_2 = row[39]
        self.Weighed_Weight_3 = row[40]
        self.Weighed_Weight_4 = row[41]
        self.Weighed_Weight_5 = row[42]
        self.Weighed_Weight_6 = row[43]
        self.Weighed_Weight_7 = row[44]
        self.Weighed_Weight_8 = row[45]
        self.Weighed_Weight_9 = row[46]
        self.Weighed_Weight_10 = row[47]
        self.Weighed_Weight_11 = row[48]
        self.Weighed_Weight_12 = row[49]
        self.Weighed_Weight_13 = row[50]
        self.Weighed_Weight_14 = row[51]
        self.Weighed_Weight_15 = row[52]
        self.WB_Weight = row[53]
        self.Auto_Calculated_Weight = row[54]
        self.Calculated_Weight = row[55]
        self.Estimated_Weight = row[56]
        self.COG_X = row[57]
        self.COG_Y = row[58]
        self.COG_Z = row[59]
        self.Auto_Calculated_COG_X = row[60]
        self.Auto_Calculated_COG_Y = row[61]
        self.Auto_Calculated_COG_Z = row[62]
        self.WB_COG_X = row[63]
        self.WB_COG_Y = row[64]
        self.WB_COG_Z = row[65]


def test(filename):
    reader = csv.reader(open(filename, "r"), delimiter=';')
    i = 0
    elems = {}
    # create target dict    dic = PriceList()
    try:
        for row in reader:
            if i != 0:
                ci = CI(i, row)
                elems[i] = ci
            i +=1
        print("%d lines loaded" % (i-1))
    except csv.Error as e:
        print("Error caught in loading csv file")
        print(e)
    

if __name__ == '__main__':
    test('test.csv')
