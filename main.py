import pygame

pygame.init()
surface = pygame.display.set_mode((800, 500))

game_state = "start_menu"
color = (128, 128,128)
surface.fill(color)
pygame.display.flip()
screen_width =800
screen_height = 500
def draw_start_menu():
    surface.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    surface.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    surface.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if game_state == "start_menu":
            draw_start_menu()