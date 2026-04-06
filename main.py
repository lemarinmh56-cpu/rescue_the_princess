import pygame 
from utils import*
bg_image = pygame.transform.scale(pygame.image.load('castle.jpg'), (800, 600))
# Configuración de ventana
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Castello')
shift = 0
right_wall= 550
all_sprites = pygame.sprite.Group()
goblin = Enemy('2.png',50,120)
goblins = [Enemy('2.png',50,120)]
all_sprites.add(goblin)

knight = Player('knigth1.png', 0 ,490)
walls = [
Wall(0,200,500,5),
Wall(500,100,300,5 ),
Wall(0,400,400,5),
Wall(500,300,400,5),
Wall(0,500,1000,100,(0,0,0)),
Wall(795,100,5,400),
Wall(1200, 500, 5, 400),
Wall(1400,400,5,400),
Wall(1450,300,5,400),
Wall(1500,250,150,5),
Wall(1450,150,100,5)
]
all_sprites.add(knight)
for wall in walls:
    all_sprites.add(wall)
run = True
# Reloj para controlar FPS
clock = pygame.time.Clock()
while run:
    window.blit(bg_image, (shift,0))
    clock.tick(40)

    for wall in walls:
        wall.draw(window)
    if knight.rect.x > right_wall:
        shift -= knight.speed
        for s in all_sprites:
            s.rect.x-= knight.speed
        
    local_shift = shift % 800
        
    window.blit(bg_image, (local_shift, 0))
        
    if local_shift != 0:
        window.blit(bg_image, (local_shift - 800, 0))
            
    window.blit(bg_image, (shift,0))
    all_sprites.draw(window)
    knight.draw(window)
    knight.update(walls)



        

    # Procesar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                knight.jump()
    pygame.display.update()