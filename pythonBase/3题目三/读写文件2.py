import os


def png_jpg(str):
    with open(str,mode='rb') as f:
        line = f.read(8)
        pngB = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
        if line == pngB:
            print('png')
        else:
            print('jpg')
png_jpg('C:\\Users\DELL\Pictures\Figure_1')
