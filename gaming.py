import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Run Run")
clock = pygame.time.Clock()
test_font = pygame.font.Font("platformerGraphicsDeluxe_Updated/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("platformerGraphics_mushroomLand/Backgrounds/bg_grasslands.png")
ground_surface = pygame.image.load("platformerGraphicsDeluxe_Updated/ground.png")
text_surface = test_font.render("Pygame", False, "Black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)