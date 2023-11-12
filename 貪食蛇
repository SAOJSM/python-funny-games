import pygame
import random

# 遊戲窗口和背景設置
window_width = 800
window_height = 600
background_color = (0, 0, 0)

# 貪吃蛇和食物的屬性設置
snake_size = 20
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# 初始化遊戲
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('貪吃蛇遊戲')

# 貪吃蛇類
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((window_width / 2), (window_height / 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = snake_color

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction

        new = (((cur[0] + (x * snake_size)) % window_width), (cur[1] + (y * snake_size)) % window_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((window_width / 2), (window_height / 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], snake_size, snake_size))

# 食物類
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = food_color
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, window_width // snake_size - 1) * snake_size,
                         random.randint(0, window_height // snake_size - 1) * snake_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], snake_size, snake_size))

# 遊戲主循環
def main():
    clock = pygame.time.Clock()
    is_running = True
    snake = Snake()
    food = Food()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        window.fill(background_color)
        snake.draw(window)
        food.draw(window)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
