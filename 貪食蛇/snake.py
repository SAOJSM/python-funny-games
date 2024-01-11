from turtle import Turtle

MOVE_DISTANCE=20
class Snake:

    #初始化的時候，蛇有三節，一字排開，放到一個列表裡
    def __init__(self):
        self.segments = []
        for i in range(3):
            seg = Turtle(shape="square")
            seg.color('white')
            seg.penup()
            seg.goto(0 - 20 * i, 0)
            self.segments.append(seg)
        self.head=self.segments[0]

    #這個是最核心的部分，每次移動的時候，從蛇尾巴往前迴圈，每個方塊往上一個方塊的座標移動，蛇頭自動往前跑

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    #蛇頭往上跑

    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(to_angle=90)
    #蛇頭往下跑

    def down(self):

        if self.head.heading() != 90:
            self.head.setheading(to_angle=270)
    #蛇頭往左跑

    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(to_angle=180)
    #蛇頭往右跑

    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(to_angle=0)

    #蛇的身子加1，原理是新建立一個例項，然後放到蛇尾巴的位置

    def add_segment(self):
        seg = Turtle(shape="square")
        seg.color('white')
        seg.penup()
        tail = self.segments[-1]
        seg.goto(tail.xcor(),tail.ycor())
        self.segments.append(seg)