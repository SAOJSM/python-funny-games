import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("坦克搶旗幟")

# 設定顏色
white = (255, 255, 255)
blue = (0, 0, 255)

# 設定遊戲參數
flag_position = pygame.Rect(random.randint(50, width - 50), random.randint(50, height - 50), 50, 50)
player_position = pygame.Rect(50, height // 2, 50, 50)
enemy_position = pygame.Rect(width - 100, height // 2, 50, 50)
player_speed = 1  # 調整速度為1
enemy_speed = 1   # 調整速度為1
flag_taken = False
game_active = False  # 新增遊戲活動狀態

# 載入並調整圖片大小
tank_img = pygame.transform.scale(pygame.image.load("tank.png"), (50, 50))
flag_img = pygame.transform.scale(pygame.image.load("flag.png"), (50, 50))

# 設定字型
font = pygame.font.Font(None, 36)

# 設定按鈕
start_button = pygame.Rect(50, 20, 100, 40)
restart_button = pygame.Rect(200, 20, 150, 40)
exit_button = pygame.Rect(400, 20, 100, 40)

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_active:
                if restart_button.collidepoint(event.pos):
                    flag_position.topleft = (random.randint(50, width - 50), random.randint(50, height - 50))
                    player_position.topleft = (50, height // 2)
                    enemy_position.topleft = (width - 100, height // 2)
                    flag_taken = False
                elif exit_button.collidepoint(event.pos):
                    running = False
            else:
                if start_button.collidepoint(event.pos):
                    game_active = True

    keys = pygame.key.get_pressed()
    if game_active:  # 當遊戲開始時才處理按鍵事件
        if keys[pygame.K_UP] and player_position.top > 0:
            player_position.y -= player_speed
        if keys[pygame.K_DOWN] and player_position.bottom < height:
            player_position.y += player_speed
        if keys[pygame.K_LEFT] and player_position.left > 0:
            player_position.x -= player_speed
        if keys[pygame.K_RIGHT] and player_position.right < width:
            player_position.x += player_speed

        # 移動敵方坦克
        if enemy_position.centery < flag_position.centery:
            enemy_position.y += enemy_speed
        elif enemy_position.centery > flag_position.centery:
            enemy_position.y -= enemy_speed
        if enemy_position.centerx < flag_position.centerx:
            enemy_position.x += enemy_speed
        elif enemy_position.centerx > flag_position.centerx:
            enemy_position.x -= enemy_speed

        # 檢查是否搶到旗幟
        if player_position.colliderect(flag_position):
            flag_taken = True

    # 更新畫面
    screen.fill(white)
    screen.blit(flag_img, flag_position.topleft)
    screen.blit(tank_img, player_position.topleft)
    screen.blit(tank_img, enemy_position.topleft)

    # 顯示文字
    if flag_taken:
        text = font.render("You Win!", True, blue)
        screen.blit(text, (width // 2 - 70, height // 2 - 20))

    # 顯示按鈕
    if not game_active:
        pygame.draw.rect(screen, blue, start_button)
        start_text = font.render("Start", True, white)
        screen.blit(start_text, (start_button.centerx - start_text.get_width() // 2, start_button.centery - start_text.get_height() // 2))
    else:
        pygame.draw.rect(screen, blue, restart_button)
        pygame.draw.rect(screen, blue, exit_button)
        restart_text = font.render("Restart", True, white)
        exit_text = font.render("Exit", True, white)
        screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
        screen.blit(exit_text, (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

    pygame.display.flip()

# 關閉遊戲
pygame.quit()
sys.exit()
