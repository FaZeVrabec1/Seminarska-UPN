import pygame
import random
from pygame import *

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (184, 61, 186)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Ga...  Wait, what am I doing...   what is this?')

clock = pygame.time.Clock()

snake_block = 10
# size of snake
snake_speed = 15
# speed of snake

highscore = 0
#Highscore

font_style = pygame.font.SysFont("bahnschrift", 25)
# game lost text size
score_font = pygame.font.SysFont("Agency FB", 35)
# score text size





def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
    # score tracker


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def message2(score):
    value = score_font.render("Your Highscore was: " + str(score), True, white)
    dis.blit(value, [dis_width / 5, dis_height / 2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    # change of place on screen

    snake_List = []
    Length_of_snake = 1
    # number of snake blocks

    global snake_speed
    snake_speed = 10
    #snake speed

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    #food block

    food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    food3x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food3y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bgx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bgy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg3x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg3y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg4x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg4y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg5x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg5y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg6x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg6y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg7x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg7y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg8x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg8y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg9x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg9y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    bg10x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    bg10y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Decrise score

    cgx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    cgy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # game over

    srx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    sry = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    Music = True
    Sound_effect_Red = mixer.Sound("Red.wav")
    Sound_effect_Green = mixer.Sound("Green.wav")
    Sound_effect_White = mixer.Sound("White.wav")
    Sound_effect_Purple = mixer.Sound("Purple.wav")
    Sound_effect_lost = mixer.Sound("Lost.wav")
    # music & sounds




    while not game_over:


        if Music== True:
            background_music = mixer.Sound("Background.wav")
            background_music.play()
            background_music.set_volume(0.3)
            Music = False
        # Background music

        while game_close == True:
            dis.fill(blue)


            global highscore
            if Length_of_snake - 1 > highscore:
                highscore = Length_of_snake - 1
                #highscore


            message("You Lost! Press C-Play Again or Q-Quit", red)
            message2(highscore)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            # Displays & Messages




            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            # End screen input

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
                elif event.key == pygame.K_ESCAPE:
                   game_over = True
        # Game input

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, green, [food2x, food2y, snake_block, snake_block])
        pygame.draw.rect(dis, green, [food3x, food3y, snake_block, snake_block])
        # draws the add number food

        pygame.draw.rect(dis, red, [bgx, bgy, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg2x, bg2y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg3x, bg3y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg4x, bg4y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg5x, bg5y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg6x, bg6y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg7x, bg7y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg8x, bg8y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg9x, bg9y, snake_block, snake_block])
        pygame.draw.rect(dis, red, [bg10x, bg10y, snake_block, snake_block])
        # draws reduce score food

        pygame.draw.rect(dis, purple, [cgx, cgy, snake_block, snake_block])
        # draws game over food

        pygame.draw.rect(dis, white, [srx, sry, snake_block, snake_block])


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # The players character on the screen


        if len(snake_List) > Length_of_snake:
            del snake_List[0]


        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
            # if snake crash in snake lose game

        our_snake(snake_block, snake_List)
        # game character
        Your_score(Length_of_snake - 1)
        # score

        pygame.display.update()



        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            Sound_effect_Green.play()
            snake_speed += 1


        if x1 == food2x and y1 == food2y:
            food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            Sound_effect_Green.play()
            snake_speed += 1


        if x1 == food3x and y1 == food3y:
            food3x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food3y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            Sound_effect_Green.play()
            snake_speed += 1

        # food blocks and faster speed




        if x1 == bgx and y1 == bgy:
            bgx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bgy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg2x and y1 == bg2y:
            bg2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg3x and y1 == bg3y:
            bg3x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg3y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg4x and y1 == bg4y:
            bg4x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg4y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg5x and y1 == bg5y:
            bg5x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg5y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg6x and y1 == bg6y:
            bg6x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg6y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg7x and y1 == bg7y:
            bg7x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg7y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg8x and y1 == bg8y:
            bg8x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg8y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg9x and y1 == bg9y:
            bg9x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg9y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()


        if x1 == bg10x and y1 == bg10y:
            bg9x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            bg9y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_speed -= 1
            Sound_effect_Red.play()
        # score reduce blocks

        if x1 == cgx and y1 == cgy:
            game_close = True

        if x1 == srx and y1 == sry:
            srx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            sry = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Sound_effect_White.play()
            if snake_speed > 10:
                snake_speed = snake_speed / 2
        # Reduce speed blocks

        if -5 >= (Length_of_snake - 1):
            game_close = True

        if game_close == True:
            background_music.stop()
            if x1 == cgx and y1 == cgy:
                Sound_effect_Purple.play()
            else:
                Sound_effect_lost.play()








        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
