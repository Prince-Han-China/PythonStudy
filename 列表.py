
# 定义列表：
li1 = [1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]    # 列表中的元素可以是数值类型、字符串、列表、元组、字典、集合等
print(li1, type(li1))

# 操作列表：

"""1.访问列表元素:list[a]，a表示索引
                输出元素"""
print(li1[0], end="\t")
print(li1[1], end="\t")
# print(li1[7])                   # IndexError: list index out of range
print(li1[-2])
# print(li1[-8])                  # IndexError: list index out of range

"""2.列表切片:list[a:b:c]
             其中，a表示起始切片的下标，省略时默认为0（步长为正）/最后一位下标（步长为负）；
                  b表示结束切片的下标，省略时默认为最后一位下标（步长为正）/0（步长为负）；
                  c表示步长，省略时默认为1。
                  输出时，包含起始下标，不包含结束下标
             输出子列表"""
print(li1[3::])
print(li1[:5:])
print(li1[::2])
print(li1[::-2])
print(li1[2:5:])
print(li1[3::2])
print(li1[5::-2])
print(li1[:3:2])
print(li1[:2:-2])
print(li1[1:6:3])
print(li1[5:0:-2])
print(li1[-1:-5:-2])
print(li1[-5:-1:2])

"""3.遍历列表："""
for i in li1:
    if i == li1[-1]:
        print(i)
    else:
        print(i, end="\t")

"""4.添加元素："""

# （1）append方法：在末尾添加单个元素
#                 list.append(要添加的元素)
li1.append(8)
print(li1)
li1.append("Elsa & Belen")
print(li1)

# （2）extend方法：在末尾添加多个元素
#                 list.extend(要添加的元素形成的可迭代对象)
"""可迭代对象：字符串，列表，元组，字典，集合……"""
li1.extend("123")
print(li1)
li1.extend([9, 10, 11])
print(li1)

# （3）insert方法：插入单个元素
#                 list.insert(a, 插入的元素)
#                 其中，a表示插入的位置
li1.insert(2, "Belen")
print(li1)
li1.insert(4, False)
print(li1)

"""5.修改元素：list[a] = 新元素"""
li1[7] = {"尊称": "寒公子", "昵称": "小鱼儿", "绰号": "龙颜"}
print(li1)

"""6.查找元素："""

# （1）in 和 not in：
print("Elsa" in li1, end="\t")
print("Eric" in li1, end="\t")
print("寒公子" not in li1)

names = ["傲雪", "寒公子", "雪儿", "小鱼儿"]
while True:
    name = input("请输入你的用户名称：")
    if name in names:
        print(f"昵称{name}已存在，请重新设定。")
    else:
        names.append(name)
        print(f"用户名{name}注册成功，欢迎使用。")
        break

print(names)

# （2）index方法：查找列表中元素的位置。
#                list.index(查找元素, a, b)
#                其中，a表示开始查找的下标，省略时默认为0；
#                     b表示结束查找的下标，省略时默认为最后一位下标。
#                查找时，包含起始查找的下标，不包含结束查找的下标。
#                输出时，元素存在时，输出元素第一次出现时的首位下标；
#                       元素不存在时，报错！
li2 = ["Elsa", "小艺", ["畅畅", "嘉嘉", "蒙蒙"], "小艺", "思雨", "歆歆"]
print(li2.index("思雨"), end="\t")
print(li2.index("小艺", 1), end="\t")
# print(li2.index("小艺", 2, 3)    # 不包含结束查找的下标
# print(li2.index("筱雅"))         # ValueError: list.index(x): x not in list

# （3）count方法：查找元素出现次数。
#                list.count(查找的元素)
print(li2.count("小艺"), end="\t")
print(li2.count("思雨"), end="\t")
print(li2.count("筱雅"))

"""7.删除元素："""

# （1）del方法：del list[a]，a表示索引
del li1[9]
print(li1)
del li1[-1]
print(li1)

# （2）remove方法：list.remove(要删除的元素)
li1.remove("1")
print(li1)
li2.remove("小艺")
print(li2)             # 只删除第一次出现的元素

# （3）clear方法：
li2.clear()
print(li2)

"""8.排序列表中的元素："""

# （1）sort方法：
#               list.sort(函数 = False/True)
#
#
li3 = [7, 9, 8, 5, 1, 2]
li3.sort()
print(li3)
li3.sort(reverse=True)
print(li3)

# （2）reverse方法：将列表内的元素顺序完全对调
li1.reverse()
print(li1)

# 列表推导式：

"""1.[f(i) for i in 可迭代对象]（f(i)为关于i的表达式）："""
li4 = [2**i for i in range(1, 11)]
print(li4)
li4 = []
for i in range(1, 11):
    li4.append(2**i)
print(li4)

li5 = [str(i) for i in li1]
print(li5)
li5 = []
for i in li1:
    li5.append(str(i))
print(li5)

li6 = [[i, i + 1] for i in range(1, 5)]
print(li6)
li6 = []
for i in range(1, 5):
    li6.append([i, i + 1])
print(li6)

"""2.[f(i) for i in 可迭代对象 if语句]："""
li7 = [2**i for i in range(1, 11) if i % 2 == 0]
print(li7)
li7 = []
for i in range(1, 11):
    if i % 2 == 0:
        li7.append(2**i)
print(li7)

"""3.[if语句的三元表达式 for i in 可迭代对象]："""
li8 = [str(i) if i % 2 == 0 else i/2 for i in range(1, 11)]
print(li8)

li9 = [i if i % 2 == 0 else str(i) if i % 3 == 0 else i/2 for i in range(1, 6)]
print(li9)

# 列表嵌套：
li10 = [1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]
print(li10[3], end="\t")
print(li10[3][1])
