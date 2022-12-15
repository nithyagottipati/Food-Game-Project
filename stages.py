import sys
import pygame
from config import *

# Terminate
def terminate():
  pygame.quit()
  sys.exit()

# The starting screen
def startingScreen(SCREEN):
  pygame.font.init()
  font = pygame.font.SysFont('Comic Sans MS', 30)
  text = font.render('Welcome to Tower Power! Press any key to start.', True, (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
  
  while True:
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(text, textRect)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          terminate()
        return
      pygame.display.update()
  clock.tick(FPS)

# The menu screen
def selectionScreen(SCREEN):
  pygame.font.init()
  font = pygame.font.SysFont('Comic Sans MS', 30)
  text = font.render('Click on a level!', True, (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (SCREEN_WIDTH // 2, 50)

  text1 = font.render('Level 1', True, (0, 0, 0))
  text1Rect = text.get_rect()
  text1Rect.center = (SCREEN_WIDTH // 2, 100)

  text2 = font.render('Level 2', True, (0, 0, 0))
  text2Rect = text.get_rect()
  text2Rect.center = (SCREEN_WIDTH // 2, 150)

  text3 = font.render('Level 3', True, (0, 0, 0))
  text3Rect = text.get_rect()
  text3Rect.center = (SCREEN_WIDTH // 2, 200)

  while True:
    global LEVEL
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(text, textRect)
    SCREEN.blit(text1, text1Rect)
    SCREEN.blit(text2, text2Rect)
    SCREEN.blit(text3, text3Rect)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          terminate()
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_position = pygame.mouse.get_pos()
        if text1Rect.collidepoint(mouse_position):
          return 1
        elif text2Rect.collidepoint(mouse_position):
          return 2
        elif text3Rect.collidepoint(mouse_position):
          return 3
      pygame.display.update()
  clock.tick(FPS)

# The winning screen 
def winningScreen(SCREEN):
  pygame.font.init()
  font = pygame.font.SysFont('Comic Sans MS', 30)
  text = font.render('Congratulations! You win!', True, (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

  font1 = pygame.font.SysFont('Comic Sans MS', 20)
  text1 = font1.render('Play again', True, (0, 0, 0))
  text1Rect = text.get_rect()
  text1Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SIZE)

  text2 = font1.render('Quit', True, (0, 0, 0))
  text2Rect = text.get_rect()
  text2Rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (1.5 * SIZE))
  
  while True:
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(text, textRect)
    SCREEN.blit(text1, text1Rect)
    SCREEN.blit(text2, text2Rect)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          terminate()
        return
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_position = pygame.mouse.get_pos()
        if text1Rect.collidepoint(mouse_position):
          return 0
        elif text2Rect.collidepoint(mouse_position):
          return 1
      pygame.display.update()
  clock.tick(FPS)

# The losing screen
def losingScreen(SCREEN):
  pygame.font.init()
  font = pygame.font.SysFont('Comic Sans MS', 30)
  text = font.render('Oh no, you lost!', True, (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

  font1 = pygame.font.SysFont('Comic Sans MS', 20)
  text1 = font1.render('Play again', True, (0, 0, 0))
  text1Rect = text.get_rect()
  text1Rect.center = (SCREEN_WIDTH // 2, 220)

  text2 = font1.render('Quit', True, (0, 0, 0))
  text2Rect = text.get_rect()
  text2Rect.center = (SCREEN_WIDTH // 2, 250)
  
  while True:
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(text, textRect)
    SCREEN.blit(text1, text1Rect)
    SCREEN.blit(text2, text2Rect)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        terminate()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          terminate()
        return
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_position = pygame.mouse.get_pos()
        if text1Rect.collidepoint(mouse_position):
          return 0
        elif text2Rect.collidepoint(mouse_position):
          return 1
      pygame.display.update()
  clock.tick(FPS)