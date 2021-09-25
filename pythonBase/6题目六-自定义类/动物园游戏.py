import random
import time
from threading import Thread
numberRoom = {}


# 游戏开始
class Tiger:

    food = 'meat'

    def __init__(self):
        self.weight = 200

    def jiao(self):
        self.weight -= 5
        print('Wow!!')

    def weishi(self,food):
        if self.food == food:
            self.weight += 10
        else:
            self.weight -= 10
class Sheep:

    food = 'grass'


    def __init__(self):
        self.weight = 100

    def jiao(self):
        self.weight -= 5
        print('mie~~')

    def weishi(self,food):
        if Sheep.food == food:
            self.weight += 10
        else:
            self.weight -= 10
class Room:
    number = 10

    def __init__(self):
         self.animal = self.getAnimal()
    def getAnimal(self):
        roomType = {}
        for room in range(1,self.number+1):
            if random.randint(0, 1) == 0:
                roomType[room] = Tiger()
            else:
                roomType[room] = Sheep()
        return roomType

room = Room()
print(room.animal)

timeNow = time.time()

print(room.animal[1])

while True:
    roomNumber = random.randint(1,10)
    choice = input("房间号是：%i，请输入你的选择----喂食(直接输入meat或者grass)  敲门(回车)："%roomNumber)

    timeEnd = time.time()

    if choice == '':
        room.animal[roomNumber].jiao()
    elif choice == 'grass' or choice == 'meat':
        room.animal[roomNumber].weishi(choice)
    else:
        print('想不想玩儿！')
    if timeEnd - timeNow > 10:
        break

    if timeEnd - timeNow > 10:
        break
for room,animal in room.animal.items():
    print(f'房间{room}动物体重为{animal.weight}')













