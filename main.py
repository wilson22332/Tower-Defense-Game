import pygame
from background import Background

import math

# Initialize Pygame
pygame.init()
# Create a Pygame window
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
# Background of the actual game
background = pygame.image.load('background.png')
default_background_size = (1000,500)
background = pygame.transform.scale(background,default_background_size)
default_background_position =(10,50)
background_width = background.get_width()
background_rect = background.get_rect()
#Tiles
tiles = math.ceil(SCREEN_WIDTH/background_width)+1

scroll = 0

#Frames
clock = pygame.time.Clock()
b=Background(50,30)

#platform
x = 100
y = 150

# Creating a rect with width
# and height
platform_rect = pygame.Rect(x, y, 200, 50)
platform_vel =5
rect = pygame.Rect(135, 220, 30, 30)
vel = 5
jump_height = 10
is_jumping = False
jump_velocity = 0
gravity = 0.5
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Geometry Dash')
time = clock.get_time()
font = pygame.font.Font(None, 24)
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
welcome_font = pygame.font.SysFont("Arial",30)
button_surface = pygame.Surface((150, 50))
text_surface = my_font.render('Start', False, (255, 255, 255))
welcome_surface = my_font.render('Welcome to Geometry Run', False, (255, 255, 255))
button_surface_size = button_surface.get_size()
button_rect = pygame.Rect(640, 300, button_surface_size[0], button_surface_size[1])
rgb = (173,216,230)
show_button = True
show_start = True
showing_background = False
run = True

while True:

    clock.tick(60)
    screen.fill(rgb)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                button_clicked = True
                if button_clicked and showing_background == False:
                    showing_background = True
                    show_button = False
    if show_button:
        screen.blit(button_surface, (640, 300))
        screen.blit(text_surface, (680, 300))
        screen.blit(welcome_surface, (550,200))
    if showing_background:

        for i in range(0, tiles):

            screen.blit(background, (i * background_width + scroll, 0))
            background_rect.x = i * background_width + scroll
            keys = pygame.key.get_pressed()
            rect.centerx = (rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % 300
            if platform_rect.left >= 300 or platform_rect.left < 100:
                platform_vel *= -1

                # Adding platform_vel to x
                # coordinate of our rect
            platform_rect.left += platform_vel
            pygame.draw.rect(screen, (255, 0, 0), platform_rect)
            if keys[pygame.K_SPACE] and not is_jumping:
                is_jumping = True
                jump_velocity = -jump_height
            if is_jumping:
                rect.y += jump_velocity
                jump_velocity += gravity
                if rect.y >= 220:
                    rect.y = 220
                    is_jumping = False
                    jump_velocity = 0

            pygame.draw.circle(screen, (255, 0, 0), rect.center, 15)
        pygame.display.flip()

        scroll -= 5 

        # reset scroll
        if abs(scroll) > background_width:
            scroll = 0


    pygame.display.update()
