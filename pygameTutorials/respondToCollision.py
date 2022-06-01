import sys, pygame, time, random
pygame.init()

size = width, height = 640, 480
backgroundColor = (104,183,150) # green background looks like basketball court
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ball Game') #  主窗口标题（Title）

Asite = Ax,Ay = 320,240
Bsite = Bx,By = 200,100
Aspeed = ASx,ASy = 2,2
Bspeed = BSx,BSy = 3,4

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
  screen.fill(backgroundColor)

  ballA = pygame.draw.circle(screen, (162,56,31), [Ax,Ay], 40, width=0)
  ballA_Frame = pygame.draw.circle(screen, (0,0,0), [Ax,Ay], 40, width=5)
  ballB = pygame.draw.circle(screen, (255,255,255), [Bx,By], 40, width=0)
  ballB_Frame = pygame.draw.circle(screen, (0,0,0), [Bx,By], 40, width=5)

  if ballA.left <= 0 or ballA.right >= width:  
      ASx = - ASx
      Ax = Ax + ASx * 4
  if ballA.top <= 0 or ballA.bottom >= height:   
      ASy = - ASy
      Ay = Ay + ASy * 4
  Ax = Ax + ASx
  Ay = Ay + ASy

  if ballB.left <= 0 or ballB.right >= width:  BSx = - BSx
  if ballB.top <= 0 or ballB.bottom >= height:   BSy = - BSy
  Bx = Bx + BSx
  By = By + BSy

  if ballA.colliderect(ballB):
    print("Collide.")
    ASx = random.choice((-1, 1))* random.randint(2,5)
    ASy = random.choice((-1, 1))* random.randint(2,5)
    BSx = random.choice((-1, 1))* random.randint(2,5)
    BSy = random.choice((-1, 1))* random.randint(2,5)
    Ax = Ax + ASx * 5  #when collide,they back in 5 times speed
    Ay = Ay + ASy * 5
    Bx = Bx + BSx * 5  
    By = By + BSy * 5

  time.sleep(0.005)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
