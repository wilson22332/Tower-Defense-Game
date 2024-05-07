import pygame

pygame.init()
surface = pygame.display.set_mode((800, 500))

color = (128, 128,128)
surface.fill(color)
rectangle_position = (400, 300) # Centre of screen
rectangle_dimension = (100, 100) # Width and Height
rectangle = pygame.Rect(rectangle_position, rectangle_dimension)
rectangle_color = (255,0,0)

running = True
while running:
    pygame.draw.rect(surface, rectangle_color, rectangle)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # Get click position
            if rectangle.collidepoint(x, y):  # Check if click is within rectangle
                surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("left mouse button")
            elif event.button == 2:
                print("middle mouse button")
            elif event.button == 3:
                print("right mouse button")
            elif event.button == 4:
                print("mouse wheel up")
            elif event.button == 5:
                print("mouse wheel down")