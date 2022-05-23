from types import CellType
import pygame
import random
import pickle


pygame.init()

snake_block = 20
cell_number = 30

dis_width = snake_block * (cell_number + 20)
dis_height = snake_block * cell_number

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timesnewroman", 35)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = 5x food')

     
num = 0

def spawn_xy(x, y):
    x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    return x, y

def snake(posx, posy, Length_of_snake, snake_List):
    snake_Head = []
    snake_Head.append(posx)
    snake_Head.append(posy)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == snake_Head:
            return True

def on_food(x1, y1, fx, fy, spx, spy, slx, sly, bx, by):
            if x1 == fx and y1 == fy:
                return "food"
            elif x1 == spx and y1 == spy:
                return "speed"
            elif x1 == slx and y1 == sly:
                return "slow"
            elif x1 == bx and y1 == by:
                return "bingo"
            
            
def speed_bonus(speed, p):
    if speed < 20:
        return p
    elif speed >= 20:
        return 2 * p
    
def speed(f, s):
    new_speed = f - s
    if new_speed < -10:
        new_speed = -10
    return new_speed

def check():
    try:
        game_state = pickle.load(open("savegame", "rb"))
        return game_state
    except EOFError:
        game_state = []
        return game_state
    
def time_tracker(time):
    if time <= 140:
        time += 1
    elif time > 140:
        time = 0
    return time

def save(snake_List, Length_of_snake, slow_speed, fast_speed, time, x1, y1, x1_change, y1_change, foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy):
    food_state = [foodx, foody, speedx, speedy, slowx, slowy, bingox, bingoy]
    game = [snake_List, Length_of_snake, slow_speed, fast_speed, food_state, time, x1, y1, x1_change, y1_change]
    return game

def snake_outside(x1, y1):
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        return True