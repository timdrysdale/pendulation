#!/usr/bin/env python3

import json

#https://stackoverflow.com/questions/9282967/how-to-open-a-file-using-the-open-with-statement
# separate json objects on the same line by inserting newline
# improve to detect whitespace between objects 
def splitobjects(oldfile, newfile):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''
    outfile = open(newfile, 'w')
    with open(oldfile, 'r', encoding='utf-8') as infile:
        for line in infile:
            newline  = line.replace("}{", "}\n{")
            outfile.write(newline)

    outfile.close()
    return # Do I gain anything by including this?



if __name__ == "__main__":
    
    #filter file to insert newline if there are multiple json objects
    
    oldfile  = "pendulum-nuc.json"
    newfile  = "pendulum-nuc.filtered.json"
    splitobjects(oldfile,newfile)

    outfile = open("pendulum-nuc.csv", 'w')

    with open(newfile, 'r', encoding='utf-8') as infile:
        for line in infile:
            try:
                obj = json.loads(line)
                outfile.write("{:d},{:d}\n".format(obj["time"], obj["enc"]))
            except Exception as e:
                print(e)

