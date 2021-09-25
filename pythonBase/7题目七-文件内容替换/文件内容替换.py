import os

# 目标目录
targetDir = r'E:\CODE\byhy\python基础\7题目七-文件内容替换\prac_re'
files = []


for (dirpath,dirnames,filenames) in os.walk(targetDir):
    for fn in filenames:

        files.append(os.path.join(dirpath,fn))

for file in files:
    with open(file,mode='r',encoding='utf8') as f1, open(f'{file}.bak',mode='w',encoding='utf8') as f2 :

        lines = f1.readlines()
        for line in lines:
            print(line)
            if not line.split(' '):
                continue
            if "https://www.bilibili.com/video/av74106411/?p=" in line:
                digitStart = line.find('av74106411/?p=') + 14
                digitEnd = digitStart
                while line[digitEnd].isdigit():
                    digitEnd += 1
                newdigit = int(line[digitStart:digitEnd]) + 3
                line = line.replace(line[digitStart:digitEnd],str(newdigit))
            f2.write(line)

