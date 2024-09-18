# Start Generation Here
import pygame
import random

# 初始化pygame
pygame.init()

# 設定畫面大小
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("貪食蛇遊戲")

# 顏色設定
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 蛇的初始設定
snake_block = 10
snake_speed = 15  # 設定移動速度
snake_list = []
length_of_snake = 1

# 隨機生成紅點
def generate_food():
    return (random.randint(0, (width - snake_block) // snake_block) * snake_block,
            random.randint(0, (height - snake_block) // snake_block) * snake_block)

food_position = generate_food()

# 主遊戲循環
def game_loop():
    global food_position
    game_over = False
    game_close = False

    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0

    while not game_over:
        while game_close:
            screen.fill(black)
            font_style = pygame.font.SysFont("bahnschrift", 25)
            mesg = font_style.render("遊戲結束! 按C重新開始或按Q退出", True, red)
            screen.blit(mesg, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

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

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # 畫紅點
        pygame.draw.rect(screen, red, [food_position[0], food_position[1], snake_block, snake_block])

        # 更新蛇的身體
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        # 檢查是否吃到紅點
        if x1 == food_position[0] and y1 == food_position[1]:
            food_position = generate_food()
            length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

# 開始遊戲
game_loop()
# End Generation Here
