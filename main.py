
import pygame

from Whale import player

from Boundries import stage

from Boundries import collectables



pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
win = pygame.font.Font(None,48)
running = True

whale = player(10,10)

wall = stage()


wall_list = wall.map()

pallets = collectables(-1000,-1000,8)

pallet_list = pallets.pallet_map()



def window_boundries():
    if whale.rect.x < 0:
       whale.rect.x = 0

    if whale.rect.x + whale.rect.width >= screen_width:
       whale.rect.x = screen_width - whale.rect.width
    
    if whale.rect.y <= 0:
       whale.rect.y = 0
    
    if whale.rect.y + whale.rect.height >= screen_height:
       whale.rect.y = screen_height - whale.rect.height


def win_codition():

    if len(pallet_list) == 0:
        text_surface = win.render("You win lol", True, (0,0,255))
        screen.blit(text_surface, (410,350))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
    screen.fill("Dark Blue")
    win_codition()
    whale.drawing(screen)
    whale.check_pallet_collisons(pallet_list)
    whale.moving()
    
    
    



    for wall in wall_list:
        wall.draw(screen)

    for pallets in pallet_list:
        pallets.draw(screen)
    
    
    
    win_codition()
    window_boundries()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()