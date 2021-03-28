import pygame as pyg
import random as rndm
import time


class SortVisual():
    def __init__(self, arraySize = 100):
        pyg.font.init()
        self.arraySize = arraySize
        self.backgroundColor = (255,255,255)
        self.width = 1000
        self.height = 800
        self.screen = pyg.display.set_mode((self.width, self.height))
        pyg.display.set_caption('Sort')
        self.screen.fill(self.backgroundColor)
        pyg.display.flip()
        self.running = True
        self.cooldown = 30 
        self.color = (0, 0, 0)
        self.tickrate = 300
        self.clock = pyg.time.Clock()
        self.curElem = 0
        self.comparisons = 0
        self.mainFont = pyg.font.SysFont('arial', 20)
        self.tickModifier = 10
        self.tickColor = (0, 0, 0)
        self.smallerNumber = 50
        self.greaterNumber = 100
        self.sizeColor = (0, 0, 0)
        self.setOff = 0
        self.hiddenComparison = 0
        self.elapsedTime = '00:00'
        self.start = 0
        self.timerColor = (0, 0, 0)
        self.test = 0
        self.a = 0

        
    def main(self):
        self.bubble = False
        self.insertion = False
        self.brick = False

        self.createShapes(size = self.arraySize)

        while self.running:
            self.clock.tick(self.tickrate)
            self.keys = pyg.key.get_pressed()
            
            if self.keys[pyg.K_DOWN]:
                if self.tickrate -  self.tickModifier > 0:
                    self.tickrate -=  self.tickModifier
                    self.tickColor = (255, 0, 0)
            
            elif self.keys[pyg.K_UP]:
                if self.tickrate +  self.tickModifier <= 1000:
                    self.tickrate +=  self.tickModifier
                    self.tickColor = (0, 255, 0)
            
            else:
                self.tickColor = (0, 0, 0)
            
            if self.keys[pyg.K_LEFT]:
                if self.arraySize - 10 >= 10:
                    self.arraySize -= 10
                    self.sizeColor = (255, 0, 0)
                    if self.setOff <= self.width + 50:
                        self.setOff += 10
                
                self.elapsedTime = 0
                self.comparisons = 0
                self.resetVariables()
                self.createShapes(self.arraySize)

            elif self.keys[pyg.K_RIGHT]:
                if self.arraySize + 10 <= 1000:
                    self.arraySize += 10
                    self.sizeColor = (0, 255, 0)
                    if self.setOff > 0:
                        self.setOff -= 10
                
                self.resetVariables()
                self.createShapes(self.arraySize)
            
            else:
                self.sizeColor = (0, 0, 0)
             
            if self.keys[pyg.K_r]:
                self.screen.fill((255, 255, 255))
                self.createShapes(self.arraySize)
                self.resetVariables()

            if self.keys[pyg.K_SPACE]:
                self.bubble = False
                self.insertion = False
                self.brick = False
                self.timerColor = (0, 0, 0)
                self.comparisons = 0

            if self.keys[pyg.K_1]:
                self.bubble = True
                self.insertion = False
                self.brick = False
                self.start = time.time()
                self.timerColor = (0, 255, 0)
            
            if self.keys[pyg.K_2]:
                self.insertion = True
                self.bubble = False
                self.brick = False
                self.start = time.time()
                self.timerColor = (0, 255, 0)
            
            if self.keys[pyg.K_3]:
                self.brick = True
                self.bubble = False
                self.insertion = False
                self.start = time.time()
                self.timerColor = (0, 255, 0)

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.running = False
            
            if self.bubble:
                self.bubbleSort()
                
            if self.insertion:
                self.insertionSort()
            
            if self.brick:
               self.a = self.brickSort(self.shapeList)
                
            self.update()
    
    def bubbleSort(self):
        try:
            if self.shapeList[self.curElem][0][3] > self.shapeList[self.curElem + 1][0][3]:
                self.shapeList[self.curElem][0][3], self.shapeList[self.curElem + 1][0][3] = self.shapeList[self.curElem + 1][0][3], self.shapeList[self.curElem][0][3]
                self.shapeList[self.curElem + 1][1] = (0, 0, 0)
                self.comparisons += 1

            if self.curElem + 1 <= len(self.shapeList):
                self.comparisons += 1
                self.curElem += 1
        
        except IndexError:
            self.curElem = 0
        
        self.checkIfSorted()

    def insertionSort(self):
        for i in range(1, len(self.shapeList)):
            key = self.shapeList[i][0][3]
            j = i - 1
            self.test = i - 1

            if j >= 0 and key < self.shapeList[j][0][3]:
                self.shapeList[j + 1][0][3] = self.shapeList[j][0][3]
                j -= 1
                self.test -= 1
                self.comparisons += 1
                self.hiddenComparison += 1
            
            self.shapeList[j + 1][0][3] = key
            self.check = True

        self.checkIfSorted()

    def brickSort(self, array):
        isSorted = 0
        length = len(array)

        if isSorted == 0:
            isSorted = 1

            for i in range(1, length - 1, 2):
                if array[i][0][3] > array[i + 1][0][3]:
                    self.comparisons += 1
                    array[i][0][3], array[i+1][0][3] = array[i + 1][0][3], array[i][0][3] 
                    isSorted = 0
            
            for i in range(0, length-1, 2): 
                if array[i][0][3] > array[i + 1][0][3]: 
                    self.comparisons += 1
                    array[i][0][3], array[i+1][0][3] = array[i + 1][0][3], array[i][0][3]
                    isSorted = 0
        
        self.checkIfSorted()

    def resetVariables(self):
        self.bubble = False
        self.insertion = False
        self.brick = False

        self.comparisons = 0
        self.elapsedTime = 0
        self.timerColor = (0, 0, 0)

    def createShapes(self, size = 400):
        self.shapeList = []

        heightChoices = [i for i in range(2, size + 2)]
      
        for i in range(size):
            height = rndm.choice(heightChoices)
            heightChoices.remove(height)

            self.shapeList.append([pyg.Rect(i + self.setOff, 0, 3, height // 1.8), (0, 0, 0), height])

    def checkIfSorted(self):
        self.hiddenComparison = 0

        timesList = (time.ctime(time.time() - self.start))
        tmpTime = timesList.split(':')
        secs = (tmpTime[2].split()[0])

        self.elapsedTime = f'{tmpTime[1]}:{secs}'

        for i in range(1, len(self.shapeList)):
            key = self.shapeList[i][0][3]
            j = i - 1
            
            if j >= 0 and key < self.shapeList[j][0][3]:
                j -= 1
                self.hiddenComparison += 1
        
        if self.hiddenComparison == 0:
            
            for i in range(self.arraySize):
                self.shapeList[i][1] = (0, 255, 0)
            

            self.createLog()

            self.bubble = False
            self.insertion = False
            self.brick = False
            self.timerColor = (0, 0, 0)

    def createLog(self):
        with open('Log.txt', 'a+') as file:
            if self.bubble:
                sortType = 'Bubble-Sort'
            
            if self.insertion:
                sortType = 'Insertion-Sort'

            if self.brick:
                sortType = 'Brick-Sort'
            
            file.write(f'{sortType} | Time: {self.elapsedTime} | Array-Size: {self.arraySize} | Comparisons: {int(self.comparisons / 100)} | Tickrate: {self.tickrate}\n')
            
    def update(self):
        self.screen.fill((255, 255, 255))
        
        for index in range(len(self.shapeList)):
            if index == self.curElem and self.bubble:
                self.shapeList[index][1] = (255, 0, 0)

            elif index == self.a and self.brick:
                self.shapeList[index][1] = (255, 0, 0)

                if not index + 1 <= len(self.shapeList):
                    self.shapeList[index + 1][1] = (255, 0, 0)

            else:
                self.shapeList[index][1] = (0, 0, 0)

                if not index + 1 <= len(self.shapeList):
                    self.shapeList[index + 1][1] = (0, 0, 0)
            
            pyg.draw.rect(self.screen, self.shapeList[index][1], self.shapeList[index][0])

        self.screen.blit(pyg.transform.rotate(self.screen, 180), (1, 0))
        self.comparisonText = self.mainFont.render(f'Comparisons: {int(self.comparisons / 100)}', 1, (0, 0, 0))
        self.screen.blit(self.comparisonText, (450, 10))

        if self.bubble:
            colorForBubble = (0, 255, 0)

        else:
            colorForBubble = (255, 0, 0)
        
        if self.insertion:
            colorForInsertion = (0, 255, 0)
        
        else:
            colorForInsertion = (255, 0, 0)
        
        if self.brick:
            colorForBrick = (0, 255, 0)
        
        else:
            colorForBrick = (255, 0, 0)
        
        self.infoText = self.mainFont.render(f'1: Bubble-Sort ({self.bubble})', 1, colorForBubble)
        self.infoText2 = self.mainFont.render(f'2: Insertion-Sort ({self.insertion})', 1, colorForInsertion)
        self.infoText3 = self.mainFont.render(f'3: Brick-Sort ({self.brick})', 1, colorForBrick)
        self.infoText4 = self.mainFont.render(f'Tickrate: ({self.tickrate})', 1, self.tickColor)
        self.infoText5 = self.mainFont.render(f'Array size: ({self.arraySize})', 1, self.sizeColor)
        self.infoText6 = self.mainFont.render(f'Time: ({self.elapsedTime})', 1, self.timerColor)
        self.infoText7 = self.mainFont.render(f'Pause: (Space)', 1, (0, 0, 0))
        self.infoText8 = self.mainFont.render(f'Scramble: (R)', 1, (0, 0, 0))


        self.screen.blit(self.infoText, (10, 10))
        self.screen.blit(self.infoText2, (10, 30))
        self.screen.blit(self.infoText3, (10, 50))
        self.screen.blit(self.infoText4, (10, 70))
        self.screen.blit(self.infoText5, (10, 90))
        self.screen.blit(self.infoText6, (10, 110))
        self.screen.blit(self.infoText7, (self.width - 120, 10))
        self.screen.blit(self.infoText8, (self.width - 120, 30))

        pyg.display.update()

if __name__ == '__main__':
    arraySize = 900
    SortVisual(arraySize).main()