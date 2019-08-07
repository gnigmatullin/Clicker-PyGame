import pygame
from random import randrange

# Init game
pygame.init()
screen_width = 640
screen_height = 480
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clicker')
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (30, 30, 30)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Get random color except black
def get_color():
    red = randrange(255)
    green = randrange(255)
    blue = randrange(255)
    if red < 10 and green < 10 and blue < 10:
        color = (255, 255, 255)
    else:
        color = (red, green, blue)
    return color

# Text Renderer
def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont("arial", textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# Main Menu
def main_menu():
    menu=True
    selected="start"
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        main()
                    if selected=="quit":
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.fill(black)
        title=text_format("Clicker", 90, yellow)
        if selected=="start":
            text_start=text_format("START", 75, white)
        else:
            text_start = text_format("START", 75, gray)
        if selected=="quit":
            text_quit=text_format("QUIT", 75, white)
        else:
            text_quit = text_format("QUIT", 75, gray)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)

def main():
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
        clock.tick(FPS)
        
    # game over
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("arial", 32)
    text = font.render("Game over!", True, (255, 255, 255))
    screen.blit(text, (screen_width/2-70, screen_height/2-50))
    pygame.display.flip()
    pygame.event.clear()
    pygame.event.wait()

main_menu()
