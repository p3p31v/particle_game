import pygame
posix=0
posiy=0
change=0
changey=0
posicy=0
posicx=0
posicx1=0
posicy1=0
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
sprite3.rect = pygame.Rect(*window.get_rect().center,0,0).inflate(80,80)

sprite4 = pygame.sprite.Sprite()
sprite4.image = pygame.Surface((80,80),pygame.SRCALPHA)
pygame.draw.circle(sprite4.image, (0,0,55),(40,40),40)
sprite4.rect = pygame.Rect(*window.get_rect().center,0,0).inflate(80,80)

sprite5 = pygame.sprite.Sprite()
sprite5.image = pygame.Surface((80,80),pygame.SRCALPHA)
pygame.draw.circle(sprite5.image, (0,0,125),(40,40),40)
sprite5.rect = pygame.Rect(*window.get_rect().center,0,0).inflate(80,80)



all_group = pygame.sprite.Group([sprite2, sprite1,sprite3,sprite4,sprite5])
test_group = pygame.sprite.Group(sprite2)
def collider_circle(circle1,circle2):
    global posicx
    global posicy
    global posicx1
    global posicy1
    global posix
    global posiy
    if pygame.sprite.collide_mask(circle1,circle2):
     #posi es el vector de posicion diferencia entre la posicion de los centros de las esferas
        posicx +=(circle2.rect.x-circle1.rect.x)#ponemos + en el igual si queremos que al chocar dos veces se transmita la velocidad(no lo hago porque va todo muy rapido)
        posicy +=(circle2.rect.y-circle1.rect.y)
        posiy +=-(circle2.rect.x-circle1.rect.x)
        posix +=(circle2.rect.y-circle1.rect.y)
    circle2.rect.x+=0.006*posicx
    circle2.rect.y+=0.006*posicy
   # circle1.rect.x+=0.006*posicx1
   # circle1.rect.y+=0.006*posicy1
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
    l=0
    u=0
    k=0
    s=0
    print(sprite1.rect.center)

    if pygame.sprite.collide_mask(sprite1,sprite2):
        #posi es el vector de posicion diferencia entre la posicion de los centros de las esferas
        posix +=(sprite2.rect.x-sprite1.rect.x)
        posiy +=(sprite2.rect.y-sprite1.rect.y)
        
        if sprite1.rect.x>change:
            l=l+(sprite1.rect.x-change)

        if sprite1.rect.x<change:
            u=u+(sprite1.rect.x-change)

        if sprite1.rect.y>changey:
            k=k+(sprite1.rect.y-changey)

        if sprite1.rect.y<changey:
            s=s+(sprite1.rect.y-changey)

        sprite2.rect.x+=l+u
        sprite2.rect.y+=k+s
            #sprite2.rect.y+=sprite1.rect.y*0.01

    change = sprite1.rect.x
    changey=sprite1.rect.y
    sprite5.rect.move_ip([1,1])
    sprite4.rect.move_ip([2,2])

    sprite2.rect.x+=0.006*posix
    sprite2.rect.y+=0.006*posiy
        
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
