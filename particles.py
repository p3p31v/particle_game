import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Particles in da house')
clock = pygame.time.Clock()
obstacle = pygame.Rect(400,200,80,80)

carImg = pygame.image.load('circle.png')
rect = carImg.get_rect()
def car(x,y):
    gameDisplay.blit(carImg,rect)



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
   # x1 = 0.2*x
   # y1 = 0.2*y
    x_change = 0
    y_change = 0
    y1_change = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            y_change = 1
           # y1_change = y1_change + 0.3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        rect.x += x_change
        rect.y += y_change
       # rect.y1 += y1_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, (0,0,0),obstacle,4)
        car(x,y)
       # car(x1,y1)
        if x > display_width - car_width or x < 0:
            crash()
        if rect.colliderect(obstacle):
            pygame.draw.rect(gameDisplay,(255,0,0),rect,4)
            x = 0
             
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
