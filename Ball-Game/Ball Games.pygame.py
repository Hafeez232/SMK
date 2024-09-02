import pygame
pygame.init()
size = width,height = 500, 500
color = (0, 0, 0)
vel = (2, 2)
title = "Hafeez"
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

#Have to download ball image
ball = pygame.image.load("ball.png pathfile")
ballRect = ball.get_rect()
run = True
while run:
    #Reset the pos
    pos = 0,0
    pygame.time.delay(100)
    print(pygame.event.get_rect())
    #Handle Arrow Key Event
    keys = pygame.key.get.pressed()
    if keys[pygame.K_LEFT]:
        pos = -10, 0
    if keys[pygame.K_RIGHT]:
        pos = 10, 0
    if keys[pygame.K_UP]:
        pos = 0, -10
    if keys[pygame.K_DOWN]:
        pos = 0, 10
    #Break the loop when ESCAPE is pressed
    if keys[pygame.K_ESCAPE]:
          run = False
    #Move the rectangle
    ballRect = ballRect.move(pos)
    window.fill(color)
    window.blit(ball,ballRect)
    pygame.display.flip()
pygame.quit()
