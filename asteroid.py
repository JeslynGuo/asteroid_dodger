import pygame, random 

class Asteroid(pygame.sprite.Sprite):
  def __init__(self, pos, scale):
    super().__init__()
    self.image = pygame.image.load("asteroid.png")
    self.scale = scale
    width = int(self.image.get_rect().width*self.scale)
    height = int(self.image.get_rect().height*self.scale)
    self.image = pygame.transform.smoothscale(
      self.image, (width, height)
    )
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,3)
    self.speed.rotate_ip(random.randint(0,360))

  
  def update(self):
    self.rect.move_ip(self.speed)
    screen_info = pygame.display.Info()
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] *= -1
      self.rect.move_ip((self.speed[0],0))
      self.image = pygame.transform.flip(self.image, True, False)
    if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
      self.speed[0] *= -1
      self.rect.move_ip((0, self.speed[1]))
      self.image = pygame.transform.flip(self.image, True, False)