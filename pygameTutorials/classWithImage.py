import sys, pygame, time
pygame.init()

class OneBall:
  def __init__(self,speedX,speedY,x,y,colour) -> None:
     self.ballSpeedX = speedX
     self.ballSpeedY = speedY
     self.x = x
     self.y = y
     self.ballColour = colour
     self.ball = pygame.draw.circle(screen, self.ballColour, [self.x, self.y], 40, width=0)
     self.ballFrame = pygame.draw.circle(screen, (0,0,0), [self.x, self.y], 40, width=5)
     
  def draw(self):
    self.ball = pygame.draw.circle(screen, self.ballColour, [self.x, self.y], 40, width=0)
    self.ballFrame = pygame.draw.circle(screen, (0,0,0), [self.x, self.y], 40, width=5)

  def move(self):
      if self.ball.left <= 0 or self.ball.right >= width:     
        self.ballSpeedX = - self.ballSpeedX
      if self.ball.top <= 0 or self.ball.bottom >= height:   
        self.ballSpeedY = - self.ballSpeedY

      self.x = self.x + self.ballSpeedX
      self.y = self.y + self.ballSpeedY

  def collide(self, OneBall):
    
      if self.ball.colliderect(OneBall.ball):
        print("Collide.")
        self.ballSpeedX = - self.ballSpeedX
        self.ballSpeedY = - self.ballSpeedY
        self.x = self.x + self.ballSpeedX * 10  #when collide,they back in 10 times speed
        self.y = self.y + self.ballSpeedY * 10

size = width, height = 640, 480
backgroundColor = (104,183,150)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ball Game') #  主窗口标题（Title）

ball001 = OneBall(2,2,320,240,(162,56,31))
ball002 = OneBall(3,4,200,100,(255,255,255))
isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.fill(backgroundColor)

  ball001.draw()
  ball002.draw()
  ball001.move()
  ball002.move()
  ball002.collide(ball001)
  ball001.collide(ball002)

  time.sleep(0.009)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示