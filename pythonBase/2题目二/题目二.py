with open('prac_filerw.txt', mode='r', encoding='utf8') as f:
    lines = f.readlines()
    newlines = []
    for line in lines:
        if not line.strip():
            continue
        if "https://www.bilibili.com/video/av74106411/?p=" in line:
            newlines.append(line)
    print(newlines)
result = []
for line in newlines:
    digitStart = line.find('av74106411/?p=') + 14
    digitEnd = digitStart
    while line[digitEnd].isdigit():
        digitEnd += 1
    newdigit = int(line[digitStart:digitEnd]) + 3
    line = line.replace(line[digitStart:digitEnd],str(newdigit))
    result.append(line)
print(result)


