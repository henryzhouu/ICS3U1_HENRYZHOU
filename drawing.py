import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

# Screen dimensions and colors
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

WHITE = (255,255,255)
MOON = (246, 241, 213)
BLUE = (25, 25, 112)
LIGHTBLUE = (173, 216, 230)
GRAY = (169, 169, 169)
DARK_GRAY = (105, 105, 105)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
DARK_GREEN = (6, 64, 43)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)
CAR_COLOR = (255, 0, 0)

stars = [(random.randint(0, WIDTH), random.randint(0,HEIGHT//2)) for _ in range(50)]




# Initial positions
car_x = 0
car_2x = 0
pumpkin_x, pumpkin_y = 520, 460  
house_x, house_y = 300, 350
tree_x, tree_y = 150, 400
driveway_y = 500
house_lights_on = False
pumpkin_flicker = False
eyes_flicker = False
flicker_counter = 0 

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    car_x += 2
    if car_x > WIDTH:
        car_x = -100 
    car_2x += 5
    if car_2x > WIDTH:
        car_2x = -100
    eyes_flicker = random.choice([True, False, False, False, True, False, True, False]) 
    if house_x < car_x < house_x + 200:
        house_lights_on = True
    elif house_x < car_2x < house_x + 200:
        house_lights_on = True
    else:
        house_lights_on = False


    # DRAWING
    screen.fill(BLUE)

    #stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)

    #moon
    pygame.draw.circle(screen, MOON, (500, 80), 50)
    # driveway
    pygame.draw.rect(screen, DARK_GRAY, (0, driveway_y, WIDTH, 100)) 

    # house
    pygame.draw.rect(screen, GRAY, (house_x, house_y, 200, 150))
    pygame.draw.polygon(screen, DARK_GRAY, [(house_x, house_y), (house_x + 200, house_y), (house_x + 100, house_y - 80)])
    pygame.draw.rect(screen, BROWN, (house_x + 85, house_y + 90, 30, 60))

    # windows+person
    if house_lights_on:
        pygame.draw.rect(screen, YELLOW, (house_x + 30, house_y + 20, 30, 30))
        pygame.draw.rect(screen, YELLOW, (house_x + 140, house_y + 20, 30, 30))
        pygame.draw.circle(screen, BLACK, (house_x + 40, house_y + 30), 5)
        pygame.draw.rect(screen, BLACK, (house_x + 37.75,house_y + 32, 5, 18))
        pygame.draw.rect (screen, BLACK, (house_x + 38, house_y + 35, 10, 3))
        pygame.draw.rect(screen,BLACK, (house_x + 33, house_y + 35, 10,3))
    else:
        pygame.draw.rect(screen, BLACK, (house_x + 30, house_y + 20, 30, 30))
        pygame.draw.rect(screen, BLACK, (house_x + 140, house_y + 20, 30, 30))



    # trees and pumpkin
    pygame.draw.rect(screen, BROWN, (tree_x + 70, tree_y, 20,100))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x+ 50,tree_y+50),(tree_x + 110,tree_y+50),(tree_x + 80, tree_y - 50)))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x+ 50,tree_y+30),(tree_x + 110,tree_y+30),(tree_x + 80, tree_y - 80)))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x+ 50,tree_y+10),(tree_x + 110,tree_y+10),(tree_x + 80, tree_y - 110)))
    pygame.draw.rect(screen, BROWN, (tree_x -10, tree_y, 20,100))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x -40,tree_y+50),(tree_x + 40,tree_y+50),(tree_x, tree_y - 50)))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x -40,tree_y+30),(tree_x + 40,tree_y+30),(tree_x, tree_y - 80)))
    pygame.draw.polygon(screen, DARK_GREEN, ((tree_x -40,tree_y+10),(tree_x + 40,tree_y+10),(tree_x, tree_y - 110)))
    pygame.draw.rect(screen, BROWN, (tree_x, tree_y, 20, 100))
    pygame.draw.circle(screen, GREEN, (tree_x + 10, tree_y - 30), 40)
    pygame.draw.rect(screen, BROWN, (tree_x - 100, tree_y,20, 100))
    pygame.draw.circle(screen, GREEN, (tree_x - 90, tree_y - 30), 40, 50)
    pygame.draw.ellipse(screen, ORANGE, (pumpkin_x, pumpkin_y, 50, 40)) 
    pygame.draw.rect(screen, BROWN, (pumpkin_x + 21, pumpkin_y - 10, 5, 10))

    if eyes_flicker:
        pygame.draw.ellipse(screen, YELLOW, (pumpkin_x + 8, pumpkin_y + 5, 10, 18))
        pygame.draw.ellipse(screen, YELLOW, (pumpkin_x + 28, pumpkin_y + 5, 10, 18))
        pygame.draw.ellipse(screen, YELLOW, (pumpkin_x+ 14, pumpkin_y+ 25, 20, 10))
    else:
        pygame.draw.ellipse(screen, BLACK, (pumpkin_x + 8, pumpkin_y + 5, 10, 18))
        pygame.draw.ellipse(screen, BLACK, (pumpkin_x + 30, pumpkin_y + 5, 10, 18))
        pygame.draw.ellipse(screen,BLACK, (pumpkin_x+ 14, pumpkin_y+ 25, 20, 10))




    # car
    pygame.draw.rect(screen, CAR_COLOR, (car_x, driveway_y - 30, 60, 30)) 
    pygame.draw.rect(screen,BLUE, (car_2x ,driveway_y - 40, 40, 30))
    pygame.draw.circle(screen, BLACK, (car_x + 10, driveway_y), 10) 
    pygame.draw.circle(screen, BLACK, (car_x + 50, driveway_y), 10)
    pygame.draw.circle(screen, GRAY, (car_x + 10, driveway_y), 7)
    pygame.draw.circle(screen, GRAY, (car_x + 50, driveway_y), 7)

    pygame.draw.rect(screen, LIGHTBLUE, (car_2x, driveway_y - 30, 60, 30)) 
    pygame.draw.rect(screen,LIGHTBLUE, (car_2x ,driveway_y - 40, 40, 30))
    pygame.draw.circle(screen, BLACK, (car_2x + 10, driveway_y), 10) 
    pygame.draw.circle(screen, BLACK, (car_2x + 50, driveway_y), 10)
    pygame.draw.circle(screen, GRAY, (car_2x + 10, driveway_y), 7)
    pygame.draw.circle(screen, GRAY, (car_2x + 50, driveway_y), 7)


    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

# Quit Pygame
pygame.quit()