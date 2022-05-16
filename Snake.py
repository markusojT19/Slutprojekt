from types import CellType
import pygame
import time
import random
 
pygame.init()

#definierar färgerna med rgb, assmidigt att ändra dem till lite snyggare om vi vill
#Gjorde maten röd så det liknar äpplen o ormen grön men vi kanske vill göra nåt annat
#Så det inte är en orm som äter äpplen utan nåt lite roligare 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 100, 0)
blue = (50, 153, 213)
dark_blue = (3, 1, 55)
color = (1, 1, 1)
 
#storleken och hastigheten på ormen, bör kunna tillfälligt ändra dessa, aka powerups
snake_block = 20
snake_speed = 20
cell_number = 30

#storleken på spelrutan, går att göra helskärm och större om man vill, testade de 
dis_width = snake_block * cell_number
dis_height = snake_block * cell_number
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Green = snake   Blue = slow   Red = speed   Yellow = food   White = Bingo food')
 
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Timesnewroman", 35)
 
def draw_background(dis):
    background_color = (3, 1, 40)
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number):
                if col % 2 == 0:
                    background_rect = pygame.Rect(col * snake_block, row * snake_block, snake_block, snake_block)
                    pygame.draw.rect(dis, background_color, background_rect)
        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    background_rect = pygame.Rect(col * snake_block, row * snake_block, snake_block, snake_block)
                    pygame.draw.rect(dis, background_color, background_rect)

 #Stylar scoreboarden tror jag
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        #Denna funktion är det som ritar ormen så vi kan se den i spelet
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 #Stylar messaget som används senare
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 #Startpositionen, de delar med 2 för att få den att börja i mitten tror jag
    x1 = dis_width / 2
    y1 = dis_height / 2
 #Variablerna som anger vilket håll ormen ska åt sen när man trycker på knapparna
    x1_change = 0
    y1_change = 0
    fast_speed = 0
    slow_speed = 0
    new_speed = 0
    timer = 0
 #Snake list är listan med kroppen senare, lengt håller bara kåll på din score, används inte praktiskt
    snake_List = []
    Length_of_snake = 1
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
            #Anropar message funktionen
            message("You Lost! Press C-Play Again or Q-Quit", red)
            #Anropar Your_score funktionen
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #stänger ned när man klickar q
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #startar om när man klickar c
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
        if new_speed > -10:
            pygame.draw.rect(dis, blue, [slowx, slowy, snake_block, snake_block])
        if timer in range(0,60):
            pygame.draw.rect(dis, white, [bingox, bingoy, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        timer += 1
        if timer > 140:
            timer = 0
        
        #snake_list är listan med kroppens positioner, om huvudet är med tas huvudet bort
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        #Kollar om någon av kroppsdelarna har samma position som huvudet (man har krockat)
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
        #Kollar om huvudet är på maten, här kan vi försöka lägga till powerups
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
        
            
        if x1 == speedx and y1 == speedy:
            speedx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            speedy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            fast_speed += 10
        
        if x1 == slowx and y1 == slowy:
            slowx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            slowy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            slow_speed += 10
        
        #Fixar så farten aldrig går under 10
        new_speed = fast_speed - slow_speed
        if new_speed < -10:
            new_speed = -10
        
        if timer in range(0,80):
            if x1 == bingox and y1 == bingoy:
                bingox = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
                bingoy = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
                Length_of_snake += 5
        
        clock.tick(snake_speed + new_speed)
    
                
                
        
            
            
        #kanske kan använda clock.tick för att bestämma tid för powerups
        
 
    pygame.quit()
    quit()
 
 
gameLoop()