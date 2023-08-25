from cgitb import grey
from turtle import delay
import pygame, sys #sys is used to exit program 
import os
import random
from pygame import mixer        # a class who handel all sound edit loop
pygame.mixer.init()     # for intializing the mixer 


mixer.music.load("start_sound.wav")    #mixer.music to play sound continuesly
mixer.music.play(-1)          #in this bracket we have to determine the music play times -1 for loop


player_lives = 2  # keep track of lives
score = 0  # keeps track of score
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb', 'apple']  # entities in the game

# initialize pygame and create window
WIDTH = 800
HEIGHT = 500
FPS =8 # controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()            #constructor
pygame.display.set_caption('Fruit Ninja Game') # ye caption k liye use hoga 
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))  # setting game display size
clock = pygame.time.Clock() # to control fps

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN=(54,33,5)
GREY = (120,120,120)


background = pygame.image.load('back.jpg')  # game background
background = pygame.transform.scale(background, (800, 500)) # background size
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))  # score display
  # images that shows remaining lives

# Generalized structure of the fruit Dictionary
def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),  # where the fruit should be positioned on x-coordinate
        'y': 800,
        'speed_x': random.randint(-10,10),
        # how fast the fruit should move in x direction. Controls the diagonal movement of fruits
        'speed_y': random.randint(-80, -60),  # control the speed of fruits in y-directionn ( UP )
        'throw': False,
        # determines if the generated coordinate of the fruits is outside the gameDisplay or not. If outside, then it will be discarded
        't': 0,  # manages the
        'hit': False,
    }

    if random.random() >= 0.75:  # Return the next random floating point number in the range [0.0, 1.0) to keep the fruits inside the gameDisplay
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False


# Dictionary to hold the data the random fruit generation
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)


def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))

def show_cross_lives(x,y):
    gameDisplay.blit(pygame.image.load("white_lives.png"),(x,y))
    #pygame.time.delay(20) for delaying the screen ////// stuck
#for event in pygame.event.get() :
    #if event.type == pygame.QUIT :
  


# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('comic.ttf')


def draw_text(display, text, size, x, y,z):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, z)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


# draw players lives
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        img_rect = img.get_rect()  # gets the (x,y) coordinates of the cross icons (lives on the the top rightmost side)
        img_rect.x = int(x + 35 * i)  # sets the next cross icon 35pixels awt from the previous one
        img_rect.y = y  # takes care of how many pixels the cross icon should be positioned from top of the screen
        display.blit(img, img_rect)


    

# show game over display & front display

def welcome():
   pass
        
def show_gameover_screen():
    if game_over:
        logo = pygame.image.load("welcome.jpg")
        gameDisplay.blit(logo,(0,0))
        draw_text(gameDisplay, "Press a key to begin!", 60, 430,370,WHITE)

       
                
    if not game_over:
        pass
    
  #  draw_text(gameDisplay, "Press a key to begin!", 64, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip() 
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                game_sound = mixer.Sound("click_s.wav")
                game_sound.play()
                waiting = False 

# Game Loop
first_round = True
game_over = True  # terminates the game While loop if more than 3-Bombs are cut
game_running = True  # used to manage the game loop
while game_running:
    if game_over:
        if first_round:
            show_gameover_screen()
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 760,15, player_lives, 'images/red_lives.png')
        
        score = 0

    for event in pygame.event.get():
        # checking for closing window
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
    #draw_white_lives(gameDisplay,760,15,player_lives, 'white_lives.png')

    for key, value in data.items():
        if value['throw']:
            

            value['x'] += value['speed_x']  # moving the fruits in x-coordinates
            value['y'] += value['speed_y']  # moving the fruits in y-coordinate
            value['speed_y'] += (1 * value['t'])  # increasing y-corrdinate
            value['t'] += 1  # increasing speed_y for next loop

            if value['y'] <= 800:
                gameDisplay.blit(value['img'],
                                 (value['x'], value['y']))  # displaying the fruit inside screen dynamically
            else:
                generate_random_fruits(key)

            current_position = pygame.mouse.get_pos()  # gets the current coordinate (x, y) in pixels of the mouse

            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x'] + 60 \
                    and current_position[1] > value['y'] and current_position[1] < value['y'] + 60:
                if key == 'bomb':
                    game_sound = mixer.Sound("bomb.wav")
                    game_sound.play()
                    player_lives -= 1
                    
                    if player_lives == 0:
                        hide_cross_lives(690, 15)
                        show_cross_lives(690,15)
                        game_over1 = pygame.image.load('game_over.png')  # game background
                        #background = pygame.transform.scale(game_over1, (260, 206))
                        gameDisplay.blit(game_over1,(142,135))
                        draw_text(gameDisplay, "   Your Total Score = " + str(score), 60, 400,340,WHITE)
                        pygame.display.flip() 
                       
                                        
                    elif player_lives == 1:
                        hide_cross_lives(725, 15)
                        show_cross_lives(725,15)
                    elif player_lives == 2:
                        hide_cross_lives(760, 15)
                        show_cross_lives(760,15)
                    # if the user clicks bombs for three time, GAME OVER message should be displayed and the window should be reset
                    if player_lives == 0:  # 3 plyr lives
                       # welcome()
                        game_sound = mixer.Sound("game_overmusic.wav")
                        game_sound.play()
                        show_gameover_screen()
                        game_over = True
                        

                    half_fruit_path = "images/explosion.png"
                else:
                    half_fruit_path = "images/" + "half_" + key + ".png"

                value['img'] = pygame.image.load(half_fruit_path)
                value['speed_x'] += 10
                if key != 'bomb':
                    score += 1
                    game_sound = mixer.Sound("cut.wav")
                    game_sound.play()   
                    
                score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                value['hit'] = True
        else:
            generate_random_fruits(key)
            


    pygame.display.update()
    clock.tick(FPS)  # keep loop running at the right speed (manages the frame/second. The loop should update afer every 1/12th pf the sec
    
    
    
pygame.quit()