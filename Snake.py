import pygame
import pickle
from GameFunctions import snake, spawn_xy, on_food, speed_bonus, speed, check, time_tracker, save, snake_outside, saved_game_exists
from DrawFunctions import draw_background, message, draw_our_snake, draw_rectangle, draw_score, draw_bingo, draw_slow

pygame.init()

num = 0
zero = [0, 0, 0, 0, 0]

white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (50, 153, 213)
red = (213, 50, 80)
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

    x1_change, y1_change, fast_speed, slow_speed, speed_change = zero

    snake_List = []
    timer = 0
    Length_of_snake = 1
    
    foodx, foody = spawn_xy(num, num)
    speedx, speedy = spawn_xy(num, num)
    slowx, slowy = spawn_xy(num, num)
    bingox, bingoy = spawn_xy(num, num)
    
    game_state = check()

    if saved_game_exists(game_state):
        snake_List, Length_of_snake, slow_speed, fast_speed, food_state, timer, x1, y1, x1_change, y1_change = game_state
        foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy = food_state
        
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            draw_score(Length_of_snake - 1)
            pygame.display.update()
            pickle.dump("", open("savegame", "wb"))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
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

        if snake_outside(x1, y1):
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(dark_blue)
        
        draw_background(dis)
        draw_rectangle(yellow, foodx, foody)
        draw_rectangle(red, speedx, speedy)
        draw_bingo(timer, white, bingox, bingoy)
        draw_slow(speed_change, blue, slowx, slowy)
                
        if snake(x1, y1, Length_of_snake, snake_List):
            game_close = True
 
        draw_our_snake(snake_block, snake_List)
        draw_score(Length_of_snake - 1)
        
        pygame.display.update()

        timer = time_tracker(timer)
        
        if timer == 80:
            bingox, bingoy = spawn_xy(bingox, bingoy)        

        food_eaten = on_food(x1, y1, foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy)
        
        if food_eaten == "food":
            foodx, foody = spawn_xy(foodx, foody)
            Length_of_snake += speed_bonus(speed_change, 1)
            
        elif food_eaten == "speed":
            speedx, speedy = spawn_xy(speedx, speedy)
            fast_speed += 10
            
        elif food_eaten == "slow":
            slowx, slowy = spawn_xy(slowx, slowy)
            slow_speed += 10
            
        elif food_eaten == "bingo":
            if timer in range(0,80):
                bingox, bingoy = spawn_xy(bingox, bingoy)
                Length_of_snake += speed_bonus(speed_change, 5)
            
        speed_change = speed(fast_speed, slow_speed)
        
        game_state = save(snake_List, Length_of_snake, slow_speed, fast_speed, timer, x1, y1, x1_change, y1_change, foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy)
        
        clock.tick(snake_speed + speed_change)
    
    pygame.quit()
    quit()
 
gameLoop()