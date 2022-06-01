print("Hello ball moving with Mouse.")

import sys, pygame, time
pygame.init()
# Try to modify this class to be with Image

size = width, height = 1040, 780
backgroundColor = (104,183,150)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ball Game') #  主窗口标题（Title）

# key ball
site = x,y = 200,100
speedX = speedY = 3
ball_key = pygame.image.load("basketball.png")
ball_rect =ball_key.get_rect()
ball_rect.x = x
ball_rect.y = y

moving = False

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:	
        if event.button == 1: # 点击鼠标左键
            moving = True
    if event.type == pygame.MOUSEBUTTONUP: # 获取松开鼠标事件
        if event.button == 1: # 松开鼠标左键
            moving = False
    if moving:
        ball_rect.x,ball_rect.y = pygame.mouse.get_pos()

  speedX = speedY = 3
  screen.fill(backgroundColor)

  if ball_rect.left <= 0 or ball_rect.right >= width:  speedX = - speedX
  if ball_rect.top <= 0 or ball_rect.bottom >= height:   speedY = - speedY

  screen.blit(ball_key,ball_rect)

  time.sleep(0.002)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
