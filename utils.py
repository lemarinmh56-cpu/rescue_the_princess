import pygame
class Character(pygame.sprite.Sprite):

    def __init__(self, c_image, x, y, speed=5, width = 80, height = 80):
        """Constructor de la clase Character."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(c_image), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_y = 0
        self.touch = False

    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, element):
        return self.rect.colliderect(element.rect)
class Player(Character):
    def gravity(self):
        self.speed_y+=0.4
    def jump(self):
        if self.touch == True:
            self.speed_y =-10
            self.touch= False
    def update(self,walls):
        """Movimiento del jugador."""
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 800 - 80:
            self.rect.x += self.speed
        walls_touched = pygame.sprite.spritecollide(self, walls, False) 
        if keys[pygame.K_RIGHT]:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left) 
        if keys[pygame.K_LEFT]:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)
        
        self.gravity() 
        self.rect.y += self.speed_y

        walls_touched = pygame.sprite.spritecollide(self, walls, False)

        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom= wall.rect.top
                self.speed_y = 0
                self.touch =True
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top= wall.rect.bottom
                self.speed_y = 0
 
                
        
    
        
                
class Wall(pygame.sprite.Sprite):

    def __init__(self, wallx, wally,wall_width, wall_height,color_wall = (252,252,252)):
        self.color = color_wall
        self.wallx = wallx
        self.wally = wally
        self.wall_width = wall_width
        self.wall_height = wall_height
        super().__init__() 

        self.image = pygame.Surface([self.wall_width, self.wall_height])
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally
        self.image.fill(color_wall)
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.rect.x,self.rect.y,self.wall_width,self.wall_height)) 
class Enemy(Character):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 750 or  self.rect.x <=0 :
            self.speed *= -1