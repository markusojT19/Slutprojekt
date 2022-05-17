from types import CellType
import pygame
import time
import random
 
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
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = 5x food')
 
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timesnewroman", 35)
 
#Stylar bakgrunden, rutnätet
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

#Ritar ut score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

#Ritar ut ormen baserat på dess längd
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
#Stylar och placerar messaget som används senare
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 2])
 
def gameLoop():
    game_over = False
    game_close = False
 #Startpositionen
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
    
    #Sätter startpositionerna för mat, respektive boosters
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
 
    speedx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    speedy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    
    slowx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    slowy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    
    bingox = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    bingoy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
 
    while not game_over:
            #game_close tar upp slutmenyn när den är True
        while game_close == True:
            #While loopen här visar menyn och väntar på att man ska trycka q eller c
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #Kollar om man trycker på quit knappen och ser till att ormen rör sig när man trycker på knapparna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
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
        #kollar om ormen krockar med kanten av skärmen, avbryter isåfall
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(dark_blue)
        draw_background(dis)
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, red, [speedx, speedy, snake_block, snake_block])
        if speed_change > -10:
            pygame.draw.rect(dis, blue, [slowx, slowy, snake_block, snake_block])
        if timer in range(0,80):
            pygame.draw.rect(dis, white, [bingox, bingoy, snake_block, snake_block])
       
        timer += 1
        if timer > 140:
            timer = 0
       
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #snake_list är listan med kroppens positioner
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        #Kollar om någon av kroppsdelarna har samma position som huvudet (man har krockat)
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            if speed_change < 20:
                Length_of_snake += 1
            elif speed_change >= 20:
                Length_of_snake += 2
        
            
        if x1 == speedx and y1 == speedy:
            speedx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            speedy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            fast_speed += 10
        
        if x1 == slowx and y1 == slowy:
            slowx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            slowy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            slow_speed += 10
        
        #Fixar så farten aldrig går under 10
        speed_change = fast_speed - slow_speed
        if speed_change < -10:
            speed_change = -10
        
        if timer in range(0,80):
            if x1 == bingox and y1 == bingoy:
                bingox = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
                bingoy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
                if speed_change < 20:
                    Length_of_snake += 5
                elif speed_change >= 20:
                    Length_of_snake += 10
        
        if timer == 80:
            bingox = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            bingoy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        
        clock.tick(snake_speed + speed_change)
    
                
        
 
    pygame.quit()
    quit()
 
 
gameLoop()