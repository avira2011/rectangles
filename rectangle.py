import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill('black')
pygame.display.update()

class Rectangle():
    def __init__(self, color, dimensions):
        self.color = color
        self.dimensions = dimensions
        self.surface = screen
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.surface,self.color,self.dimensions)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
    blue_rect = Rectangle('blue', (50,20,100,50))
    blue_rect.draw()

    white_rect = Rectangle('white', (150,20,150,75))
    white_rect.draw()

    green_rect = Rectangle('green', (50,100,200,100))
    green_rect.draw()

    red_rect = Rectangle('red', (300,100,60,10))
    red_rect.draw()

    yellow_rect = Rectangle('yellow', (0,400,500,50))
    yellow_rect.draw()
    pygame.display.update()

