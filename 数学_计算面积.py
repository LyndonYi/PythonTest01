import math
while True:
    # 用户输入
    r = input("请输入圆的半径：")
    # 判断如果是字符则重新输入
    if not r.isalpha() :
        # 数据处理
        r = float(r)
        cicleArea = math.pi*r**2
        # 结果输出
        print("圆的面积是：%f"%cicleArea)
        break
    else:
        print("您输入的格式有误，请重新输入！")
        continue


        