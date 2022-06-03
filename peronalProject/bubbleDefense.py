import sys, pygame, time, random
pygame.init()
# launcher class
class launcher():
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
        # self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        # self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)
    # def drawBullet(self):
    #     self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
    #     self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)


    def move(self,key):
        if key == 'W':  
            mybullet = bullet(self.x,self.y)
            mybullet.drawBullet()
            print("W be pressed!")
            
        if key == 'A': self.x = self.x - self.speed
        if key == 'D': self.x = self.x + self.speed
      
        if self.x <= 0 :  self.x = 0
        if self.x >= width-60: self.x = width-60
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]
        
    def bulletFly(self):
        self.bullety = self.bullety - self.bulletSpeed
        print("x: ",self.bulletx, ",y: ",self.bullety)


class bullet():
    def __init__(self,x,y) -> None:
        self.bulletSpeed = 10
        self.bulletx = x+20
        self.bullety = y-20
        self.bulletColour = (238,201,0)
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)

    def drawBullet(self):
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)

    def bulletFly(self):
        self.bullety = self.bullety - self.bulletSpeed
        print("x: ",self.bulletx, ",y: ",self.bullety)
        

class wall():
    def __init__(self) -> None:
        self.wallColour = (139,58,58)
        self.posx = [random.sample(range(0,460,20), 15),random.sample(range(0,460,20), 15),random.sample(range(0,460,20), 15),random.sample(range(0,460,20), 15)]
        self.lines = len(self.posx)
        print(self.lines)


    def draw(self):     # 13 grids each line
        for i in range(0,self.lines):
            print("i: ",i)
            for j in self.posx[i]:
                self.walls = pygame.draw.rect(screen,self.wallColour,[j,i*20,20,20],0)
        
    def move(self):
        pass
    def clear(self):
        pass


size = width, height = 460, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）
backgroundPic = pygame.image.load("bgPic.png")
mylancher = launcher()
mywall = wall()
smallWhile = 0

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
        keyPressed =  pygame.key.get_pressed()
        if keyPressed[pygame.K_w]: 
            mybullet = bullet(mylancher.x,mylancher.y)
            mybullet.drawBullet()
            # mylancher.move('W')
        if keyPressed[pygame.K_a]: mylancher.move('A')
        if keyPressed[pygame.K_d]: mylancher.move('D')
  screen.blit(backgroundPic,(0,0))

#   if smallWhile == 100:  # make a smaller while
#       mywall.draw()
#       pygame.draw.circle(screen, (0,0,0), [250, 200], 40, width=0)
#       smallWhile = 0
#   smallWhile = smallWhile+1
#   print("SmW: " , smallWhile)


  mywall.draw()

  for i in range(20,441,20): pygame.draw.line(screen,(112,128,144),[i,0],[i,680],1) # Draw xy lines
  for i in range(20,681,20): pygame.draw.line(screen,(112,128,144),[0,i],[460,i],1)

  mylancher.draw()  # lancher without xy lines
  #   if  mylancher.bullety >0: 
  #      mylancher.bulletFly()


  time.sleep(0.01)
  pygame.display.flip()  # 刷新整个界面显示