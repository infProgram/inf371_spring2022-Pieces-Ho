import sys, pygame, time
pygame.init()

class OneBall:
  def __init__(self,speedX,speedY,x,y,colour) -> None:
     self.ballSpeedX = speedX
     self.ballSpeedY = speedY
     self.x = x
     self.y = y
     self.ball = pygame.draw.circle(screen, colour, [x, y], 40, width=0)
     self.ballFrame = pygame.draw.circle(screen, (0,0,0), [x, y], 40, width=5)

  def move(self):
      if self.ball.left <= 0 or self.ball.right >= width:     #如果球碰到左或者右边缘，就将球横向速度取反
        self.ballSpeedX = - self.ballSpeedX
      if self.ball.top <= 0 or self.ball.bottom >= height:    #如果球碰到左或者右边缘，就将球纵向速度取反
        self.ballSpeedY = - self.ballSpeedY

      x = x + self.ballSpeedX
      y = y + self.ballSpeedY



#ballSpeed = [2, 2]
size = width, height = 640, 480
backgroundColor = (104,183,150)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ball Game') #主窗口标题

# x = 320
# y = 240

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  
  screen.fill(backgroundColor)

  ball001 = OneBall

  # ball = pygame.draw.circle(screen, (162,56,31), [x, y], 40, width=0)
  # frame = pygame.draw.circle(screen, (0,0,0), [x, y], 40, width=5)
  
  # if ball.left <= 0 or ball.right >= width:     #如果球碰到左或者右边缘，就将球横向速度取反
  #       ballSpeed[0] = - ballSpeed[0]
  # if ball.top <= 0 or ball.bottom >= height:    #如果球碰到左或者右边缘，就将球纵向速度取反
  #       ballSpeed[1] = - ballSpeed[1]

  # x = x+ballSpeed[0]
  # y = y+ballSpeed[1]



  time.sleep(0.009)
  
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
