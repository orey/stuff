#============================================
# File name:      csv2rdf.py
# Author:         Olivier Rey
# Date:           November 2018
# License:        GPL v3
#============================================
import csv, configparser
from rdflib import Graph, Literal, URIRef, RDF
from rdf2graphviz import rdf_to_graphviz

# Keys in the config file
DOMAIN = 'domain'
TYPE = 'type'
PREFIX = 'predicate_prefix'
DELIMITER = 'delimiter'

class Config():
    def __init__(self,config_filename, csv_filename):
        self.domain = ''
        self.type = ''
        self.prefix = ''
        self.delimiter = ''
        self.predicates = []
        self.csv_filename = csv_filename
        self.config = configparser.ConfigParser()
        self.config.read(config_filename)
        if csv_filename in self.config:
            self.domain = self.config[csv_filename][DOMAIN]
            self.type = self.config[csv_filename][TYPE]
            self.prefix = self.config[csv_filename][PREFIX]
            self.delimiter = self.config[csv_filename][DELIMITER]
        self.store = Graph()
        self.type = URIRef(self.domain + self.type)
    def print(self):
        print('Configuration for ' + self.csv_filename + ': ' \
              + self.domain + '|' + self.type + '|' + self.prefix \
              + '|' + self.delimiter)
    def parse_file(self):
        reader = csv.reader(open(self.csv_filename, "r"), \
                            delimiter=self.delimiter)
        try:
            for i, row in enumerate(reader):
                if i == 0:
                    for elem in row:
                        predicate = self.domain + format_predicate(elem)
                        self.predicates.append(URIRef(predicate))
                    print(self.predicates)
                else:
                    subject = URIRef(self.domain + self.prefix + str(i))
                    self.store.add((subject, RDF.type, self.type))
                    for n, elem in enumerate(row):
                        if not elem == '':
                            e = Literal(elem)
                            self.store.add((subject, self.predicates[n], e))
                        
            print("%d lines loaded" % (i-1))
        except csv.Error as e:
            print("Error caught in loading csv file")
            print(e)
    def dump_store(self):
        storename = self.csv_filename.split('.')[0] + '.rdf'
        self.store.serialize(storename, format='turtle')
        print('Store dumped')
    def get_store(self):
        return self.store
        
def format_predicate(pred):
    new = ''
    for i, c in enumerate(pred):
        if c in [' ', '-']:
            new += '_'
        else:
            new += pred[i]
    return new

    
def test_pred():
    print(format_predicate('I am a big-boy'))


if __name__ == '__main__':
    conf = Config('csv2rdf.ini','test.csv')
    conf.print()
    test_pred()
    conf.parse_file()
    conf.dump_store()
    rdf_to_graphviz(conf.get_store(),'xyz', True, False)
