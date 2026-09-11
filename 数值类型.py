
"""整形数据int：整数"""
寒公子 = 100000000000000000
print(寒公子, type(寒公子))                # type(x)表示x的数据类型

"""浮点型数据float：含有小数点的数据"""
小鱼儿 = 2718280000000000.0
print(小鱼儿, type(小鱼儿))
Elsa = 12345678901234567890.1
print(Elsa, type(Elsa))

"""布尔型数据bool：True/False"""
print(True, type(True))
print(False, type(False))                # 严格区分大小写
num1 = True                              # True = 1
num2 = False                             # False = 0
result1 = num1 + 520
result2 = num2 + 1314
print(result1, result2, sep="&")

"""复数型数据complex：复数"""
付宽博 = 3 + 4j                           # j/J表示虚数单位
print(付宽博, type(付宽博))
print(f"虚部：{付宽博.imag}")
print(f"实部：{付宽博.real}")
z = complex(4,5)
print(z)
