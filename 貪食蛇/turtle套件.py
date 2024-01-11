from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#初始化畫布，設定長度，寬度和標題
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#tracer設定為0的作用是關閉動畫效果，我們通過timer設定延時，然後通過update手動重新整理介面，否則預設的動畫效果看起來就是每個方塊的移動效果
#想象一下GIF或者CRT顯示器的原理，多個畫面連續重新整理，看起來就像動起來一樣
screen.tracer(0)

#例項化三個物件
snake_segments = Snake()
food = Food()
scoreboard = Scoreboard()

#監聽上下左右的鍵盤操作
screen.listen()
screen.onkey(snake_segments.up, "Up")
screen.onkey(snake_segments.down, "Down")
screen.onkey(snake_segments.left, "Left")
screen.onkey(snake_segments.right, "Right")

#布林值判斷是否結束遊戲
game_is_on = True
while game_is_on:

#每次停頓0.1秒後重新整理一下介面，然後蛇移動一下
    screen.update()
    time.sleep(0.1)
    snake_segments.move()

# 如果蛇頭碰見食物了，那麼食物重新整理隨機生成一下，分數加一，蛇身長度加一
    if snake_segments.head.distance(food) < 15:
        print("yum yum yum")
        food.refresh()
        scoreboard.addscore()
        snake_segments.add_segment()

# 如果蛇頭撞牆了，那麼Game over

    if snake_segments.head.xcor() > 280 or snake_segments.head.xcor() < -280 or snake_segments.head.ycor() > 280 or snake_segments.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

# 如果蛇頭撞到身子了，那麼Game over，注意列表是從第二節開始的，排除蛇頭

    for seg in snake_segments.segments[1:]:

        if snake_segments.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
