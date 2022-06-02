import sys, pygame, time
pygame.init()
# launcher class
class launcher():
    def __init__(self) -> None:    
        self.speed = 20
        self.x = 200
        self.y = 660
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]
        self.tank = pygame.draw.polygon(screen, (102,153,102),self.points)
        self.tankFrame = pygame.draw.polygon(screen, (46,139,87), self.points, width=2)

    def draw(self):
        self.tank = pygame.draw.polygon(screen, (102,153,102),self.points)
        self.tankFrame = pygame.draw.polygon(screen, (46,139,87), self.points, width=2)
    def move(self,key):
        if key == 'W': pass
        if key == 'A': self.x = self.x - self.speed
        if key == 'D': self.x = self.x + self.speed
        print("x: ",self.x, ",y: ",self.y)

        if self.x <= 0 :  self.x = 0
        if self.x >= width-60: self.x = width-60
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]
        





size = width, height = 460, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）
backgroundPic = pygame.image.load("bgPic.png")
mylancher = launcher()

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
        keyPressed =  pygame.key.get_pressed()
        if keyPressed[pygame.K_w]: mylancher.move('W')
        if keyPressed[pygame.K_a]: mylancher.move('A')
        if keyPressed[pygame.K_d]: mylancher.move('D')
  screen.blit(backgroundPic,(0,0))
  for i in range(20,441,20): pygame.draw.line(screen,(112,128,144),[i,0],[i,680],1) # Draw xy lines
  for i in range(20,681,20): pygame.draw.line(screen,(112,128,144),[0,i],[460,i],1)

  mylancher.draw()

  time.sleep(0.01)
  pygame.display.flip()  # 刷新整个界面显示