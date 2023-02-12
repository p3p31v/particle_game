import pygame
import math
import random
posix=0
posiy=0
change=0
changey=0
posicy=0
posicx=0
posicx1=0
posicy1=0
posix45=0
posiy45=0
posix45_0=0
posiy45_0=0
k1=0
k2=0
k3=0
k4=0
v1x=10#random.randint(-10,10)#10
v1y=0
v2x=-22#random.randint(-10,10)#-22
v2y=0
vfinsprite4x=v1x
vfinsprite4y=v1y
vfinsprite5x=v2x
vfinsprite5y=v2y

alpha=0#(v1x*v2x+v1y*v2y)/(math.sqrt((v1x^2)+(v1y^2))*math.sqrt((v2x^2)+(v2y^2)))
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
pygame.draw.circle(sprite4.image, (255,0,255),(40,40),40)
sprite4.rect = pygame.Rect(*window.get_rect().center,0,0).inflate(80,80)

sprite5 = pygame.sprite.Sprite()
sprite5.image = pygame.Surface((80,80),pygame.SRCALPHA)
pygame.draw.circle(sprite5.image, (255,255,0),(40,40),40)
sprite5.rect = pygame.Rect(*window.get_rect().center,0,0).inflate(80,80)

sprite4.rect.x=100#sprite4.rect.x=100
sprite4.rect.y=800#sprite4.rect.y=400


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
    posix45_0 =sprite5.rect.x-sprite4.rect.x
    posiy45_0 =sprite5.rect.y-sprite4.rect.y

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
        # Here we will use REALISTIC physics
            #sprite2.rect.y+=sprite1.rect.y*0.01
    if pygame.sprite.collide_mask(sprite4,sprite5):
        posix45 =sprite5.rect.x-sprite4.rect.x
        posiy45 =sprite5.rect.y-sprite4.rect.y
        if posix45>0 and posiy45>0:
            if math.sqrt(v1x**2+v1y**2)<math.sqrt(v2x**2+v2y**2):#hecho
                k1=1
                k2=1
                k3=1
                k4=-1
            elif math.sqrt(v1x**2+v1y**2)>math.sqrt(v2x**2+v2y**2):#hecho
                k1=1
                k2=-1
                k3=1
                k4=1
        elif posix45>0 and posiy45<0:
            if math.sqrt(v1x**2+v1y**2)<math.sqrt(v2x**2+v2y**2):#hechop
                k1=1
                k2=-1
                k3=1
                k4=1
            elif math.sqrt(v1x**2+v1y**2)>math.sqrt(v2x**2+v2y**2):#hechop
                k1=1
                k2=1
                k3=1
                k4=-1
