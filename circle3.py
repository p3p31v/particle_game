import pygame
posix=0
posiy=0
posicy=0
posicx=0
pygame.init()
window = pygame.display.set_mode((1000, 1000))

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((80, 80), pygame.SRCALPHA)
pygame.draw.circle(sprite1.image, (255, 0, 0), (40, 40), 40)
sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(40, 40)
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((80, 89), pygame.SRCALPHA)
pygame.draw.circle(sprite2.image, (0, 255, 0), (40, 40), 40)
sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(80, 80)
sprite3 = pygame.sprite.Sprite()
sprite3.image = pygame.Surface((80,80),pygame.SRCALPHA)
pygame.draw.circle(sprite3.image, (0,0,255),(40,40),40)
sprite3.rect = pygame.Rect(*window.get_rect().center,0,100).inflate(80,80)

all_group = pygame.sprite.Group([sprite2, sprite1,sprite3])
test_group = pygame.sprite.Group(sprite2)
def collider_circle(circle1,circle2):
    global posicx
    global posicy

    if pygame.sprite.collide_mask(circle1,circle2):
     #posi es el vector de posicion diferencia entre la posicion de los centros de las esferas
        posicx =circle2.rect.x-circle1.rect.x#ponemos + en el igual si queremos que al chocar dos veces se transmita la velocidad(no lo hago porque va todo muy rapido)
        posicy =circle2.rect.y-circle1.rect.y

    circle2.rect.x+=0.06*posicx
    circle2.rect.y+=0.06*posicy
    #circle1.rect.x-=0.06*posicx
    #circle1.rect.y-=0.06*posicy
    if circle2.rect.right>=1000 or circle2.rect.left<=0:
        posicx *=-1
    if circle2.rect.bottom>= 1000 or circle2.rect.top<=0:
        posicy *=-1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sprite1.rect.center = pygame.mouse.get_pos()

    collide = pygame.sprite.spritecollide(sprite1, test_group, False, pygame.sprite.collide_circle)

    window.fill(0)
    print(sprite1.rect.center)

    if pygame.sprite.collide_mask(sprite1,sprite2):
        #posi es el vector de posicion diferencia entre la posicion de los centros de las esferas
        posix =sprite2.rect.x-sprite1.rect.x
        posiy =sprite2.rect.y-sprite1.rect.y


    sprite2.rect.x+=0.06*posix
    sprite2.rect.y+=0.06*posiy
        
    if sprite2.rect.right>=1000 or sprite2.rect.left<=0:
        posix *=-1
    if sprite2.rect.bottom>= 1000 or sprite2.rect.top<=0:
        posiy *=-1
 


    collider_circle(sprite2,sprite3)
    all_group.draw(window)

    for s in collide:
        pygame.draw.circle(window, (255, 255, 255), s.rect.center, s.rect.width // 2, 5)
       
    pygame.display.flip()

pygame.quit()
exit()
