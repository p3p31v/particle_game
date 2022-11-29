import pygame
change=0
t=0
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

all_group = pygame.sprite.Group([sprite2, sprite1])
test_group = pygame.sprite.Group(sprite2)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sprite1.rect.center = pygame.mouse.get_pos()

    if sprite1.rect.x>change:
        t=t+1
    if sprite1.rect.x<change
        u=u+1
 #aqui me quedo ma;ana sigo   if sprite1.rect.y>

    collide = pygame.sprite.spritecollide(sprite1, test_group, False, pygame.sprite.collide_circle)

    window.fill(0)
    change = sprite1.rect.x
    print(t)
    print(sprite1.rect.center)
    if pygame.sprite.collide_mask(sprite1,sprite2):
        if sprite1.rect.x>0 and sprite1.rect.y>0:

            sprite2.rect.x+=sprite1.rect.x*0.01
            sprite2.rect.y+=sprite1.rect.y*0.01


    all_group.draw(window)
    for s in collide:
        pygame.draw.circle(window, (255, 255, 255), s.rect.center, s.rect.width // 2, 5)
       # sprite2.rect.x+=1
    pygame.display.flip()

pygame.quit()
exit()
