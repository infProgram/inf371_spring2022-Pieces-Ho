from re import T
import sys, pygame, time, random
pygame.init()

class launcher():   # launcher class
    def __init__(self) -> None:    
        self.speed = 20
        self.x = 200
        self.y = 660
        self.tankColour = (154,205,50)
        self.bulletSpeed = 10
        self.bulletx = self.x+20
        self.bullety = self.y-20
        self.bulletColour = (238,201,0)
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]

    def draw(self):
        self.tank = pygame.draw.polygon(screen, self.tankColour,self.points)
        self.tankFrame = pygame.draw.polygon(screen, (46,139,87), self.points, width=2)

    def move(self,key):
        if key == 'A': self.x = self.x - self.speed
        if key == 'D': self.x = self.x + self.speed
      
        if self.x < -21 :  self.x = -20
        if self.x > width-40: self.x = width-40
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]


class bullet():   # bullet class
    def __init__(self) -> None:
        self.bulletSpeed = 20
        self.bulletx = 0
        self.bullety = 0
        self.bulletColour = (238,201,0)
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)

    def startBullet(self,x,y):
        print("press W! ")
        self.bulletx = x+20
        self.bullety = y-20
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[x+20,y-20,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)

    def bulletFlyDraw(self):
        self.bullety = self.bullety - self.bulletSpeed
        print("x: ",self.bulletx, ",y: ",self.bullety)
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)
        

class wall():
    def __init__(self) -> None:
        self.wallColour = (139,58,58)
        self.posx = [random.sample(range(0,460,20),15),random.sample(range(0,460,20),random.randint(12, 15)),random.sample(range(0,460,20),13),random.sample(range(0,460,20),14),random.sample(range(0,460,20),15)]

    def draw(self):     # 23 grids each line, and 34 lines, 34-2 = 32
        for i in range(len(self.posx)):      
            # print("Line: ",i, end="  ")
            # print("in: ",self.posx[i])
            for j in self.posx[i]:
                self.walls = pygame.draw.rect(screen,self.wallColour,[j,i*20,20,20],0)
        if len(self.posx) >=  32:
            print("Game over!")
            sys.exit()
        
    def move(self):
        self.posx.insert(0,random.sample(range(0,460,20),random.randint(12, 15)))

    def clearline(self):
        for i in range(0,len(self.posx)):      
            if len(self.posx[i]) == 23:
                del self.posx[i]

    def addPiece(self,x,y):
        print("x: ",x, ",y: ",y)
        for i in range(len(self.posx)):      
            for j in self.posx[i]:
                if x == j  and y == i*20 : 
                    print("----insert= line: ",i+1, ",y: ",x)
                    # self.posx.insert(i+1,x)
                    self.posx[i+1].append(x)
                    
                    return False

        return True


size = width, height = 460, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）
backgroundPic = pygame.image.load("bgPic.png")
mylancher = launcher()
mywall = wall()
mybullet = bullet()
wallWhile = 0
boolBulletFly = False
bulleyStayFlag = True

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN: 
        keyPressed =  pygame.key.get_pressed()
        if keyPressed[pygame.K_w]: 
            mybullet.startBullet(mylancher.x,mylancher.y)
            boolBulletFly = True
            bulleyStayFlag = True
        if keyPressed[pygame.K_a]: mylancher.move('A')
        if keyPressed[pygame.K_d]: mylancher.move('D')
  screen.blit(backgroundPic,(0,0))

  if wallWhile == 70:  # wall move speed in smaller while
      mywall.move()
      wallWhile = 0
  wallWhile = wallWhile+1
  mywall.draw() # Draw wall with xy lines

  for i in range(20,441,20): pygame.draw.line(screen,(112,128,144),[i,0],[i,680],1) # Draw xy lines
  for i in range(20,681,20): pygame.draw.line(screen,(112,128,144),[0,i],[460,i],1)

  mywall.clearline()
  mylancher.draw()  # Draw lancher without xy lines
  if  mybullet.bullety >0 and bulleyStayFlag == True and boolBulletFly == True: 
      mybullet.bulletFlyDraw()
      if mywall.addPiece(mybullet.bulletx,mybullet.bullety) ==  False: 
          bulleyStayFlag = False
  if  mybullet.bullety <= 0 or bulleyStayFlag == False:    
      boolBulletFly == False



  


  time.sleep(0.01)
  pygame.display.flip()  # 刷新整个界面显示