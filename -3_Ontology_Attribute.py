'''
Created on 26 Oct 2015

@author: nid16
'''

import codecs 

output = open('./Ontology_Attributes.txt', mode='wb')

line = 0 

output.write("@relation Lethality\n" + "\n" + "@attribute gene string\n")

for Line in open('./Refined_GO_Nodes.txt', mode='rb'):
    line = line+1
    print(line)
    output.write("@attribute ")
    Line = Line.replace("\n", "")
    Line = Line.replace("\r", "")
    output.write(Line)
    output.write(" {1,0}")
    output.write("\n")

output.write("@attribute outcome {lethal,viable}\n" + "\n" + "@data\n")
output.close()