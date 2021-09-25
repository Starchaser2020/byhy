from threading import Thread,Lock
import requests

taskList = [
    'http://mirrors.kernel.org/gnu/gnome.README',
    'http://mirrors.163.com/centos/6/isos/x86_64/README.txt',
    'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt',
]
lock = Lock()
content = {}
def getHttpText(URL,idx):

    res = requests.get(URL)
    HttpText = res.text
    lock.acquire()
    # with open('./readme89.TXT',mode='a',encoding='utf8') as f:
    #     f.write(f'第{idx}个址的内容\n{HttpText}')
    content[idx] = f'第{idx}个请求返回的内容------{HttpText}'
    lock.release()
theadlist = []
for idx in range(len(taskList)):
    thread = Thread(
                    target=getHttpText,
                    args=(taskList[idx],idx),
    )
    thread.start()
    theadlist.append(thread)
for thread in theadlist:
    thread.join()

with open('./readme89.TXT',mode='a',encoding='utf8') as f:
    for i in range(len(content)):
        f.write(content[i])

