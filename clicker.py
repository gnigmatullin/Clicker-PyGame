import pygame
from random import randrange

# get random color except black 
def get_color():
    red = randrange(255)
    green = randrange(255)
    blue = randrange(255)
    if red < 10 and green < 10 and blue < 10:
        color = (255, 255, 255)
    else:
        color = (red, green, blue)
    return color

def main():
    # init game
    pygame.init()
    clock = pygame.time.Clock()
    screen_width = 640
    screen_height = 480
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Clicker')
    font = pygame.font.SysFont("arial", 16)
    
    level = 1
    score = 0
    hits = 0
    miss = 0
    
    # init ball
    color = get_color()
    radius = 0
    max_radius = 100
    pos = (10+randrange(screen_width-10), 10+randrange(screen_height-10))
    
    run = True

    # main game cycle    
    while run:
        # process events
        pressed = pygame.key.get_pressed()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    screen_color = screen.get_at((mouse_x, mouse_y))
                    if screen_color == color:
                        score = score + 100 - radius
                        color = get_color()
                        radius = 0
                        max_radius = 100
                        pos = (10+randrange(screen_width-10), 10+randrange(screen_height-10))
                        hits = hits + 1
                    else:
                        miss = miss + 1
                        score = score - radius
        # drawing
        screen.fill((0, 0, 0))
        text = font.render("Level: "+str(level), True, (255, 255, 255))
        screen.blit(text, (10, 5))
        text = font.render("Score: "+str(score), True, (255, 201, 14))
        screen.blit(text, (100, 5))
        text = font.render("Hits: "+str(hits), True, (34, 177, 76))
        screen.blit(text, (200, 5))
        text = font.render("Miss: "+str(miss), True, (237, 28, 36))
        screen.blit(text, (300, 5))
        pygame.draw.circle(screen, color, pos, radius)
        radius += 1
        if radius >= max_radius:
            color = get_color()
            radius = 0
            max_radius = 100
            pos = (10+randrange(screen_width-10), 10+randrange(screen_height-10))
            score = score - max_radius
            miss = miss + 1
        pygame.display.flip()
        if score <= -100:
            run = False
        # delay
        clock.tick(60)
        
    # game over
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("arial", 32)
    text = font.render("Game over!", True, (255, 255, 255))
    screen.blit(text, (screen_width/2-70, screen_height/2-50))
    pygame.display.flip()
    pygame.event.clear()
    pygame.event.wait()

main()
