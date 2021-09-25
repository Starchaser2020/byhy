with open('cfiles/gbk编码.txt', mode='r', encoding='gbk') as f1:
    gbkStr = f1.read()
with open('cfiles/utf8编码.txt', mode='r', encoding='utf8') as f2:
    utf8Str = f2.read()
newStr = gbkStr + utf8Str
print(newStr)
newFile = input('请输入新文件的名称：')
newFile = newFile + '.txt'
with open(f"题目一/cfiles/{newFile}", mode='w', encoding='utf8') as f3:
    f3.write(newStr)
