import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("fireworks!!!!!")

FPS = 60

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255), (255, 165, 0),
         (255, 255, 255), (230, 230, 250), (255, 192, 203)]


class Projectile:
    pass


class Firework:
    pass


class launcher:
    WIDTH = 15
    HEIGHT = 20
    COLOR = 'red'

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency  #ms
        self.start_time = time.time()
        self.fireworks = []

        def draw(self, win):
            pygame.draw.rect(win, self.COLOR,
                             (self.x, self.y, self.WIDTH, self.HEIGHT))


def draw(launchers):
    win.fill("black")

    for launcher in launchers:
        launcher.draw(win)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    launchers = [launcher(100, HEIGHT - launcher.HEIGHT, 3000)]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(launchers)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()