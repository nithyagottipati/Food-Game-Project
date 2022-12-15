import pygame
import sys
from config import *
from random import randint, random
from classes import *
from stages import *
from math import floor

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', int(SIZE * 0.3))

# Draw the grid
def draw_grid():
  top = (0, 102, 0)
  bottom = (0, 102, 0)
  side = (235 + randint(0, 20), 50 + randint(0, 20), 200 + randint(0, 20))
  green_1 = (169, 215, 81)
  green_2 = (162, 208, 73)
 
  # Draw top and bottom borders
  for i in range (1, WIDTH):
    topborder = pygame.Rect((i * SIZE, 0), (SIZE, SIZE))
    pygame.draw.rect(surface, top, topborder)
    bottomborder = pygame.Rect((i * SIZE, (HEIGHT - 1) * SIZE), (SIZE, SIZE))
    pygame.draw.rect(surface, bottom, bottomborder)

  # Draw left border
  for i in range (0, HEIGHT):
    leftborder = pygame.Rect((0, i * SIZE), (SIZE, SIZE))
    pygame.draw.rect(surface, side, leftborder)

  for y in range(1, HEIGHT - 1):
      for x in range(1, WIDTH):
        lawn = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
        color = green_1 if (x + y) % 2 == 0 else green_2
        pygame.draw.rect(surface, color, lawn)

  SCREEN.blit(surface, (0, 0))

  # Blitting all the stats onto the screen as well
  coinsText = font.render(f'Coins: ${COINS}', True, (255, 215, 0))
  SCREEN.blit(coinsText, (1.2 * SIZE, (HEIGHT - 0.6) * SIZE))

  livesText = font.render(f'Lives Left: {LIVES}', True, (255, 192,203))
  SCREEN.blit(livesText, (4 * SIZE, (HEIGHT - 0.6) * SIZE))

  wavesText = font.render(f'Waves Left: {WAVES}', True, (255, 192,203))
  SCREEN.blit(wavesText, (6 * SIZE, (HEIGHT - 0.6) * SIZE))

  tower_name = list(TOWERS.keys())[CLICKED_PACKET]
  if tower_name == "None Selected":
    tower_info = "Click to select"
  else:
    tower_info = TOWERS[tower_name][4]
  selectedText = font.render(f'Selected Tower: {tower_name} ({tower_info})', True, (0, 0, 0))
  SCREEN.blit(selectedText, (5.2 * SIZE, 0.2 * SIZE))

  commentText = font.render(COMMENT, True, (0, 0, 0))
  SCREEN.blit(commentText, (5.2 * SIZE, 0.6 * SIZE))

  # Blitting the seedpackets
  seedpacket1.draw(SCREEN)
  seedpacket2.draw(SCREEN)
  seedpacket3.draw(SCREEN)
  seedpacket4.draw(SCREEN)

# Terminates the game
def terminate():
  pygame.quit()
  sys.exit()

# Start a wave of enemies
def startWave(fries_num, burger_num, donut_num, spaghetti_num):
  for i in range(fries_num):
    # Fries stats
    fries = Enemy(200, 0.005, 3, 12 + (5 * random()), randint(1, 5), FRIES, 0)
    enemies.add(fries)

  for i in range(burger_num):
    # Burger stats
    burger = Enemy(500, 0.005, 2, 12 + (5 * random()), randint(1, 5), BURGER, 0)
    enemies.add(burger)

  for i in range(donut_num):
    # Donut stats
    donut = Enemy(300, 0.005, 5, 12 + (5 * random()), randint(1, 5), DONUT, 0)
    enemies.add(donut)

  for i in range(spaghetti_num):
    # Spaghetti stats
    spaghetti = Enemy(150, 0.01, 2, 12 + (5 * random()), randint(1, 5), SPAGHETTI, 0)
    enemies.add(spaghetti)

# Generate bullets for tower attack
def towerAttack(tower):
    if tower.image == CARROT and (tower.counter % tower.speed) == 0:
      newbullet = Bullet(tower.position[0], tower.position[1], tower.damage, 0.05, BULLET)
      bullets.add(newbullet)
      newbullet.draw(SCREEN)
    elif tower.image == POMEGRANATE and (tower.counter % tower.speed) == 0:
      newbullet = Bullet(tower.position[0], tower.position[1], tower.damage, 0.05, EXPLOSION)
      bullets.add(newbullet)
      newbullet.draw(SCREEN)
      tower.currhealth = 0
      tower.die()
    elif tower.image == LETTUCE and (tower.counter % tower.speed) == 0:
      newbullet = Bullet(tower.position[0], tower.position[1], tower.damage, 0.05, ICE)
      bullets.add(newbullet)
      newbullet.draw(SCREEN)
      tower.currhealth = 0
      tower.die()

