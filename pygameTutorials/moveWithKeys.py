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

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: sys.exit()
    # control key ball
  keyPressed =  pygame.key.get_pressed()
  if keyPressed[pygame.K_w]: ball_rect.y = ball_rect.y - speedY
  if keyPressed[pygame.K_s]: ball_rect.y = ball_rect.y + speedY
  if keyPressed[pygame.K_a]: ball_rect.x = ball_rect.x - speedX
  if keyPressed[pygame.K_d]: ball_rect.x = ball_rect.x + speedX
  screen.fill(backgroundColor)

  if ball_rect.left <= 0 or ball_rect.right >= width:  ASx = - ASx
  if ball_rect.top <= 0 or ball_rect.bottom >= height:   ASy = - ASy

  screen.blit(ball_key,ball_rect)

  time.sleep(0.002)
  pygame.display.flip()  # 刷新整个界面显示  # pygame.display.update(_) 刷新指定部分显示
