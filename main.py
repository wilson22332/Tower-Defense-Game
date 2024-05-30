
import pygame
from background import Background
from user import Enemy
import math

# Initialize Pygame
pygame.init()
# Create a Pygame window
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
# Background of the actual game
background = pygame.image.load('background.png')
default_background_size = (1000,500)
background = pygame.transform.scale(background,default_background_size)
default_background_position =(10,50)
background_width = background.get_width()
background_rect = background.get_rect()
#Tiles
tiles = math.ceil(SCREEN_WIDTH/background_width)+1
#Scrolling background
scroll = 0

#Frames
clock = pygame.time.Clock()
#Where the background is going to be
b=Background(50,30)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Geometry Dash')
time = clock.get_time()

#initlizaing enemies
enemy_image = pygame.image.load('user.png')
enemy = Enemy((200,300), enemy_image)
enemy_image = pygame.image.load('user.png')
image = pygame.transform.scale(enemy_image, (100,100))

# Create a font object
font = pygame.font.Font(None, 24)
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
welcome_font = pygame.font.SysFont("Arial",30)

# Create a surface for the button
button_surface = pygame.Surface((150, 50))
text_surface = my_font.render('Start', False, (255, 255, 255))
welcome_surface = my_font.render('Welcome To Tower Defense', False, (255, 255, 255))
button_surface_size = button_surface.get_size()
button_rect = pygame.Rect(350, 300, button_surface_size[0], button_surface_size[1])
rgb = (155, 255, 155)
show_button = True
show_start = True
showing_background = False
run = True
# Start the main loop
while True:
    # Set the frame rate
    clock.tick(60)
    # Fill the display with color
    screen.fill(rgb)
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            run = False
            pygame.quit()

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if button_rect.collidepoint(event.pos):
                button_clicked = True
                if button_clicked and showing_background == False:
                    showing_background = True
                    show_button = False





    # Draw the button on the screen
    if show_button:
        screen.blit(button_surface, (340, 300))
        screen.blit(text_surface, (380, 300))
        screen.blit(welcome_surface, (250,200))
    if showing_background:

        for i in range(0,tiles):
            screen.blit(background,(i * background_width - scroll,0))
            pygame.draw.rect(screen,(255,0,0), background_rect)
        scroll -= 5
        if abs(scroll)> background_width:
            scroll =0
        screen.blit(background, default_background_position)
        screen.blit(image, (200,300))


    pygame.display.update()
