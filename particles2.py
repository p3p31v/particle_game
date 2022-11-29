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
obstacle = pygame.Rect(400,300,80,80)
carImg = pygame.image.load('circle.png')
rect = carImg.get_rect()
rect1 = carImg.get_rect(center=(100,100))
class Ball(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.image = pygame.image.load(os.path.join('resources', 'circle.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass

print(type(Ball))
#Cm=pygame.sprite.collide_mask(rect,rect1)
def circle(cx,cy,radio):
    circle = pygame.draw.circle(gameDisplay,0xFFFF0000,(cx,cy),radio)

def car(x,y):
    gameDisplay.blit(carImg,rect)
#hay que meter rect1 para que aparezca la segunda bola.Tambien hay que definir
#x1 e y1 dentro del bucle del juego, aunque todo empieza en 0,0 igualmente
#porque la funcion get_rect va con el 0,0
def particle(x1,y1):
    gameDisplay.blit(carImg,rect1)


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
    x=400
    y=200
    x1=200
    y1=200
    x_change = 0
    y_change = 0
    x1_change=2
    y1_change = 1
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
       # rect1.y+=y1_change #no es y1
       # rect1.x+=x1_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, (0,0,0),obstacle,4)
        car(x,y)
        circle(200,200,25)
        circle(200,100,25)
        particle(x1,y1)
        Cm=pygame.sprite.collide_mask(car(x,y),circle(200,200,25))
 #       if Cm !=None:
  #          print('life -1')
        if x > display_width - car_width or x < 0:
            crash()
#        print(rect.x,rect.y)
       # if rect.x<480 and rect.x>350 and rect.y<380 and rect.y>250:
           # for i in range(1,40):

               # x_change = -x_change
               # y_change = -y_change
           # rect.x += x_change
           # rect.y += y_change
            
        if rect.colliderect(obstacle):
            pygame.draw.rect(gameDisplay,(255,0,0),rect,4)
            #for i in range(1,40):

            x_change = -x_change
            y_change = -y_change
            rect.x +=x_change
            rect.y +=y_change
        if rect.colliderect(rect1):
            pygame.draw.rect(gameDisplay,(255,0,0),rect,4)
          #  for i in range(1,40):

            x_change=-x_change
            y_change=-y_change
            rect.x +=x_change
            rect.y +=y_change
            rect1.x +=-x_change+x1_change
            rect1.y +=-y_change+y1_change

        pygame.display.update()
        clock.tick(60)
#https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
game_loop()
pygame.quit()
quit()

