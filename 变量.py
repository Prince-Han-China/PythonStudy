
# 直接定义单一变量
寒公子 = 100000000000           # "="前后都有空格
print(寒公子)                   # 寒公子为变量，变量必须先赋值再使用
print("寒公子")                 # "寒公子"为数据

# 将一个变量赋值给另一个变量
小鱼儿 = 寒公子                  # 新变量在前，原变量在后
print(小鱼儿)

# 将运算结果赋值给变量
孙天睿 = 寒公子 + 小鱼儿          # "+"前后都有空格    新变量在前
print(孙天睿)

# 同一变量可以被反复赋值:输出时以上面最近的变量定义为准
Elsa = 10000000
print(Elsa)

Elsa = 100000000
print(Elsa)

Elsa = 1000000000
print(Elsa)

# 变量命名

# 1.遵循标识符规定
# 2.多单词变量命名方式

# (1)下划线分割法：函数、变量
print(Elsa)
environmental_protection_strategy = "新能源+节能"
print(environmental_protection_strategy)
# (2)大驼峰命名法：类
EnvironmentalProtectionStrategy = "新能源+节能"
print(EnvironmentalProtectionStrategy)
# (3)小驼峰命名法：
environmentalProtectionStrategy = "新能源+节能"
print(environmentalProtectionStrategy)
