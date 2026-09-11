
"""*args"""
print("寒公子")                         # 输出1个值
print('寒公子')                         # 可用单引号
print("寒公子", 'Elsa')                 # 输出2个值(*args之间用"逗号+空格"隔开）
print("寒公子", "Elsa", "小鱼儿")        # 输出3个值

"""seg=" "   设置分隔符"""
print("寒公子", "Elsa", "小鱼儿")             # 未设置seg参数，默认"空格"隔开
print("寒公子", "Elsa", "小鱼儿", sep=",")    # 设置了seg参数，采用所设置的分隔符隔开
print("寒公子", "Elsa", "小鱼儿", sep="/")

"""end=" "     设置结尾符"""
print("寒公子")
print("Elsa", "小鱼儿")                 # 未设置end参数，默认"/n"结尾
print("寒公子", end=" ")                # 设置end参数，采用所设置的结尾符结尾
print("Elsa", "小鱼儿")
