import csv
from graphviz import Graph

#===============================================
class Field:
	fieldID = 0
	tablename = ''
	fieldname = ''
	fieldtype = ''
	
	def __init__(self, fid, tname,fname,ftype):
		self.fieldID   = fid		
		self.tablename = tname
		self.fieldname = fname
		self.fieldtype = ftype

#===============================================
FIELDS = []
GRAPH = Graph()

#===============================================
def loadFields():
	with open('base.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row['ID'], row['TableName'], row['FieldName'], row['FieldType'])
			FIELDS.append(Field(row['ID'], row['TableName'], row['FieldName'], row['FieldType']))
	print(FIELDS)
						
#===============================================
def generateGraph():
	for f in FIELDS:
		GRAPH.node(f.fieldID, f.fieldName)
		GRAPH.edge(
		



#===============================================
def main():
	loadFields()

#===============================================
if __name__ == "__main__":
    main()

