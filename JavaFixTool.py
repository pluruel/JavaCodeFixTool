import os
import re
from shutil import copyfile

inputpath = "C:\dev\Python\input"
outputpath = "C:\dev\Python\output"

def search(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            fullpath = path + '\\' + filename
            genpath = fullpath.replace(dirname, '')
            cpyandpaste(dirname, genpath, filename)
 
        
def cpyandpaste(dirname, path, filename):
    inf = open(dirname + path, 'r')
    newpath = path
    outputfullpath = outputpath + newpath
    outputfolderpath = outputfullpath.replace(filename, '')
    
    ext = os.path.splitext(filename)[-1]

    if ext == '.class' or ext == '.git'):
        return

    if not os.path.exists(outputfolderpath):
        os.makedirs(outputfolderpath)
    outf = open(outputfullpath, 'w')
    
    if ext != '.java' :
        copyfile(dirname + path, outputfullpath)
        outf.close()
        return

    else :
        while True:
            line = inf.readline()
        
            if not line: break

            if line.find("new AVC(") > -1:
                line = line.replace("new AVC(", "AVC.run2(")
           
            outf.write(line)
    outf.close()



search(inputpath)

