import pygame
import sys

# 初始化pygame
pygame.init() 

# 定義顏色
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 設定視窗大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 設定標題
pygame.display.set_caption("搶旗幟遊戲") 

# 定義玩家類別
class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.width = 40
        self.height = 60
        
    # 移動方法
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            
        # 邊界檢測
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height

    # 畫圖方法        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
# 定義旗幟        
class Flag():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 40
        self.height = 60
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# 建立藍色玩家
player_1 = Player(100, 300, BLUE) 

# 建立紅色玩家
player_2 = Player(500, 300, RED)

# 建立中間的旗幟
flag = Flag(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, (0, 255, 0))

# 遊戲結束旗標
game_over = False

# 主迴圈
while True:

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    # 移動玩家
    player_1.move() 
    player_2.move()
    
    # 重新繪製屏幕
    screen.fill((255, 255, 255))  

    # 畫旗幟
    flag.draw()

    # 畫兩個玩家
    player_1.draw()
    player_2.draw()

    # 檢測玩家與旗幟碰撞
    if pygame.Rect.colliderect(player_1.x, player_1.y, player_1.width, player_1.height, flag.x, flag.y, flag.width, flag.height):
        print("藍色玩家得到旗幟,獲勝!")
        game_over = True

    if pygame.Rect.colliderect(player_2.x, player_2.y, player_2.width, player_2.height, flag.x, flag.y, flag.width, flag.height):
        print("紅色玩家得到旗幟,獲勝!")
        game_over = True

    # 顯示遊戲結束畫面  
    if game_over:
        font = pygame.font.Font(None, 60)
        text = font.render("遊戲結束", True, (0,0,0)) 
        screen.blit(text, (300,250))
        
        # 顯示重新開始按鈕
        again_btn = pygame.Rect(350, 300, 100, 50) 
        pygame.draw.rect(screen, RED, again_btn)
        btn_text = font.render("重新開始", True, (255,255,255))
        screen.blit(btn_text, (360,310))
        
        # 檢測重新開始按鈕是否被點擊
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if again_btn.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                game_over = False
        
    pygame.display.flip() 

pygame.quit()
