import sys, pygame, time
pygame.init()

size = width, height = 460, 680
backgroundColor = (211,211,211) # green background looks like basketball court
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）


isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.fill(backgroundColor)


  time.sleep(0.007)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示