# Gameplay
def gameplay():
  
  global enemies, towers, bullets
  enemies = pygame.sprite.Group()
  towers = pygame.sprite.Group()
  bullets = pygame.sprite.Group()

  global COINS, LIVES, COMMENT, WAVES, CLICKED_PACKET
  COINS = 1250 + (1000 // LEVEL)
  LIVES = 8//LEVEL
  WAVES = LEVEL * 3
  COMMENT = COMMENTS[0]
  CLICKED_PACKET = 0
  COUNTER = 0

  global seedpacket1, seedpacket2, seedpacket3, seedpacket4
  seedpacket1 = Packet(1, 0, 100, SEEDPACKET1)
  seedpacket2 = Packet(2, 0, 150, SEEDPACKET2)
  seedpacket3 = Packet(3, 0, 175, SEEDPACKET3)
  seedpacket4 = Packet(4, 0, 50, SEEDPACKET4)
  
  draw_grid()
  startWave (1,1,1,1)
  WAVES -= 1

  pygame.display.update()
  
  while LIVES >= 0:
    # Draw grid and packets
    draw_grid()
    # Draw enemies, towers, and bullets on screen
    for enemy in enemies:
      x = floor(enemy.position[0])
      y = floor(enemy.position[1])
      if x > WIDTH - 1:
        enemy.move(0)
      elif enemy.frozen == 0:
        if (GRID[y - 1][x - 1] == "NULL"):
          enemy.move(0)
        else:
          GRID[y - 1][x - 1].currhealth -= enemy.damage
      else:
        enemy.frozen -= 1
      
      enemy.draw(SCREEN)

    for tower in towers:
      towerAttack(tower)
      tower.draw(SCREEN)
    
    for bullet in bullets:
      bullet.draw(SCREEN)
      bullet.move()
        
    pygame.display.update()
    
    # Bullets hitting enemy
    # Carrot bullet release
    for enemy in enemies:
      for bullet in bullets:
        if bullet.image == BULLET:
          collision = pygame.sprite.collide_rect(bullet, enemy)
          if collision == True:
            enemy.currhealth = enemy.currhealth - bullet.damage
            bullet.kill()
            enemy.die()

    # Bombegranate bomb release
    for bullet in bullets:
      if bullet.image == EXPLOSION:
        for enemy in enemies:
          collision = pygame.sprite.collide_rect(bullet, enemy)
          if collision == True:
            enemy.currhealth = enemy.currhealth - bullet.damage
            enemy.die()
        pygame.time.delay(50)
        bullet.kill()
        
    # Iceberg Lettuce ice release
      elif bullet.image == ICE:
        for enemy in enemies:
          collision = pygame.sprite.collide_rect(bullet, enemy)
          if collision == True:
            enemy.frozen = 250
            enemy.die()
        pygame.time.delay(50)
        bullet.kill()
          
    # Enemy attacking tower
    for enemy in enemies:
      for tower in towers:
        collision = pygame.sprite.collide_rect(enemy, tower)
        if collision == True:
          #if not 
          tower.currhealth = tower.currhealth - enemy.damage
          tower.die()
            
    # Reduce lives when enemy reaches the end
    for enemy in enemies:
      if enemy.position[0] < 1:
        LIVES -= 1  
        enemy.kill() 

     # If all enemies have been killed, return 1
    if len(enemies) == 0 and LIVES > 0 and WAVES == 0:
      return 1
  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      elif event.type == WAVE_EVENT:
        if WAVES > 0:
          startWave (1,1,1,1)
          WAVES -= 1
      elif event.type == pygame.MOUSEBUTTONUP:
        if seedpacket1.rect.collidepoint(pygame.mouse.get_pos()) and seedpacket1.cost <= COINS:
          CLICKED_PACKET = 1
        elif seedpacket2.rect.collidepoint(pygame.mouse.get_pos()) and seedpacket2.cost <= COINS:
          CLICKED_PACKET = 2
        elif seedpacket3.rect.collidepoint(pygame.mouse.get_pos()) and seedpacket3.cost <= COINS:
          CLICKED_PACKET = 3
        elif seedpacket4.rect.collidepoint(pygame.mouse.get_pos()) and seedpacket4.cost <= COINS:
          CLICKED_PACKET = 4
        else:
          position = pygame.mouse.get_pos()
          x = position[0] // SIZE
          y = position[1] // SIZE
          if (CLICKED_PACKET > 0) and (x >= 1 and y >= 1 and x < WIDTH and y < HEIGHT) and GRID[y - 1][x - 1] == "NULL":
            newtower = Tower(x, y, list(TOWERS.keys())[CLICKED_PACKET])
            towers.add(newtower)
            GRID[y - 1][x - 1] = newtower
            tower_info = list(TOWERS.keys())[CLICKED_PACKET]
            COINS = COINS - TOWERS[tower_info][5]
            newtower.draw(SCREEN)
            pygame.display.update()
            CLICKED_PACKET = 0
            COMMENT = COMMENTS[0]

  # If lives are 0, return 0
  return 0

def main():
  pygame.init()
  pygame.display.set_caption('Tower Power')

  global surface
  surface = pygame.Surface(SCREEN.get_size())
  surface = surface.convert()

  global STAGE
  STAGE = STAGES[0]
  
  global LEVEL
  LEVEL = 0

  while True:
    if STAGE == "start":
      startingScreen(SCREEN)
      STAGE = STAGES[1]
    
    elif STAGE == "menu":
      LEVEL = selectionScreen(SCREEN)
      STAGE = STAGES[2]

    elif STAGE == "gameplay":
      value = gameplay()
      # If value is 0, return losing screen
      if value == 0:
        STAGE = STAGES[4]
      # Else, return winning screen
      else:
        STAGE = STAGES[3]
    
    elif STAGE == "success":
      playagain = winningScreen(SCREEN)
      if playagain == 0:
        STAGE = STAGES[0]
      else:
        terminate()

    elif STAGE == "failure":
      playagain = losingScreen(SCREEN)
      if playagain == 0:
        STAGE = STAGES[0]
      else:
        terminate()

if __name__ == "__main__":
  main()