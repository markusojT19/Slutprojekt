import pygame

pygame.init()

red = (213, 50, 80)
green = (0, 100, 0)

snake_block = 20
cell_number = 30

dis_width = snake_block * (cell_number + 20)
dis_height = snake_block * cell_number

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timesnewroman", 35)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = 5x food')
 
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

def draw_our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def draw_rectangle(color, x, y):
    pygame.draw.rect(dis, color,[x, y, snake_block, snake_block])

def draw_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0]) 

def draw_bingo(time, white, bingox, bingoy):
    if time in range(0,80):
        draw_rectangle(white, bingox, bingoy)

def draw_slow(speed_change, blue, slowx, slowy):
    if speed_change > -10:
        draw_rectangle(blue, slowx, slowy)