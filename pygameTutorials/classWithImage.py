import sys, pygame, time
pygame.init()
# Try to modify this class to be with Image

class OneBall:
  def __init__(self,filename,speedX,speedY,x,y) -> None:
     self.picture = pygame.image.load(filename)
     self.rect = self.picture.get_rect()
     self.ballSpeedX = speedX
     self.ballSpeedY = speedY
     self.rect.x = x
     self.rect.y = y

  def move(self):
      if self.rect.left <= 0 or self.rect.right >= width:     
        self.ballSpeedX = - self.ballSpeedX
        self.rect.x = self.rect.x + self.ballSpeedX * 9
      if self.rect.top <= 0 or self.rect.bottom >= height:   
        self.ballSpeedY = - self.ballSpeedY
        self.rect.y = self.rect.y + self.ballSpeedY * 9

      self.rect.x = self.rect.x + self.ballSpeedX
      self.rect.y = self.rect.y + self.ballSpeedY

  def collide(self, OneBall):   
      if self.rect.colliderect(OneBall.rect):
        print("Collide.")
        self.ballSpeedX = - self.ballSpeedX
        self.ballSpeedY = - self.ballSpeedY
        self.rect.x = self.rect.x + self.ballSpeedX * 10  #when collide,they back in 10 times speed
        self.rect.y = self.rect.y + self.ballSpeedY * 10

  def blit(self, screen):
    screen.blit(self.picture, self.rect)

size = width, height = 1040, 780
backgroundColor = (104,183,150)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ball Game') #  主窗口标题（Title）

ball001 = OneBall("soccer.png",4,3,520,340)
ball002 = OneBall("basketball.png",3,4,200,100)
isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.fill(backgroundColor)

  ball001.blit(screen)
  ball002.blit(screen)

  ball001.move()
  ball002.move()

  ball001.collide(ball002)
  ball002.collide(ball001)
#   ball001.collide(ball002)

  time.sleep(0.005)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
