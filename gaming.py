import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Run Run")
clock = pygame.time.Clock()
test_font = pygame.font.Font("platformerGraphicsDeluxe_Updated/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("platformerGraphics_mushroomLand/Backgrounds/bg_grasslands.png").convert()
ground_surface = pygame.image.load("platformerGraphicsDeluxe_Updated/ground.png").convert()
text_surface = test_font.render("Run Run", False, "Black")

snail_surface = pygame.image.load("platformerGraphicsDeluxe_Updated/snailWalk1.png").convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))

    pygame.display.update()
    clock.tick(60)