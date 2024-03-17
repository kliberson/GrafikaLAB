import pygame
import sys

pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dwa trójkąty')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_triangle(surface, color, points):
    pygame.draw.polygon(surface, color, points)

def draw_rectangle(surface, color, rect):
    pygame.draw.rect(surface, color, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Czyszczenie ekranu
    screen.fill(WHITE)

    triangle1_points = [(width // 2, height // 2), (width // 2 - 50, height//2 + 100), (width // 2 + 50, height//2 + 100)]
    triangle2_points = [(width // 2, height// 2-100), (width // 2 - 50, height // 2 - 200), (width // 2 + 50, height // 2- 200)]

    rect_width = 220
    rect_height = 100
    rect_x = width//2 - rect_width//2
    rect_y = height//2-25 - rect_height//2-25


    draw_rectangle(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    draw_triangle(screen, BLUE, triangle1_points)
    draw_triangle(screen, BLUE, triangle2_points)
    # Odświeżenie ekranu
    pygame.display.flip()


pygame.quit()
sys.exit()
