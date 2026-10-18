
name = "寒公子"
girlfriend = "Elsa"
brother = "付宽博"

# str.format()
print("我的姓名：{}，我的女友：{}，我的兄弟：{}".format(name, girlfriend, brother))
print("我的姓名：{R1}，我的女友：{R2}，我的兄弟：{R3}".format(R1=name, R2=girlfriend, R3=brother))

# f-string

"""1.填充表达："""
print("我的姓名：{name}，我的女友：{girlfriend}，我的兄弟：{brother}")
print(F"我的姓名：{name}，我的女友：{girlfriend}，我的兄弟：{brother}")

"""2.表达式："""
n1 = 12
n2 = 36
print(f"{n1} * {n2} = {n1 * n2}")

"""3.设置整数位数："""
money = 4213
print(f"我的存款：{money:10d}")          # “nd”表示显示为n位数，默认前面补 空格
print(f"我的存款：{money:010d}")         # “0nd”表示显示为n位数，前面补0
print("我的学号：9999999999")

"""4.保留小数精度："""
pai = 3.141592653589793
n3 = 9.11
print(f"圆周率 = {pai:.3f}")            # “nf”表示显示n位小数，超过n位遵循四舍五入
print(f"答案 = {n3:.3f}")               # “nf”表示显示n位小数，不足n位后面补0
