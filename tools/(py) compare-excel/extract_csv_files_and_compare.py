import pandas as pd

def createDelta(old, new, delta):
    print('Comparing:' + old + ' and ' + new + '...')
    with open(old, 'r', encoding="utf-8") as t1, open(new, 'r', encoding="utf-8") as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    with open(delta, 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                outFile.write(line)
    print(delta + ' file created')

sheetnames1 = []
data1 = pd.read_excel('old.xlsx', sheet_name=None)

# loop through the dictionary and save csv
fn = ""
for sheet_name, df in data1.items():
    fn = 'old_' + sheet_name +'.csv'
    print('Generating: ' + fn)
    df.to_csv(fn, sep='|')
    sheetnames1.append(sheet_name)
    print('Done')

sheetnames2 = []
data2 = pd.read_excel('new.xlsx', sheet_name=None)

# loop through the dictionary and save csv
for sheet_name, df in data2.items():
    fn = 'new_' + sheet_name +'.csv'
    print('Generating: new_' + sheet_name + '.csv')
    df.to_csv(fn, sep='|')
    sheetnames2.append(sheet_name)
    print('Done')

for sn in sheetnames2:
    if sn in sheetnames1:
        createDelta('old_' + sn + '.csv', 'new_' + sn + '.csv', 'compared_' + sn + '.csv')
    else:
        print(sn + ' tab is in the new file and not in the old one. Skipping...')


        
