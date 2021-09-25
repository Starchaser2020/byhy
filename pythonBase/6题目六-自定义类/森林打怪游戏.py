import random

class Palyer:

    def __init__(self, arrowSolderNumber, axeSolderNumber, arrowSolder, axeSolder):
        self.lingshi = 1000
        self.arrowSolderNumber = arrowSolderNumber
        self.arrowSolder = arrowSolder
        self.axeSolderNumber = axeSolderNumber
        self.axeSolder = axeSolder
        self.solder = self.getSolder()
        self.currentSloder = None
        self.hireSolder()
    def choiceSolder(self, solder):
        if solder in self.solder:
            return self.solder[solder]

    def getSolder(self):
        solder = {}
        for arrowSolder in self.arrowSolder:
            solder[arrowSolder] = ArrowSolder()
        for axeSolder in self.axeSolder:
            solder[axeSolder] = AxeSolder()
        return solder

    def healSolder(self,lingshiNumber):
        self.lingshi -= lingshiNumber
        self.currentSloder.getHeal(lingshiNumber)

    def hireSolder(self):
        self.lingshi -= self.arrowSolderNumber * ArrowSolder.price
        self.lingshi -= self.axeSolderNumber * AxeSolder.price


class ArrowSolder():
    Typename = '弓箭兵'
    price = 100
    def __init__(self):
        self.blood = 100

    def killMonster(self,moster):

        if moster == '鹰妖' and self.blood >=20:
            self.blood -= 20
        elif moster == '狼妖' and self.blood >= 80:
            self.blood -= 80
        else:
            self.blood = 0

    def getHeal(self,lingshi):
        self.blood += lingshi
        if lingshi + self.blood >= 100:
            self.blood = 100


class AxeSolder():
    Typename = '斧头兵'
    price = 120
    def __init__(self):
        self.blood = 120

    def killMonster(self,monster):
        if monster == '鹰妖' and self.blood >= 80:
            self.blood -= 80
        elif monster == '狼妖' and self.blood >= 20:
            self.blood -= 20
        else:
            self.blood = 0
    def getHeal(self,lingshi):
        self.blood += lingshi
        if lingshi + self.blood >= 100:
            self.blood = 100
class Forest:
    def __init__(self):
        self.forestAnimal = self.produceAnimal()

    def produceAnimal(self):
        forestAnimal = []
        for i in range(7):
            animal = random.choice(['鹰妖', '狼妖'])
            forestAnimal.append(animal)
        return forestAnimal
forestAnimal = Forest().produceAnimal()
print('森林中的怪物：',forestAnimal)

while True:
    arrowNumber = int(input('请选择弓箭兵的数量：'))
    axeNumber = int(input('请选择斧头兵的数量：'))
    if arrowNumber * 100 + axeNumber * 120 > 1000:
        print('灵石不足')
        continue
    break


arrow = input('请为每个弓箭兵命名：').split(' ')
axe = input('请为每个斧头兵命名：').split(' ')

player = Palyer(arrowNumber,axeNumber,arrow,axe)
forestIndex = 0
while forestIndex <= 6:
    currentSolders = [solder for solder in player.solder]
    print('当前士兵：',currentSolders)
    print('这是第%i座森林，请派出你的战士：'%(forestIndex+1))
    solderName = input('请输入你的勇士名字：')
    player.currentSloder = player.choiceSolder(solderName)
    print('当前战士血量：',player.currentSloder.blood)
    lingshi = int(input('选择是否需要治疗当前士兵（不需要请输入0，需要请输入灵石数量）：'))
    player.currentSloder.getHeal(lingshi)
    player.currentSloder.killMonster(forestAnimal[forestIndex])
    if player.currentSloder.blood == 0:
        player.solder.pop(solderName)

if forestIndex == 7:
    print(player.lingshi)
else:
    print('任务失败')




