import pygame 
import random
from pygame.locals import * 
import sys
from ship import Ship 
from asteroid import Asteroid

pygame.init()

# screen display
screen_info = pygame.display.Info()
# set width and height of the screen
screen_size = (width, height) = int(screen_info.current_w), int(screen_info.current_h)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
color = (0, 127, 255)

# create player
player = Ship ((20,200))

# setup game variables
NumLevels = 4
Level = 1

asteroids = pygame.sprite.Group()
asteroid_count = 3

def init():
  global asteroids, asteroid_count
  player.reset((20, 200))
  asteroids.empty()
  asteroid_count += 3
  for i in range(asteroid_count):
    asteroids.add(
      Asteroid(
        # pos (x,y)
        (
          random.randint(50, width-50),
          random.randint(50, height-50)
        ),
        #scale 
        random.choice([0.1,0.09,0.08])
      )
    )

def main():
  global Level, NumLevels

  init()

  while Level < NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          player.speed[0] = -10
        if event.key == pygame.K_UP:
          player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          player.speed[1] = 10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 0
        if event.key == pygame.K_LEFT:
          player.speed[0] = 0
        if event.type == pygame.K_UP:
          player.speed[1] = 0
        if event.key == pygame.K_DOWN:
          player.speed[1] = 0

    # draw sprites and add colors to screen, UI
    player.update()
    asteroids.update()
    screen.fill(color)
    asteroids.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()