import os
import re
# 目标目录
targetDir = r'E:\CODE\byhy\pythonBase\7题目七-文件内容替换\prac_re'
files = []
files2 = []

for (dirpath,dirnames,filenames) in os.walk(targetDir):
    for fn in filenames:
        if str(fn).endswith('.md'):
            files.append(os.path.join(dirpath,fn))
        if str(fn).endswith('.bak2'):
            os.remove(os.path.join(dirpath,fn))

def subFunc(match):
    src = match[0]
    number = int(match[1]) + 3
    dest = f'https://www.bilibili.com/video/av74106411/?p={number}'
    return dest




p = re.compile(r'https://www\.bilibili\.com/video/av74106411/\?p=(\d+)')
for file in files:

    with open(file,mode='r',encoding='utf8') as f1, open(f'{file}.bak2',mode='w',encoding='utf8') as f2 :

        lines = f1.read()


        f2.write(re.sub(r'https://www\.bilibili\.com/video/av74106411/\?p=(\d+)',subFunc,lines))

