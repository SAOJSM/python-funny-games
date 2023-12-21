import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設定遊戲視窗
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("坦克搶旗幟")

# 設定顏色
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# 設定遊戲參數
flag_position = (random.randint(50, width - 50), random.randint(50, height - 50))
player_position = [50, height // 2]
enemy_position = [width - 50, height // 2]
player_speed = 1  # 調整速度為1
enemy_speed = 1   # 調整速度為1
flag_taken = False

# 載入並調整圖片大小
tank_img = pygame.transform.scale(pygame.image.load("tank.png"), (50, 50))
flag_img = pygame.transform.scale(pygame.image.load("flag.png"), (50, 50))

# 設定字型
font = pygame.font.Font(None, 36)

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_position[1] > 0:
        player_position[1] -= player_speed
    if keys[pygame.K_DOWN] and player_position[1] < height - 50:
        player_position[1] += player_speed
    if keys[pygame.K_LEFT] and player_position[0] > 0:
        player_position[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_position[0] < width - 50:
        player_position[0] += player_speed

    # 移動敵方坦克
    if enemy_position[1] < player_position[1]:
        enemy_position[1] += enemy_speed
    elif enemy_position[1] > player_position[1]:
        enemy_position[1] -= enemy_speed
    if enemy_position[0] < player_position[0]:
        enemy_position[0] += enemy_speed
    elif enemy_position[0] > player_position[0]:
        enemy_position[0] -= enemy_speed

    # 檢查是否搶到旗幟
    if (
        player_position[0] < flag_position[0] < player_position[0] + 50
        and player_position[1] < flag_position[1] < player_position[1] + 50
    ):
        flag_taken = True

    # 更新畫面
    screen.fill(white)
    screen.blit(flag_img, flag_position)
    screen.blit(tank_img, player_position)
    screen.blit(tank_img, enemy_position)

    # 顯示文字
    if flag_taken:
        text = font.render("You Win!", True, blue)
        screen.blit(text, (width // 2 - 70, height // 2 - 20))

    pygame.display.flip()

# 關閉遊戲
pygame.quit()
sys.exit()
