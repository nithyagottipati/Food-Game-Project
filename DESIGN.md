Inspired by Plants vs Zombies, our project is a defense tower game in which the user must place various vegetable and fruit-themed towers on the game board in order to protect their territory from oncoming “enemy” foods. Our program utilizes PyGame, a cross-platform set of video game-related Python modules that allowed us to replicate the general functionality of a typical video game. 

config.py:

config.py contains all the global variables we need in the game. In addition, each of our game characters was hand-drawn and thereby loaded into the program as png files -- we decided to perform this step upfront in the file config.py in order to prioritize efficiency in the run-time of the game. We also set up a timer with an interval of 600 milliseconds to create a "shoot_event", which allows bullets to be spawned at intervals.

classes.py:

We then created unique classes in classes.py for each “category” of sprites loaded into the game, namely for packets, enemies, bullets and towers. We attributed various important characteristics such as speed and position accordingly. We also defined functions for each, such as draw() to draw the sprite on the screen, or move() to program the movement of the enemies/bullets. 

We decided to use classes because we could assign attributes, create functions for each type of sprite in the game, and this would also make it easier to have sprites interact with each other (e.g. enemies and towers) 

stages.py:

stages.py holds various screens or messages that we broadcast to our users during various aspects of our game’s timeline, including the opening welcome screen, the level selection screen and the win/loss screens. When the game opens, one will notice that coins and lives are assigned to the user at the bottom of the game board, while each tower and enemy sprite displays a health bar. In order to account for the effects of collisions of sprites, we decided to group our sprites through PyGame's functionalities in the main file. 

main.py:

In main.py, we have several important functions for gameplay:

draw_grid() is used to draw the black borders, as well as the playing grid. It also renders the number of coins and lives left

terminate() ends the game

startWave() is used to generate waves of enemies, by adding enemies (which are spawned in random locations) to an enemies sprite group which will be drawn in gameplay()

gameplay() is where the actual gameplay happens – we define three global sprite groups, enemies, towers and bullets, and these will be iterated through and printed onscreen. We draw the grid, the packets, enemies and towers onscreen. 

We also detect for collisions between sprites. If an enemy collides with a tower, we reduce the tower's health. We also check the call the tower.die() function whether the health of the tower reaches 0, in which case we kill the tower. If a bullet collides with an enemy, we reduce the enemy's health. We also call bullet.kill() to delete the bullet, and we call enemy.die() to check if the enemy's health is 0, in which case we kill the enemy.

In addition, we also check whether the enemy has reached the left border, in which case we reduce the lives by 1. Note that if the lives reach 0, we exit the while loop and return 0 to exit the function with a loss state, which calls the losingScreen() function in main(). 

On the other hand, if the size of the enemies sprite group is empty and lives are still more than 0 (i.e. all enemies have died), this means the user has won, so we return 1 to exit the function with a win state, which calls the winningScreen() function in main().

We also check for various events in this function. If the carrot_shoot_event (determined by the event timer) is detected, we generate a bullet sprite at the position of every carrot and add it to the bullets sprite group. This allows the bullets to be drawn, hence generating bullets in a loop. 

We also detect mouse clicks, to check if the user is planting a packet. If the mouse position collides with a seed packet, we change CLICKED_PACKET to the number of the packet (to indicate which packet the user has chosen). We also detect clicks on the grid itself, so if CLICKED_PACKET has a value and the user clicks anywhere in the grid, a plant will be 'planted'.

main()

This function allows the player to move between stages.







