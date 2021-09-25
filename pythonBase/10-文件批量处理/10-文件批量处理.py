import os
import re
from pathlib import Path

class FileProcessing:
    def __init__(self,path):
        self.path = path
        self.fileInc = []
        self.fileAg = []
        self.getFile()
        self.sameFile()

    def getFile(self):
        pInc = re.compile(r'\.inc\.md$')
        pAg = re.compile(r'\.ag\.md$')

        for (dirpath, dirnames, filenames) in os.walk(self.path):
            for fn in filenames:
                if pInc.findall(fn) and os.path.join(dirpath,fn) not in self.fileInc:
                    self.fileInc.append(os.path.join(dirpath,fn))
                elif pAg.findall(fn) and os.path.join(dirpath,fn) not in self.fileAg:
                    self.fileAg.append(os.path.join(dirpath,fn))


    def sameFile(self):
        p = re.compile(r'(\w+)\.\w+\.md$')
        fileIncName = {}
        fileAgcName = {}
        for f in self.fileInc:
            for match in p.finditer(f):
                fileIncName[match.group(1)]=f
        for f in self.fileAg:
            for match in p.finditer(f):
                fileAgcName[match.group(1)]=f

        for fileIn in fileIncName:

            if fileIn in fileAgcName:
                fileTime = self.readFileTime()
                if fileTime[fileAgcName[fileIn]] == int(os.path.getmtime(fileAgcName[fileIn])):
                    print('文件已修改')
                    continue
                else:
                    self.submit(fileIncName[fileIn])
                    self.recordFileTime()

            else:
                self.submit(fileIncName[fileIn])
                self.recordFileTime()

    def submit(self,f):
        p = re.compile(r'<jcy-include> "(.*\.md)"',re.M)
        with open(f,mode='r',encoding='utf8') as f1, open(f'{os.path.join(os.path.dirname(f),os.path.basename(f).split(".")[0]+".ag.md")}',mode='w',encoding='utf8') as f2:
            line = f1.read()
            line = re.sub(p,self.subFunc,line)
            f2.write(line)
    def subFunc(self,match):
        file = os.path.join(self.path,match.group(1))
        with open(file,mode='r',encoding='utf8') as f:
            line = f.read()
        return line

    def recordFileTime(self):
        self.getFile()
        fileTime = []
        for file in self.fileAg:
            fileTime.append(f'{file}:{os.path.getmtime(file)}\n')
        with open('record.txt','w') as f:
            f.writelines(fileTime)

    def readFileTime(self):
        fileTime = {}
        with open('record.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                fileTime[f"{line.split(':')[0]}"] = int(float(line.split(':')[1]))
        return fileTime


fP = FileProcessing(r'.\hugo-demo\content')

