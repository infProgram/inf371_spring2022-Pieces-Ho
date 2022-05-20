import sys, pygame, random
pygame.init()


size = width, height = 640, 480
ballSpeed = [2, 2]
backgroundColor = (104,183,150)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption('Ball Game') #主窗口标题

x = y = 200
# ballSurface = pygame.Surface((150,150))
# ballRect = ballSurface.get_rect()

# ball = pygame.draw.circle(ballSurface, (133,233,23), [60, 250], 40, width=0)
# ballpict = pygame.draw.circle(ballSurface, (133,233,23), [60, 250], 40, width=0)

testSurface = pygame.Surface((200,200))
testRect = pygame.Rect(50, 50, 30, 50)
test = pygame.draw.rect(testSurface, (123,133,0), testRect)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    # if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        sys.exit()
      if event.key == pygame.K_w:       # w键，控制1号玩家向上移动
        y = y-10
      if event.key == pygame.K_s:       # s键，控制1号玩家向下移动
        y = y+10
      if event.key == pygame.K_a:      # 上键头，控制2号玩家向上移动
        x = x-10
      if event.key == pygame.K_d:    # 下键头，控制2号玩家向下移动
        x = x+10

  screen.fill(backgroundColor)
  ball = pygame.draw.circle(screen, (162,56,31), [x, y], 40, width=0)
  frame = pygame.draw.circle(screen, (0,0,0), [x, y], 40, width=5)

  if ball.



  # screen.blit(testSurface, testRect)  # 新矩形对象粘在主窗口上（图像，坐标）
  # screen.blit(ballSurface,ballRect)
  
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
