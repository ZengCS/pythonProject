import turtle as t


# 根据传入的参数绘制指定边长的五角星
def drawStar(length):
    t.begin_fill()
    for j in range(5):
        t.forward(length)
        t.left(72)
        t.forward(length)
        t.right(144)
    t.end_fill()


# 绘制五星红旗
def drawFlag():
    t.Screen().title("绘制五星红旗")
    # 国旗宽度，只需要改变这个值，就可以绘制不同尺寸的国旗了，其他值都是通过这个动态计算的
    width = t.numinput("红旗宽度", "请输入五星红旗宽度100~1200", 720, 100, 1200)

    # 国旗比例：3:2
    height = width / 3 * 2
    # 国旗左上角点的坐标
    rectX0 = -width / 2
    rectY0 = height / 2
    # 大五角星边长 = 国旗高度/10
    len1 = height / 10
    # 小五角星边长 = 大五角星边长/3
    len2 = len1 / 3

    # 设置画笔绘制速度，越大越快
    t.speed(10)
    # 1、画矩形
    t.penup()
    t.goto(rectX0, rectY0)
    t.pendown()
    t.color('red')
    t.begin_fill()
    for i in range(2):
        # 位移距离
        t.forward(width)
        # 右转角度
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    # 2、画大五角星
    t.penup()
    t.goto(rectX0 + len1 * 1.5, rectY0 - len1 * 2.5)
    t.pendown()
    t.color('yellow')
    # 调函数绘制五角星
    drawStar(len1)

    # 3、画四个小五角星
    # 第一个五角星的坐标
    x0 = rectX0 + len1 * 5
    y0 = rectY0 - len1
    for i in range(4):
        t.penup()
        t.goto(x0, y0)
        t.pendown()
        # 每个五角星都会在上一个的前提下再旋转24°
        t.right(24)
        # 调函数绘制五角星
        drawStar(len2)

        if i == 0:
            x0 += 3 * len2
            y0 -= 3 * len2
        elif i == 1:
            x0 += len2 / 2
            y0 -= len2 * 4
        elif i == 2:
            x0 -= len2 * 2.22
            y0 -= len2 * 3
    t.hideturtle()
    t.done()


# 调用绘制方法
drawFlag()
