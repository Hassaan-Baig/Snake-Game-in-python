import random
import pygame
import math
from pygame import mixer
import time

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('snake.png')

clock = pygame.time.Clock()


def bg():
    screen.blit(background, (170, 40))


# Caption and Icon
pygame.display.set_caption("SNAKE GAME")

# SNAKE
snakeImg = pygame.image.load('robot.png')
headX = 370
headY = 480
headVel = 6


def snakeHead():
    screen.blit(snakeImg, (headX, headY))


# SNAKE BODY
bodyImg = []
bodyX = []
bodyY = []
bodyParts = 0

# SNAKE MOVEMENT
left = False
right = True
up = False
down = False

# FOOD
foodX = random.randint(20, 700)
foodY = random.randint(20, 500)
foodImg = pygame.image.load('pizza.png')


def food():
    screen.blit(foodImg, (foodX, foodY))


def addBody():
    global bodyParts
    bodyImg.append(pygame.image.load('rounded-rectangle.png'))
    bodyX.append(headX)
    bodyY.append(headY)
    bodyParts += 1


def snakeBody(partsNo):
    for j in range(partsNo):
        screen.blit(bodyImg[j], (bodyX[j], bodyY[j]))


game = pygame.font.Font("Generating Script Font.ttf", 64)


def GameOver():
    gameOver = game.render("GAME OVER !", True, (0, 0, 255))
    screen.blit(gameOver, (260, 250))


scoreVal = 0
font = pygame.font.Font("Generating Script Font.ttf", 32)
textY = 15
textX = 670


def showScore():
    score = font.render("SCORE: " + str(scoreVal), True, (255, 0, 5))
    screen.blit(score, (textX, textY))


for i in range(5):
    addBody()

end = False
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame.KEYDOWN:
            if not end:
                if event.key == pygame.K_LEFT:
                    if not right and not left:
                        left = True
                        right = up = down = False
                if event.key == pygame.K_RIGHT:
                    if not right and not left:
                        right = True
                        left = up = down = False
                if event.key == pygame.K_DOWN:
                    if not up and not down:
                        down = True
                        right = left = up = False
                if event.key == pygame.K_UP:
                    if not up and not down:
                        up = True
                        right = left = down = False
    # screen color
    screen.fill((255, 255, 255))
    bg()
    if not end:
        snakeBody(bodyParts)
    # Food Eating
    if 32 >= math.sqrt((headX - foodX) ** 2 + (headY - foodY) ** 2):
        scoreVal += 10
        addBody()
        foodX = random.randint(20, 700)
        foodY = random.randint(20, 500)

    # SNAKE BODY MOVEMENT
    x = headX
    y = headY
    if right:
        headX += headVel
    elif left:
        headX -= headVel
    elif up:
        headY -= headVel
    elif down:
        headY += headVel

    for i in range(bodyParts):
        if i == 0:
            a = bodyX[0]
            b = bodyY[0]
            bodyX[i] = x
            bodyY[i] = y
        else:
            t1 = bodyX[i]
            t2 = bodyY[i]
            bodyX[i] = a
            bodyY[i] = b
            a = t1
            b = t2
    if headX >= 755 or headX <= 15 or headY >= 555 or headY < 15:
        GameOver()
        textX = 330
        textY = 320
        end = True
    if not end:
        food()
        snakeHead()
    showScore()
    # SELF COLLISION
    for i in range(bodyParts):
        if headX == bodyX[i] and headY == bodyY[i]:
            GameOver()
            textX = 330
            textY = 320
            end = True
    clock.tick(60)
    # left boundary
    pygame.draw.line(screen, (0, 0, 0), (10, 0), (10, 595), 10)  # black
    pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, 600), 10)  # yellow
    # right boundary
    pygame.draw.line(screen, (0, 0, 0), (785, 0), (785, 600), 10)  # black
    pygame.draw.line(screen, (255, 0, 0), (795, 0), (795, 600), 10)  # yellow
    # upper boundary
    pygame.draw.line(screen, (0, 0, 0), (10, 585), (785, 585), 10)  # black
    pygame.draw.line(screen, (255, 255, 0), (0, 595), (800, 595), 10)  # yellow
    # lower boundary
    pygame.draw.line(screen, (0, 0, 0), (10, 10), (785, 10), 10)  # black
    pygame.draw.line(screen, (255, 255, 0), (0, 0), (800, 0), 10)  # yellow
    pygame.display.update()
