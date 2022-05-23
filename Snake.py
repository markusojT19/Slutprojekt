from queue import Empty
from types import CellType
import pygame
import time
import random
import pickle
from operator import itemgetter
from functions import Your_score, draw_background, message, our_snake, snake, spawn_xy, draw_rectangle, food_pickup, speed_bonus

pygame.init()

num = 0

white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 100, 0)
black = (0, 0, 0)
dark_blue = (3, 1, 55)
 
snake_block = 20
snake_speed = 20
cell_number = 30

dis_width = snake_block * (cell_number + 20)
dis_height = snake_block * cell_number
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = 5x food')
 
clock = pygame.time.Clock()

    
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    fast_speed = 0
    slow_speed = 0
    speed_change = 0
    timer = 0

    snake_List = []
    Length_of_snake = 1
    
    foodx, foody = spawn_xy(num, num)
 
    speedx, speedy = spawn_xy(num, num)
    
    slowx, slowy = spawn_xy(num, num)
    
    bingox, bingoy = spawn_xy(num, num)
    
    try:
        game_state = pickle.load(open("savegame", "rb"))
    except EOFError:
        game_state = []

    if len(game_state) > 0:
        snake_List, Length_of_snake, slow_speed, fast_speed, food_state, timer, x1, y1, x1_change, y1_change = itemgetter(*range(0,10))(game_state)
        foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy = itemgetter(*range(0,8))(food_state)
        
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            pickle.dump("", open("savegame", "wb"))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        food_state = [foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy]
        game_state = [snake_List] + [Length_of_snake] + [slow_speed] + [fast_speed] + [food_state] + [timer] + [x1] + [y1] + [x1_change] + [y1_change]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pickle.dump("", open("savegame", "wb"))
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pickle.dump(game_state, open("savegame", "wb"))
                    game_over = True
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(dark_blue)
        draw_background(dis)
        draw_rectangle(yellow, foodx, foody)
        draw_rectangle(red, speedx, speedy)
        if speed_change > -10:
            draw_rectangle(blue, slowx, slowy)
        if timer in range(0,80):
            draw_rectangle(white, bingox, bingoy)
            
        timer += 1
        if timer > 140:
            timer = 0
        
        if snake(x1, y1, Length_of_snake, snake_List):
            game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
        
        if food_pickup(x1, y1, foodx, foody):
            foodx, foody = spawn_xy(foodx, foody)
            Length_of_snake += speed_bonus(speed_change, 1)
            
        if food_pickup(x1, y1, speedx, speedy):
            speedx, speedy = spawn_xy(speedx, speedy)
            fast_speed += 10
        
        if food_pickup(x1, y1, slowx, slowy):
            slowx, slowy = spawn_xy(slowx, slowy)
            slow_speed += 10
        
        speed_change = fast_speed - slow_speed
        if speed_change < -10:
            speed_change = -10
        
        if timer in range(0,80):
            if food_pickup(x1, y1, bingox, bingoy):
                bingox, bingoy = spawn_xy(bingox, bingoy)
                Length_of_snake += speed_bonus(speed_change, 5)
        
        if timer == 80:
            bingox, bingoy = spawn_xy(bingox, bingoy)
        
        clock.tick(snake_speed + speed_change)
    
    pygame.quit()
    quit()
 
gameLoop()