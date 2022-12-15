import pygame
from config import *
from stages import *
import math

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', int(SIZE * 0.3))

# Draws health bar (general function used for enemies and towers)
def draw_health(position, size, border_color, bar_color, progress, SCREEN):
    pygame.draw.rect(SCREEN, border_color, (position, size), 1)
    inner_position = (position[0] + 2, position[1] + 2)
    inner_size = ((size[0] - 4) * progress, size[1] - 4)
    pygame.draw.rect(SCREEN, bar_color, (inner_position, inner_size))

# Create enemy class
class Enemy(pygame.sprite.Sprite):
  def __init__(self, health, speed, damage, x, y, image, frozen):
    pygame.sprite.Sprite.__init__(self)
    self.maxhealth = health
    self.currhealth = health
    self.speed = speed
    self.damage = damage
    self.position = (x, y)
    self.image = image
    self.rect = self.image.get_rect()
    self.frozen = 0

  # Check if enemy has reached leftmost border of screen
  def reachEnd(self):
      if self.position[0] <= SIZE:
        self.kill()
        return True
      return False

  def draw(self, SCREEN):
    self.rect.x = self.position[0] * SIZE
    self.rect.y = self.position[1] * SIZE
    SCREEN.blit(self.image, self.rect)
    
    draw_health((self.rect.x, self.rect.y), (SIZE, SIZE/6), (255, 255, 255), (255, 80, 80), self.currhealth / self.maxhealth, SCREEN)

  def move(self, frozen):
    if not(self.rect.x < SIZE-1) and (self.frozen == 0):
      self.position = (self.position[0] - self.speed, self.position[1])
    else:
      pass
      
  def damage(self, damage):
    self.currhealth -= damage

  def die(self):
    if self.currhealth <= 0:
      self.kill()

# Create tower class
class Tower(pygame.sprite.Sprite):
  def __init__(self, x, y, plant):
    pygame.sprite.Sprite.__init__(self)
    stats = TOWERS[plant]
    self.maxhealth = stats[0]
    self.currhealth = stats[0]
    self.speed = stats[1]
    self.damage = stats[2]
    self.position = (x, y)
    self.image = stats[3]
    self.counter = 0
    self.rect = self.image.get_rect()
  
  def draw(self, SCREEN):
    self.counter += 1
    self.rect.x = self.position[0] * SIZE
    self.rect.y = self.position[1] * SIZE
    SCREEN.blit(self.image, self.rect)
    
    draw_health((self.rect.x, self.rect.y), (SIZE, SIZE/6), (255, 255, 255), (153, 204, 255), self.currhealth/self.maxhealth, SCREEN)

  def die(self):
    if self.currhealth <= 0:
      self.kill()
      GRID[self.position[1] - 1][self.position[0] - 1] = "NULL"

# Create packet class
class Packet(pygame.sprite.Sprite):
  def __init__(self, x, y, cost, image):
    pygame.sprite.Sprite.__init__(self)
    self.position = (x, y)
    self.cost = cost
    self.image = image
    self.rect = self.image.get_rect()
    
  def draw(self, SCREEN):
    self.rect.x = self.position[0] * SIZE
    self.rect.y = self.position[1] * SIZE
    SCREEN.blit(self.image, self.rect)
    coinsText = font.render(f'${self.cost}', True, (0, 0, 0))
    coinRect = coinsText.get_rect()
    coinRect.bottom = self.rect.bottom
    coinRect.centerx = self.rect.centerx
    SCREEN.blit(coinsText, coinRect)

# Create bullet class
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x , y, damage, speed, image):
    pygame.sprite.Sprite.__init__(self)
    self.position = (x,y)
    self.damage = damage
    self.image = image
    self.speed = speed
    self.rect = self.image.get_rect()
  
  def draw(self, SCREEN):
    if self.image == BULLET:
      self.rect.x = self.position[0] * SIZE
      self.rect.y = self.position[1] * SIZE
    else:
      self.rect.x = self.position[0] * SIZE - SIZE
      self.rect.y = self.position[1] * SIZE - SIZE

    SCREEN.blit(self.image, self.rect)
  
  def move(self):
    if not(self.rect.x > 12 * SIZE):
      self.position = (self.position[0] + self.speed, self.position[1])
    else:
      self.kill()
  
  def die(self):
    self.kill()