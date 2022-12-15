import pygame

# Global screen variables
WIDTH = 12
HEIGHT = 7
SIZE = 100
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE
FPS = 1

# Loading needed images upfront for efficiency
SEEDPACKET1 = pygame.transform.scale(pygame.image.load("images/Carrot_Launcher_Packet.png"), (SIZE, SIZE))
SEEDPACKET2 = pygame.transform.scale(pygame.image.load("images/Potato_Partition_Packet.png"), (SIZE, SIZE))
SEEDPACKET3 = pygame.transform.scale(pygame.image.load("images/Bomb-agranate_Packet.png"), (SIZE, SIZE))
SEEDPACKET4 = pygame.transform.scale(pygame.image.load("images/Iceberg_Lettuce_Packet.png"), (SIZE, SIZE))

CARROT = pygame.transform.scale(pygame.image.load("images/Carrot_Launcher.png"), (SIZE, SIZE))
POTATO = pygame.transform.scale(pygame.image.load("images/Potato_Partition.png"), (SIZE, SIZE))
POMEGRANATE = pygame.transform.scale(pygame.image.load("images/Bomb-agranate.png"), (SIZE, SIZE))
LETTUCE = pygame.transform.scale(pygame.image.load("images/Iceberg_Lettuce.png"), (SIZE, SIZE))

BULLET = pygame.transform.scale(pygame.image.load("images/Bullet.png"), (SIZE, SIZE))
ICE = pygame.transform.scale(pygame.image.load("images/Ice.png"), (SIZE * 3, SIZE * 3))
EXPLOSION = pygame.transform.scale(pygame.image.load("images/Explosion.png"), (SIZE * 3, SIZE * 3))

FRIES = pygame.transform.scale(pygame.image.load("images/Fries.png"), (SIZE, SIZE))
BURGER = pygame.transform.scale(pygame.image.load("images/Burger.png"), (SIZE, SIZE))
DONUT = pygame.transform.scale(pygame.image.load("images/Donut.png"), (SIZE, SIZE))
SPAGHETTI = pygame.transform.scale(pygame.image.load("images/Spaghetti.png"), (SIZE, SIZE))

# Game settings
SCORE = 0
LEVEL = 0

# Used later to check for the stage of gameplay
STAGES = ["start", "menu", "gameplay", "success", "failure"]
STAGE = STAGES[0]
COMMENTS = ["Click on a plant packet to plant!", "Click on a lawn square to plant!", "Not enough coins--defeat more enemies."]

# Enemy types list, tower types dictionary with name to stats [health, speed, damage, image, description, cost]
ENEMIES = ["Donut", "Burger", "Fries", "Spaghetti"]
TOWERS = {"None Selected":[],
"Carrot Launcher":[300, 50, 10, CARROT, "Shoots carrot projectiles.", 100],
"Potato Partition":[2000, 100, 0, POTATO, "Blocks enemies with high health.", 150],
"Bomb-agranate":[1000, 15, 75, POMEGRANATE, "Explodes with massive damage!", 175], 
"Iceberg Lettuce":[400, 100, 0, LETTUCE, "Freezes after a short delay.", 50]}

GRID = []
for row in range(HEIGHT - 2):
  row = []
  for column in range(WIDTH - 1):
    row.append("NULL")
  GRID.append(row)

# Create timer and event for waves
pygame.init()
WAVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(WAVE_EVENT, 10000)
