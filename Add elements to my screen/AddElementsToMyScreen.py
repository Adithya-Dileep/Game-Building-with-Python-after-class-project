import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Elements Example")
font = pygame.font.Font(None, 32)
text_surface = font.render("This is a rectangle.", True, white)
text_rect = text_surface.get_rect(center=(screen_width // 2, 50)) # Center near the top
rect_x = 50
rect_y = 100
rect_width = 200
rect_height = 150
my_rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    # Draw the rectangle onto the screen
    # arguments: (surface, color, rect_object)
    pygame.draw.rect(screen, blue, my_rectangle)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()
sys.exit()