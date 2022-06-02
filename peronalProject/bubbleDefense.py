import sys, pygame, time
pygame.init()

size = width, height = 460, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）
backgroundPic = pygame.image.load("bgPic.png")

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.blit(backgroundPic,(0,0))


  time.sleep(0.007)
  pygame.display.flip()  # 刷新整个界面显示