import sys, pygame, time, random
pygame.init()

class launcher():   # launcher class
    def __init__(self) -> None:     # set speed, inital xy, colour, frameColour and keypoints
        self.speed = 20
        self.x = 200
        self.y = 660
        self.tankColour = (154,205,50)
        self.tankFrameColour = (46,139,87)
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]

    def draw(self):     # draw the launcher
        self.tank = pygame.draw.polygon(screen, self.tankColour,self.points)
        self.tankFrame = pygame.draw.polygon(screen, self.tankFrameColour, self.points, width=2)

    def move(self,key):          # move the launcher
        if key == 'A': self.x = self.x - self.speed
        if key == 'D': self.x = self.x + self.speed
      
        if self.x < -21 :  self.x = -20     # make sure the tank will not out the window.
        if self.x > width-40: self.x = width-40
        self.points = [(self.x,self.y),(self.x+20,self.y),(self.x+20,self.y-20),(self.x+40,self.y-20),(self.x+40,self.y),(self.x+60,self.y),(self.x+60,self.y+20),(self.x,self.y+20)]


class bullet():   # bullet class
    def __init__(self) -> None:     # set speed, inital xy and colour
        self.bulletSpeed = 20
        self.bulletx = 0
        self.bullety = 0
        self.bulletColour = (238,201,0)

    def startBullet(self,x,y):     # when press 'W', draw the bullet from top of launcher
        print("press W! ")
        self.bulletx = x+20
        self.bullety = y-20
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)

    def bulletFlyDraw(self):    # after press 'W', bullet fly up
        self.bullety = self.bullety - self.bulletSpeed
        self.bullet = pygame.draw.rect(screen,self.bulletColour,[self.bulletx,self.bullety,20,20],0)
        self.bulletFrame = pygame.draw.rect(screen,(139,121,94),[self.bulletx,self.bullety,20,20],1)
        

class wall():   # wall class
    def __init__(self) -> None:     # set colour, and initial 5 lines wall by random(the wall store in 2D array).
        self.wallColour = (139,58,58)
        self.posx = [random.sample(range(0,460,20),15),random.sample(range(0,460,20),16),random.sample(range(0,460,20),17),random.sample(range(0,460,20),18),random.sample(range(0,460,20),18)]

    def draw(self):       # draw wall by 2D array, return gameover or not
        for i in range(len(self.posx)):      
            for j in self.posx[i]:
                self.walls = pygame.draw.rect(screen,self.wallColour,[j,i*20,20,20],0)
        if len(self.posx) >=  33:   # check gameover, there are 23 grids each line, and 34 lines, 34-2+1 = 33
            return True
        else: return False
        
    def move(self):     # move down the wall, which is equivalent to adding row 0
        self.posx.insert(0,random.sample(range(0,460,20),random.randint(15, 20)))

    def clearline(self):    # when a line is full, clear it.
        i = 0
        while(i < len(self.posx)):
            if len(self.posx[i]) >= 23:
                del self.posx[i]
                i = i-1
            i = i+1

    def addPiece(self,x,y):     # when bullet arrive, it becomes a new pieces of wall
        for i in range(len(self.posx)):      
            for j in self.posx[i]:
                if x == j  and y == i*20 : 
                    if i+1 < len(self.posx):   self.posx[i+1].append(x)
                    else:  self.posx.insert(i+1,[x])
                    return False
        return True


size = width, height = 460, 680     # screen size, title, and back picture 
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense')
backgroundPic = pygame.image.load("bgPic.png")
fallTime = 550  # time of the wall fall down, it smaller, game harder.
mylancher = launcher()  # 3 instance of class
mywall = wall()
mybullet = bullet()
wallWhile = 0   # time of wall fall start from 0
boolBulletFly = False   # bool make bullet fly or not
bulleyStayFlag = True   # bool make bullet stay or not
font = pygame.font.SysFont('Lucida Grande', 75)     # the text size, style of GameOver
text = font.render('Game Over!', True, (0, 0, 0))

