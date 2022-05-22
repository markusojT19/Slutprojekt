from types import CellType
import pygame
import time
import random
import pickle
import functions

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 100, 0)
blue = (50, 153, 213)
dark_blue = (3, 1, 55)

snake_block = 20
snake_speed = 20
cell_number = 30

dis_width = snake_block * (cell_number + 20)
dis_height = snake_block * cell_number

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timesnewroman", 35)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = 5x food')

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
    
def draw_background(dis):
    background_color = (3, 1, 40)
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number + 20):
                if col % 2 == 0:
                    background_rect = pygame.Rect(col * snake_block, row * snake_block, snake_block, snake_block)
                    pygame.draw.rect(dis, background_color, background_rect)
        else:
            for col in range(cell_number + 20):
                if col % 2 != 0:
                    background_rect = pygame.Rect(col * snake_block, row * snake_block, snake_block, snake_block)
                    pygame.draw.rect(dis, background_color, background_rect)  

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 2])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        
num = 0

def spawn_x(x):
    x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    return x
    
def spawn_y(y):
    y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    return y

def rectangle(color, x, y):
    pygame.draw.rect(dis, color,[x, y, snake_block, snake_block])

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

def food_pickup(x1, y1, fx, fy):
            if x1 == fx and y1 == fy:
                return True