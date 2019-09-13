import pygame
from random import randrange

# Init game
pygame.init()
screen_width = 640
screen_height = 480
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((screen_width, screen_height))
caption = 'Clicker v.1.1'
pygame.display.set_caption(caption)
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
    newFont = pygame.font.Font("retro.ttf", textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# Main Menu
def main_menu():
    menu=True
    selected=0
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if mouse_y > 300 and mouse_y < 360:
                    selected=0
                elif mouse_y > 360 and mouse_y < 420:
                    selected=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if mouse_y > 300 and mouse_y < 360:
                        selected=0
                        main()
                    elif mouse_y > 360 and mouse_y < 420:
                        selected=1
                        pygame.quit()
                        quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected=selected+1
                    if selected > 1:
                        selected = 0
                elif event.key==pygame.K_DOWN:
                    selected=selected-1
                    if selected < 0:
                        selected = 1
                if event.key==pygame.K_RETURN:
                    if selected==0:
                        main()
                    if selected==1:
                        pygame.quit()
                        quit()
        # Main Menu UI
        screen.fill(black)
        title=text_format(caption, 90, yellow)
        if selected==0:
            pygame.draw.rect(screen, (128, 128, 255), pygame.Rect(10, 300, screen_width-20, 60))
            text_start=text_format("START", 75, white)
        else:
            text_start = text_format("START", 75, gray)
        if selected==1:
            pygame.draw.rect(screen, (128, 128, 255), pygame.Rect(10, 360, screen_width-20, 60))
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
    level = 1
    score = 0
    hits = 0
    miss = 0
    
    # load sounds
    hit_wav = pygame.mixer.Sound('hit.wav')
    miss_wav = pygame.mixer.Sound('miss.wav')
    
    # load music
    pygame.mixer.music.load('background.mid')
    pygame.mixer.music.play(-1)

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
                pygame.mixer.music.stop()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    screen_color = screen.get_at((mouse_x, mouse_y))
                    if screen_color == color:   # hit
                        score = score + 100 - radius
                        if score > 1000 and score < 2000:
                            level = 2
                        elif score > 2000 and score < 3000:
                            level = 3
                        elif score > 3000 and score < 4000:
                            level = 4
                        elif score > 4000 and score < 5000:
                            level = 5
                        elif score > 5000 and score < 6000:
                            level = 6
                        elif score > 6000 and score < 7000:
                            level = 7
                        elif score > 7000 and score < 8000:
                            level = 8
                        elif score > 8000:
                            level = 9
                        color = get_color()
                        radius = 0
                        max_radius = 100
                        pos = (10+randrange(screen_width-10), 10+randrange(screen_height-10))
                        hits = hits + 1
                        hit_wav.play()
                    else:   # miss
                        miss = miss + 1
                        miss_wav.play()
        # drawing
        screen.fill((0, 0, 0))
        font = pygame.font.Font("retro.ttf", 25)
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
        clock.tick(level*10)
        
    # game over
    pygame.mixer.music.stop()
    
    screen.fill((0, 0, 0))
    font = pygame.font.Font("retro.ttf", 75)
    text = font.render("Game over!", True, yellow)
    screen.blit(text, (screen_width/2-140, screen_height/2-50))
    pygame.display.flip()
    pygame.event.clear()
    pygame.event.wait()

main_menu()
