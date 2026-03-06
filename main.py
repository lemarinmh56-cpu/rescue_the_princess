import pygame 
from utils import*
bg_image = pygame.transform.scale(pygame.image.load('castle.jpg'), (800, 600))
# Configuración de ventana
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Castello')


knight = Player('knigth.png', 0 ,0)
walls = [
Wall(0,200,500,5),
Wall(500,300,300,5 ),
Wall(0,400,200,5),
Wall(0,500,800,100,(0,0,0))

]
run = True
# Reloj para controlar FPS
clock = pygame.time.Clock()
while run:
    window.blit(bg_image, (0,0))
    clock.tick(40)
    knight.draw(window)
    knight.update(walls)
    for wall in walls:
        wall.draw(window)

    # Procesar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                knight.jump()
    pygame.display.update()