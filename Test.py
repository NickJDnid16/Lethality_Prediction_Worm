import csv
inputfile = open('./allele_phenotypic_data_fb_2015_04.tsv', mode='r')
outputfile = open('./NumOfGenes.txt', mode='w')
inputfile = csv.reader(inputfile, delimiter='\t')
outputfile = csv.writer(outputfile)
Seen = []

for row in inputfile:



      #del row[1]
    Temp = (str(row[0]))
    Temp = Temp.split('[')[0].strip()
    #Temp = Temp.replace(',','')
    #print Temp
    #print len(Temp)
    if Temp not in Seen:

        Seen.append(Temp)
print len(Seen)








