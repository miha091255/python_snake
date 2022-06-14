import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
grey = (169, 169, 169)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
direction = ''
pause = False


dis_width = 900
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змей')

clock = pygame.time.Clock()

snake_block = 10
standard_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    # value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    if score > 0:
        pygame.display.set_caption('Змей \t: ' + str(score))
    # dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        if snake_list.index(x) == (len(snake_list)-1):
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, grey, [x[0], x[1], snake_block, snake_block])


def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + pos * 22])


def game_loop():
    global standard_speed, direction, pause
    snake_speed = standard_speed
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(black)
            message("Потрачено", red, 0)
            message("С - заново", red, 1)
            message("Esc - Выход", red, 2)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    snake_speed = standard_speed
                if event.key == pygame.K_x:
                    snake_speed = standard_speed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_z:
                    snake_speed *= 2
                if event.key == pygame.K_x:
                    snake_speed = 5
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != 'right':
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'left'
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != 'left':
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'right'
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 'down':
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'up'
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 'up':
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'down'

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        # snake_head.append(x1)
        # snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        if not pause:
            pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        if not pause:
            clock.tick(snake_speed)

    pygame.quit()
    # quit()


game_loop()
