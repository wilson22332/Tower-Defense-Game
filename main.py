import pygame


# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tower Defense')
time = clock.get_time()
# Create a font object
font = pygame.font.Font(None, 24)
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
welcome_font = pygame.font.SysFont("Arial",30)
# Create a surface for the button
button_surface = pygame.Surface((150, 50))
text_surface = my_font.render('Start', False, (255, 255, 255))
welcome_surface = my_font.render('Welcome To Tower Defense', False, (255, 255, 255))
# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(325, 125, 200, 50)  # Adjust the position as needed
rgb = (155, 255, 155)
show_button = True
show_start = True

# Start the main loop
while True:
    # Set the frame rate
    clock.tick(60)
    # Fill the display with color
    screen.fill(rgb)

    # Get events from the event queue
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
                if button_clicked == True:
                    print("happy")
                    rgb = (155,155,155)
                    show_button = False



    # Draw the button on the screen
    if show_button:
        print("plswork")
        screen.blit(button_surface, (500, 100))
        screen.blit(text_surface, (335, 100))
        screen.blit(welcome_surface, (100,100))

    # Update the game state
    pygame.display.update()