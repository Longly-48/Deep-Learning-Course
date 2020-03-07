print("求一元二次方程ax²+bx+c=0（a≠0）的解，请输入对应a,b,c的值")
a = input("输入a的值：")
b = input("输入b的值：")
c = input("输入c的值：")
a = float(a)
b = float(b)
c = float(c)
delta = b * b - 4 * a * c
if delta < 0:
    print("无解！")
elif delta == 0:
    print("有一个解！")
    x = (-b) / (2 * a)
    print("它的解是：", x)
elif delta > 0:
    print("有两个解！")
    delta_sqrt = delta ** 0.5
    x1 = (-b + delta_sqrt) / (2 * a)
    x2 = (-b - delta_sqrt) / (2 * a)
    print("它的解是：", x1, x2)

