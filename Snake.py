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
 
#storleken på spelrutan, går att göra helskärm och större om man vill, testade de 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Cappe o Maccuzer')
 
clock = pygame.time.Clock()
 
#storleken och hastigheten på ormen, bör kunna tillfälligt ändra dessa, aka powerups
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 #Stylar scoreboarden tror jag
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
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
 #Snake list är listan med kroppen senare, lengt håller bara kåll på din score, används inte praktiskt
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
            #game_close tar upp slutmenyn när den är True
        while game_close == True:
            #While loopen här visar menyn och väntar på att man ska trycka q eller c
            dis.fill(blue)
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
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
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
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        #kanske kan använda clock.tick för att bestämma tid för powerups
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()