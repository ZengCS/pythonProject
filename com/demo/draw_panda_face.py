import matplotlib.pyplot as plt


def draw_panda_face():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # 耳朵-左
    ears1 = plt.Circle((0.2, 0.85), 0.1, color='black')
    ax.add_artist(ears1)

    # 耳朵-右
    ears1 = plt.Circle((0.8, 0.85), 0.1, color='black')
    ax.add_artist(ears1)

    # 画一个脸，盖住耳朵
    face = plt.Circle((0.5, 0.5), 0.45, color='#F2F2F2', )
    ax.add_artist(face)

    # 眼睛-左
    eyes1 = plt.Circle((0.3, 0.6), 0.1, color='#545454')
    ax.add_artist(eyes1)
    # 眼珠
    eyes1 = plt.Circle((0.32, 0.58), 0.02, color='black')
    ax.add_artist(eyes1)

    # 眼睛-右
    eyes2 = plt.Circle((0.7, 0.6), 0.1, color='#545454')
    ax.add_artist(eyes2)
    # 眼珠
    eyes2 = plt.Circle((0.68, 0.58), 0.02, color='black')
    ax.add_artist(eyes2)

    # 鼻子-外
    nose_out = plt.Circle((0.5, 0.4), 0.1, color='#545454', )
    ax.add_artist(nose_out)
    # 鼻子-内
    nose = plt.Circle((0.5, 0.4), 0.05, color='#222222')
    ax.add_artist(nose)

    # 画嘴巴
    mouth = plt.Rectangle((0.42, 0.2), 0.16, 0.02, angle=0.0, color='#222222', fill=True)
    ax.add_artist(mouth)
    mouth = plt.Circle((0.42, 0.21), 0.01, color='#222222')
    ax.add_artist(mouth)
    mouth = plt.Circle((0.58, 0.21), 0.01, color='#222222')
    ax.add_artist(mouth)

    # Remove axis
    plt.axis('off')

    # Show the plot
    plt.show()


draw_panda_face()
