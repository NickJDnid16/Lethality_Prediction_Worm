__author__ = 'nid16'

import codecs
import csv

data = {}

outputfile = open('./Gene&GO_F.txt', mode='w')

for line in open('./gene_association.WS250.wb.c_elegans'):

    if(line[:2] == "WB"):#FlyBase = FB
        split_string = line.split("\t")
        genome = split_string [2]
        GO = split_string [4]
        dataMarker = split_string [6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","

for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")

outputfile.close()


########################################################


inputfile = open('./Gene&GO_F.txt', mode='r')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)



for rows in inputfile:

        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                print rows