pressA = False
pressD = False

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    
    if event.type == pygame.KEYDOWN:    # control with 'W', 'A', 'D' in game 
        keyPressed =  pygame.key.get_pressed()
        if keyPressed[pygame.K_w]: 
            mybullet.startBullet(mylancher.x,mylancher.y)
            boolBulletFly = True
            bulleyStayFlag = True
        if keyPressed[pygame.K_a]: mylancher.move('A')
        if keyPressed[pygame.K_d]: mylancher.move('D')
 
        # # pygame.key.set_repeat(0,1)
        # pygame.key.set_repeat(pygame.KEYDOWN)
        # keyRepeat = pygame.key.get_pressed()
        # if keyRepeat[pygame.K_a]: mylancher.move('A')
        # if keyRepeat[pygame.K_a]:  mylancher.move('D')

    # pygame.key.set_repeat(0,1)
    pygame.key.set_repeat(pygame.KEYDOWN)
    keyRepeat = pygame.key.get_pressed()
    if keyRepeat[pygame.K_a]: mylancher.move('A')
    if keyRepeat[pygame.K_a]:  mylancher.move('D')


#     if event.type == pygame.KEYDOWN:    # control with 'W', 'A', 'D' in game 
#         keyPressed =  pygame.key.get_pressed()
#         if keyPressed[pygame.K_w] : 
#             mybullet.startBullet(mylancher.x,mylancher.y)
#             boolBulletFly = True
#             bulleyStayFlag = True

#         if keyPressed[pygame.K_a] and pressA == False: 
#             pressA = True
#             print("PPpress A! ")
#         if keyPressed[pygame.K_d] and pressD == False: 
#             pressD = True
#             print("PPpress D! ")
#     elif event.type == pygame.KEYUP:
#         if event.key == pygame.K_a : pressA = False
#         if event.key == pygame.K_d : pressD = False
#         print(" in False")
#     # print("when in it boolA: ", pressA, " boolD: ", pressD)
#   if pressA == True:    
#         mylancher.move('A')
#         print("move A")
#         time.sleep(0.03)
#   if pressD == True:    
#         mylancher.move('D')
#         time.sleep(0.03)


    # if event.type == pygame.KEYDOWN:    # control with 'W', 'A', 'D' in game 
    #     keyPressed =  pygame.key.get_pressed()
    #     if keyPressed[pygame.K_w]: 
    #         mybullet.startBullet(mylancher.x,mylancher.y)
    #         boolBulletFly = True
    #         bulleyStayFlag = True
    #     if keyPressed[pygame.K_a]: mylancher.move('A')
    #     if keyPressed[pygame.K_d]: mylancher.move('D')

  screen.blit(backgroundPic,(0,0))

  if wallWhile == fallTime and boolOver == False:  # wall move speed in smaller while
      mywall.move()
      wallWhile = 0
  wallWhile = wallWhile+1
  boolOver = mywall.draw() # Draw wall with xy lines

  for i in range(20,441,20): pygame.draw.line(screen,(112,128,144),[i,0],[i,680],1) # Draw xy lines
  for i in range(20,681,20): pygame.draw.line(screen,(112,128,144),[0,i],[460,i],1)

  mywall.clearline()    # check whether the line is full
  mylancher.draw()  # Draw lancher without xy lines

  if  mybullet.bullety >0 and bulleyStayFlag == True and boolBulletFly == True:     # after press 'W', bullet fly
      mybullet.bulletFlyDraw()
      if mywall.addPiece(mybullet.bulletx,mybullet.bullety) ==  False: 
          bulleyStayFlag = False
  if  mybullet.bullety <= 0 or bulleyStayFlag == False:    
      boolBulletFly == False

  if boolOver:  # Print Game over
      screen.blit(text, (90, 220))
      time.sleep(1)

  time.sleep(0.001)
  pygame.display.flip()  # 刷新整个界面显示