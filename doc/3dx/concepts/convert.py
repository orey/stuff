import sys, json, csv

def usage():
    print("Converter of DS 3DX JSON list of modules")
    print("Usage (warning, parameters must be entered in order):")
    print("> convert [filename.json] [option]")
    print("Options:")
    print("    [1]: print 3DX modules (rough JSON)")
    print("    [2]: count 3DX modules")
    print("    [3]: analyze 3DX modules")
    print("    [4]: export CSV")

#=========================================JSON structure
#reader: new Ext.data.JsonReader({
#	            root: 'products',
#	            id: 'id',
#	            fields: [
#	               'product_number', 
#	               'product_type',
#	               'product_trigram', 
#	               'product_name', 
#	               'prerequisite', 
#	               'available_pricing',
#	               'default_support_level',
#	               'ext_enterprise_user',
#	               'remote_access',
#	               'licensing_structure',
#	               'withdrawn_after',
#	               'portfolio_type',
#	               'portfolio_product',
#	               'product_description',
#				   'business_category',
#				   'addtional_information',
#				   'addtional_information_label',
#				   'ds_offerings',
#	            ]
#	        }),
#
#{"id":"3382",
# "business_category":"3DEXCITE DELTAGEN",
# "product_number":"6CB-DMK-EDU",
# "product_type":"Package",
# "product_trigram":"DMK-EDU",
# "product_name":"3DEXCITE DELTAGEN Marketing Suite - University",
# "prerequisite":"",
# "available_pricing":"PLC\/YLC\/TBL2\/TBL3",
# "default_support_level":"Advantage",
# "ext_enterprise_user":"No",
# "remote_access":"No",
# "licensing_structure":"Shareable",
# "withdrawn_after":"",
# "portfolio_type":null,
# "portfolio_product":null,
# "included_products_numbers":null,
# "included_item_names":null,
# "addtional_information":"",
# "ds_offerings":"Licensed Program",
# "addtional_information_label":"",
# "product_description":[{
#    "id":"3382",
#    "business_category":"3DEXCITE DELTAGEN",
#    "product_number":"6CB-DMK-EDU",
#    "product_type":"Package",
#    "product_trigram":"DMK-EDU",
#    "product_name":"3DEXCITE DELTAGEN Marketing Suite - University",
#    "prerequisite":"",
#    "available_pricing":"PLC\/YLC\/TBL2\/TBL3",
#    "default_support_level":"Advantage",
#    "ext_enterprise_user":"No",
#    "remote_access":"No",
#    "licensing_structure":"Shareable",
#    "withdrawn_after":"",
#    "portfolio_type":null,
#    "portfolio_product":null,
#    "included_products_numbers":null,
#    "included_item_names":null,
#    "addtional_information":"",
#    "ds_offerings":"Licensed Program",
#    "addtional_information_label":""}]}


FIELD_NAMES = ['id','business_category', 'product_name', 'product_number', 'product_type', 'product_trigram','prerequisite','available_pricing','default_support_level','ext_enterprise_user','remote_access','licensing_structure','withdrawn_after','portfolio_type','portfolio_product','included_product_numbers','included_item_names','ds_offerings']

def filter_dict(dic, filter):
    dict2 = dict()
    for k, v in dic.items():
        if k in filter:
            dict2[k] = v  #.replace('\n','')
    return dict2

            
def dump_store(datastore):
    tab = datastore["products"]
    with open('modules.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for elem in tab:
            writer.writerow(filter_dict(elem,FIELD_NAMES))
    print("Dump completed")

    
def print_3DX_modules(datastore):
    tab = datastore["products"]
    for elem in tab:
        print(elem)

        
def count_3DX_modules(datastore):
    tab = datastore["products"]
    i = 0
    for elem in tab:
        i += 1
    print("Number of elements printed:" + str(i))

    
def analyze_3DX_modules(datastore):
    tab = datastore["products"]
    for elem in tab:
        print(len(elem["product_description"]),end = '|')

        
if __name__ == "__main__":
    filename = ""
    datastore = None
    opt = 0
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        opt = sys.argv[2]
    else:
        usage()
        sys.exit(0)
    try:
        with open(filename, 'r') as f:
            datastore = json.load(f)
            print(opt)
            if opt == '1':
                print_3DX_modules(datastore)
            elif opt == '2':
                count_3DX_modules(datastore)
            elif opt == '3':
                analyze_3DX_modules(datastore)
            elif opt == '4':
                dump_store(datastore)
            else:
                print("Option not recognized")
    except Exception as e:
        print("An error has occurred.")
        print(e)



