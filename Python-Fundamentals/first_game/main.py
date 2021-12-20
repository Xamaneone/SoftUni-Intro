import pygame
import math
import random
from pygame import mixer

# Initialize the pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.jpg")

# Background Sound
mixer.music.load("soundtrack.wav")
mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Potato Smasher")
icon = pygame.image.load("potato.png")
pygame.display.set_icon(icon)




# Player
playerImg = pygame.image.load("ship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


# Score

score_value = 0
font = pygame.font.Font("snowy_schristmas.otf", 102)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font("snowy_schristmas.otf", 64)


for i in range(int(num_of_enemies)):
    enemyImg.append(pygame.image.load("illuminati.png"))
    enemyX.append(random.randint(100, 700))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("potato.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if int(distance) < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((255, 194, 132))
    # Background Image
    screen.blit(background, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it s right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound("kill_sound.wav")
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

    # player movement
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerX += playerX_change


    # enemy movement
    for i in range(int(num_of_enemies)):

        # Game Over
        if enemyY[i] > 440:
            for j in range(int(num_of_enemies)):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_Sound = mixer.Sound("kill_sound.wav")
            bullet_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # num_of_enemies += 0.50
            enemyX[i] = random.randint(100, 700)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()