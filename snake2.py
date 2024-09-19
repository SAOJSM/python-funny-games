import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("貪食蛇遊戲")

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

# Generate random food position
def generate_food():
    return (random.randint(0, (width - snake_block) // snake_block) * snake_block,
            random.randint(0, (height - snake_block) // snake_block) * snake_block)

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1
    food_position = generate_food()

    clock = pygame.time.Clock()

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
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, red, [food_position[0], food_position[1], snake_block, snake_block])

        # Update snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collisions with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for segment in snake_list:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == food_position[0] and y1 == food_position[1]:
            food_position = generate_food()
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

# Start the game
game_loop()