#no se por que cambia el signo de la velocidad, tengo que mirarlo, voy a hacer lo de abajo suponiendo que no cambian e iremos corrigiendo. En un principio me lo invento lol

        elif posix45<0 and posiy45<0:
            if math.sqrt(v1x**2+v1y**2)<math.sqrt(v2x**2+v2y**2):#hecho
                k1=-1
                k2=-1
                k3=-1
                k4=1
            elif math.sqrt(v1x**2+v1y**2)>math.sqrt(v2x**2+v2y**2):#hecho
                k1=1
                k2=-1
                k3=1
                k4=1
        elif posix45<0 and posiy45>0:
            if math.sqrt(v1x**2+v1y**2)<math.sqrt(v2x**2+v2y**2):#hecho
                k1=1
                k2=-1
                k3=1
                k4=1
            elif math.sqrt(v1x**2+v1y**2)>math.sqrt(v2x**2+v2y**2):#hecho
                k1=1
                k2=1
                k3=1
                k4=-1
        print('vector de posicion')
        print(posix45,posiy45)
        alpha45=(v1x*posix45+v1y*posiy45)/(math.sqrt((v1x**2)+(v1y**2))*math.sqrt((posix45**2)+(posiy45**2)))
        alpha45=math.acos(alpha45)
        print('alpha')
        print(alpha45)
        vfinsprite4=(v1x+v2x)*math.sin(alpha45)+(v1y+v2y)*math.cos(alpha45)
        vfinsprite5=(v1x+v2x)*math.cos(alpha45)-(v1y+v2y)*math.sin(alpha45)
        vfinsprite4=vfinsprite4
        vfinsprite5=vfinsprite5
        print(vfinsprite4,vfinsprite5)
        vfinsprite4x=k1*vfinsprite4*math.cos((math.pi/2)-alpha45)
        vfinsprite4y=k2*vfinsprite4*math.sin((math.pi/2)-alpha45)
        vfinsprite5x=k3*vfinsprite5*math.cos(alpha45)# la amarilla
        vfinsprite5y=k4*vfinsprite5*math.sin(alpha45)
        sprite4.rect.x=sprite4.rect.x-k1*v1x
        sprite4.rect.y=sprite4.rect.y-k2*v1y
        sprite5.rect.x=sprite5.rect.x - k3*v2x
        sprite5.rect.y=sprite5.rect.y-k4*v2y
        print("rosa y despues amarilla")
        print(vfinsprite4x,vfinsprite4y,vfinsprite5x,vfinsprite5y)
    #    sprite5.rect.y+=10
    
   
    v1x=vfinsprite4x + 0.1*posix45_0/((0.01*posix45_0)**2+(0.01*posiy45_0)**2)
    v1y=vfinsprite4y + 0.1*posiy45_0/((0.01*posix45_0)**2+(0.01*posiy45_0)**2)
    v2x=vfinsprite5x - 0.1*posix45_0/((0.01*posix45_0)**2+(0.01*posiy45_0)**2)
    v2y=vfinsprite5y - 0.1*posiy45_0/((0.01*posix45_0)**2+(0.01*posiy45_0)**2)
    pu=0.001*posiy45_0/((0.01*posix45_0)**2+(0.01*posiy45_0)**2)
    print("v1x,posix45_0,v1y,posiy45_0,v2x,-posix45_0,v2y,-posiy45_0,pu")
    print(v1x,posix45_0,v1y,posiy45_0,v2x,-posix45_0,v2y,-posiy45_0,pu)
    sprite4.rect.x+=v1x
    sprite4.rect.y+=v1y
    sprite5.rect.x+=v2x
    sprite5.rect.y+=v2y
    #sprite4.rect.move_ip([round(vfinsprite4x),round(vfinsprite4y)])
    #sprite5.rect.move_ip([round(vfinsprite5x),round(vfinsprite5y)])
    change = sprite1.rect.x
    changey=sprite1.rect.y
    
    #alpha=(v1x*v2x+v1y*v2y)/(math.sqrt((v1x**2)+(v1y**2))*math.sqrt((v2x**2)+(v2y**2)))
   # alpha=math.acos(alpha)
    
    
    print(alpha)
    #sprite5.rect.move_ip([v2x,v2y])
    #sprite4.rect.move_ip([v1x,v1y])

    sprite2.rect.x+=0.006*posix
    sprite2.rect.y+=0.006*posiy
        
    if sprite2.rect.right>=1000 or sprite2.rect.left<=0:
        posix *=-1
    if sprite2.rect.bottom>= 1000 or sprite2.rect.top<=0:
        posiy *=-1
    if sprite4.rect.right>=1000 or sprite4.rect.left<=0:
        vfinsprite4x *=-1
    if sprite4.rect.bottom>= 1000 or sprite4.rect.top<=0:
        vfinsprite4y *=-1
    if sprite5.rect.right>=1000 or sprite5.rect.left<=0:
        vfinsprite5x *=-1
    if sprite5.rect.bottom>=1000 or sprite5.rect.top<=0:
        vfinsprite5y *=-1


    collider_circle(sprite2,sprite3)
    all_group.draw(window)

    for s in collide:
        pygame.draw.circle(window, (255, 255, 255), s.rect.center, s.rect.width // 2, 5)
    clockobject = pygame.time.Clock()
    clockobject.tick(80)
    pygame.display.flip()

pygame.quit()
exit()
