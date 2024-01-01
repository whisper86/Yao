from pI import PI


def main(r):
    s = PI() * float(r)
    print("圆的面积为 %f" % s)


radius = input("输入圆的半径")
if __name__ == "__main__":
    main(r=radius)
