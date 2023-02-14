import turtle as t


# 根据传入的参数绘制指定边长的五角星
def drawStar(x, y, length):
    # 提笔
    t.penup()
    # 位移
    t.goto(x, y)
    # 落笔
    t.pendown()
    # 改色
    t.color('yellow')
    # 开始填充
    t.begin_fill()
    for j in range(5):
        # 绘制
        t.forward(length)
        # 向左旋转72°
        t.left(72)
        # 绘制
        t.forward(length)
        # 向右旋转144°
        t.right(144)
    # 结束填充
    t.end_fill()


# 绘制矩形
def drawRect(x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


# 绘制五星红旗
def drawFlag():
    t.Screen().title("绘制五星红旗")
    # 国旗宽度，只需要改变这个值，就可以绘制不同尺寸的国旗了，其他值都是通过这个动态计算的
    # 让用户输入
    # width = t.numinput("红旗宽度", "请输入五星红旗宽度100~1200", 720, 100, 1200)
    width = 720

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
    t.color('red')

    # 1、写几个字
    t.penup()
    t.goto(0 - 40, rectY0 + 20)
    t.pendown()
    t.write("五星红旗", font=('Arial', 20))

    # 2、画矩形
    drawRect(rectX0, rectY0, width, height)

    # 3、画大五角星
    s1x = rectX0 + len1 * 1.5
    s1y = rectY0 - len1 * 2.5
    drawStar(s1x, s1y, len1)

    # 4、画四个小五角星
    # 第一个五角星的坐标
    x0 = rectX0 + len1 * 5
    y0 = rectY0 - len1
    for i in range(4):
        # 每个五角星都会在上一个的前提下再旋转24°
        t.right(24)
        # 调函数绘制五角星
        drawStar(x0, y0, len2)

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
