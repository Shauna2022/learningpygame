import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Run Run")
clock = pygame.time.Clock()
test_font = pygame.font.Font("platformerGraphicsDeluxe_Updated/Pixeltype.ttf", 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load("platformerGraphics_mushroomLand/Backgrounds/bg_grasslands.png").convert()
ground_surface = pygame.image.load("platformerGraphicsDeluxe_Updated/ground.png").convert()

# score_surf = test_font.render("Run Run", False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("platformerGraphicsDeluxe_Updated/snailWalk1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("platformerGraphicsDeluxe_Updated/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000) - start_time

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # pygame.draw.rect(screen, "#c0e8ec",  score_rect)
    # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    # screen.blit(score_surf, score_rect)
    # display_score()
    display_score()

    if game_active:
        # snail
        snail_rect.x -= 6
        if snail_rect.x <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        # player_rect.left += 1
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("pink")

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")
    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
