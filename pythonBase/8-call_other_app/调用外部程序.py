from subprocess import PIPE,Popen
import os
targetDir = r'E:\CODE\byhy\pythonBase\8-call_other_app\callOthers'
files = []


for (dirpath, dirnames, filenames) in os.walk(targetDir):

    for fn in filenames:
        # 把 dirpath 和 每个文件名拼接起来 就是全路径
        files.append(os.path.join(dirpath,fn))

for file in files:
    newfile = file[:-3] + 'new.mp4'


    proc = Popen(
        fr'ffmpeg.exe -i "{file}" -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy "{newfile}"',
        shell=True,
        stderr=PIPE,
        stdout=PIPE,
    )
    outinfo, errinfo = proc.communicate()
    outinfo = outinfo.decode('gbk')


