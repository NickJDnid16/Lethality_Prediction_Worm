__author__ = 'nid16'

import codecs
import csv

data = {}
import sys

outputfile = open('./Gene&GO_F.txt', mode='w')
FUNCoutputfile = open('./Gene_With_GO_FUNC .txt', mode='w')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='w')
Seen =[]
FUNC = []
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



########################################################

newFUNC = []

geneSeen = []
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    lethality = split_line[1]
    if (lethality == "lethal"):
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                tempFUNC.append(str(line) + "\t1")
                print tempFUNC
                newFUNC.append(tempFUNC)
    if (lethality == "viable"):
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.replace('\n','')
                tempFUNC.append(str(line) + "\t0")

                print tempFUNC
                newFUNC.append(tempFUNC)

        print "Something"
        #print tempFUNC
#FUNCoutputfile.write("\n".join(newFUNC))


for element in newFUNC:
    #FUNCoutputfile.writelines(str(element)+"\n")
    FUNCoutputfile.write(" ".join(element) + "\n")


###############################################################



########################################################

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")
  #  FUNCoutputfile.write()
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
########################################################
outputfile.close()
inputfile = open('./Gene&GO_F_With_Lethality.txt', mode='r')
lethaloutfile = open('./Worm_Gene_Lethal.txt', mode='w')
alloutfile = open('./Worm_Gene_Viable_Lethal.txt', mode='w')
inputfile = csv.reader(inputfile, delimiter=',')
for line in inputfile:
    if "lethal" in line[-1]:
        lethaloutfile.write(line[0] + "\n")
    alloutfile.write(line[0] + "\n")