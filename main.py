import pygame as pg
import pygame
from background import Background
from enemy import Enemy

# Initialize Pygame
pygame.init()
# Background of the actual game
background = pygame.image.load('background.png')
default_background_size = (1000,500)
background = pygame.transform.scale(background,default_background_size)
default_background_position =(10,50)
#Frames
clock = pygame.time.Clock()
#Where the background is going to be
b=Background(50,30)
# Create a Pygame window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tower Defense')
time = clock.get_time()

#initlizaing enemies
enemy_image = pygame.image.load('enemy.png')
enemy = Enemy((200,300), enemy_image)
enemy_image = pygame.image.load('enemy.png')
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
        screen.blit(background, default_background_position)
        screen.blit(image, (200,300))


    pg.display.flip()
