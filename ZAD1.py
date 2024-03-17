import pygame
import math

pygame.init()

window_size = (600, 600)
window = pygame.display.set_mode(window_size)

background_color = (255, 255, 255)
polygon_outline_color = (0, 0, 0)
polygon_fill_color = (235, 97, 97)

radius = 150
num_points = 7
angle = 2 * math.pi / num_points
position = (window_size[0] // 2, window_size[1] // 2)

rotation_angle = 0
scale_factor = 1
vertical_stretch_factor = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            position = (window_size[0] // 2, window_size[1] // 2)
            
            if event.key == pygame.K_1:
                rotation_angle = 0
                scale_factor = 1
                vertical_stretch_factor = 1

            elif event.key == pygame.K_2:
                rotation_angle = math.radians(45)
                scale_factor = 1.5
                vertical_stretch_factor = 1

            elif event.key == pygame.K_3:
                rotation_angle = math.radians(180)
                scale_factor = 1
                vertical_stretch_factor = 1.1
                
            elif event.key == pygame.K_4:
                rotation_angle = math.radians(25)
                scale_factor = 1
                vertical_stretch_factor = 0.5

            elif event.key == pygame.K_5:
                position = (window_size[0] // 2, window_size[1] - 500)
                rotation_angle = 0
                scale_factor = 1
                vertical_stretch_factor = 0.3

            elif event.key == pygame.K_6:
                rotation_angle = math.radians(25) + math.radians(90)
                scale_factor = 1
                vertical_stretch_factor = 0.5

            elif event.key == pygame.K_7:
                rotation_angle = math.radians(180)
                scale_factor = 1
                vertical_stretch_factor = 1.1

            elif event.key == pygame.K_8:
                position = (window_size[0] // 2 - 100, window_size[1] - 100)
                rotation_angle = math.radians(135)
                scale_factor = 1
                vertical_stretch_factor = 0.4

            elif event.key == pygame.K_9:
                position = (window_size[0] // 2 + 150, window_size[1] // 2)
                rotation_angle = math.radians(25) + math.radians(90) + math.radians(180)
                scale_factor = 1
                vertical_stretch_factor = 1

    window.fill(background_color)
    points = []
    for i in range(num_points):
        x = position[0] + radius * scale_factor * math.cos(i * angle + rotation_angle)
        y = position[1] + (radius * scale_factor * math.sin(i * angle + rotation_angle)) * vertical_stretch_factor
        points.append((x, y))
    pygame.draw.polygon(window, polygon_fill_color, points)
    pygame.draw.polygon(window, polygon_outline_color, points, 1)
    pygame.display.flip()

pygame.quit()
