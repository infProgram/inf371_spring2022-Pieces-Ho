import sys, pygame, time
pygame.init()

size = width, height = 460, 680
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bubble Defense') #  主窗口标题（Title）
backgroundPic = pygame.image.load("bgPic.png")
pointsx = [(-1,20),(460,20)]

pointsy = [(20, -1),(20, 680),(40, 680),(40, -1),(60, -1),(60, 680),(80, 680),(80, -1),(100, -1),(100, 680),(120, 680),(120, -1), 
(140, -1),(140, 680),(160, 680),(160, -1),(180, -1),(180, 680),(200, 680),(200, -1),(220, -1),(220, 680),(240, 680), 
(240, -1),(260, -1),(260, 680),(280, 680),(280, -1),(300, -1),(300, 680),(320, 680),(320, -1),(340, -1), (340, 680),
(360, 680),(360, -1),(380, -1),(380, 680),(400, 680),(400, -1),(420, -1),(420, 680),(440, 680),(440, -1)]

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.blit(backgroundPic,(0,0))
  pygame.draw.lines(screen, (112,128,144), 0, pointsx, 2)
  pygame.draw.lines(screen, (112,128,144), 0, pointsy, 2)


  time.sleep(0.007)
  pygame.display.flip()  # 刷新整个界面显示