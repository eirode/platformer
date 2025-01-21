import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, x_acc, friction, *groups):
        super().__init__(*groups)
        self.surf = pygame.surface.Surface((30, 30))
        self.surf.fill((182, 208, 226))
        self.rect = self.surf.get_rect(center=(10, 420))

        self.vector = pygame.math.Vector2
        self.pos = self.vector(10, 385)
        self.speed = self.vector(0, 0)
        self.acceleration = self.vector(0, 0)

        self.screen_width = screen_width
        self.x_acc = x_acc
        self.friction = friction

    
    def move(self):
        self.acceleration = self.vector(0, 0.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_q]:
            self.acceleration.x -= self.x_acc
        if pressed_keys[pygame.K_d]:
            self.acceleration.x += self.x_acc
        self.acceleration.x += self.speed.x * self.friction
        self.speed += self.acceleration
        self.pos += self.speed + self.acceleration / 2
        self.pos.x = self.pos.x % self.screen_width
        

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.speed.y = 0
        self.rect.midbottom = self.pos
