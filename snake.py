import pygame
import random

pygame.init()

screen = pygame.display.set_mode((810, 600))

#icon
icon = pygame.image.load('graphics/snake.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake')

#draw head
color = (0, 0, 0)
headX = 390
headY = 270
headX_change = 0.1
headY_change = 0
headRotation = 'right'

#create head rectangle
headRect = pygame.Rect(headX, headY, 30, 30)

def drawhead(headRect):
    pygame.draw.rect(screen, color, headRect)

#draw tail
tail_count = 0
tailX = []
tailY = []
tailX.append(headX)
tailY.append(headY)
def drawtail(x, y):
    tailRect = pygame.Rect(x, y, 30, 30)
    pygame.draw.rect(screen, color, tailRect)


#draw apple

appleX = random.randint(1, 25)*30 
appleY = random.randint(1, 18)*30 

#create apple rectangle
appleRect = pygame.Rect(appleX, appleY, 30, 30)

def drawapple(appleRect):
    pygame.draw.rect(screen, color, appleRect)

#clock
clock = pygame.time.Clock()

#game-over
font = pygame.font.Font('freesansbold.ttf', 64)
textX = 220
textY = 250

def gameover(x, y):
    gameover = font.render('GAME OVER', True, (0, 0, 0))
    screen.blit(gameover, (x, y))

game_state = 'play'

running = True

while running:
    screen.fill((255, 255, 255))
    clock.tick(10)
    tailX[0] = headX
    tailY[0] = headY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state is 'play':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and headRotation != 'right':
                    headRotation = 'left'
                    headY_change = 0
                    headX_change = -30
                if event.key == pygame.K_d and headRotation != 'left':
                    headRotation = 'right'
                    headY_change = 0
                    headX_change = 30
                if event.key == pygame.K_w and headRotation != 'down':
                    headRotation = 'up'
                    headY_change = -30
                    headX_change = 0
                if event.key == pygame.K_s and headRotation != 'up':
                    headRotation = 'down'
                    headY_change = 30
                    headX_change = 0
    if headRect.colliderect(appleRect):
        appleX = random.randint(0, 25)*30
        appleY = random.randint(0, 19)*30
        tailX.append(tailX[tail_count])
        tailY.append(tailY[tail_count])
        tail_count += 1

    
    #draw tail
    for i in range(tail_count):
        tailX[tail_count-i] = tailX[tail_count-i-1]
        tailY[tail_count-i] = tailY[tail_count-i-1]
        tailRect = pygame.Rect(tailX[tail_count-i], tailY[tail_count-i], 30, 30)
        drawhead(tailRect)    

    headX += headX_change
    headY += headY_change
    if headX > 800 or headX < 0 or headY > 600 or headY < 0:
        gameover(textX, textY)
        headX_change = 0
        headY_change = 0
        game_state = 'gameover'

    #draw current head position
    headRect = pygame.Rect(headX, headY, 30, 30)
    drawhead(headRect)

    #draw current apple position
    appleRect = pygame.Rect(appleX, appleY, 30, 30)
    drawapple(appleRect)

    pygame.display.update()