import sys, pygame, random
pygame.init()

class Item():
  # Constructor
  def __init__(self, filename, screenSize, speed): # self is like this
    # self is always the first argument in a method (function)
    self.picture = pygame.image.load(filename)
    self.rect = self.picture.get_rect()
    self.width = screenSize[0]
    self.height = screenSize[1]
    self.speed = speed
    self.randomPosition()

  def move(self):
    self.rect = self.rect.move(self.speed)
    if self.rect.left < 0 or self.rect.right > self.width:
      self.speed[0] = -self.speed[0]
    if self.rect.top < 0 or self.rect.bottom > self.height:
      self.speed[1] = -self.speed[1]

  def moveAmount(self, amount):
    self.rect = self.rect.move(amount)

  def moveToPosition(self, position):  
    self.rect.x = position[0] - self.rect.w/2
    self.rect.y = position[1] - self.rect.h/2

  def blit(self, screen):
    screen.blit(self.picture, self.rect)

  def randomBounceOnCollide(self, rect):
    if self.rect.colliderect(rect):
      self.speed[0] = random.randint(-5, 5)
      self.speed[1] = random.randint(-5, 5)

  def randomPosition(self):
    self.rect.x = random.randint(0, self.width)
    self.rect.y = random.randint(0, self.height)

size = width, height = 640, 480
faceSpeed = [5, 5]
ballSpeed = [2, 2]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)
backgroundColor = (100, 100, 100)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", size, ballSpeed)
face = Item("smileyTiny.png", size, faceSpeed)

testSurface = pygame.Surface((50,50))
testRect = pygame.Rect(0, 0, 50, 50)
test = pygame.draw.rect(testSurface, blue, testRect)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  
  ball.randomBounceOnCollide(face.rect)
  face.randomBounceOnCollide(ball.rect)

  ball.move()
  face.move()
  

  screen.fill(backgroundColor)
  ball.blit(screen)
  face.blit(screen)
  screen.blit(testSurface, testRect)
  pygame.display.flip()
