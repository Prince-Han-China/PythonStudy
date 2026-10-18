
# 定义元组：
tup1 = (1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7})    # 元组中的元素可以是数值类型、字符串、列表、元组、字典、集合等
print(tup1, type(tup1))
tup2 = (1)
print(tup2, type(tup2))
tup2 = (1,)                       # 当元组中只有一个元素时，需以“，”结尾
print(tup2, type(tup2))

# 操作元组：

"""1.访问元组元素:tuple[a]，a表示索引
                输出元素"""
print(tup1[1], end="\t")
# print(tup1[7])        # IndexError: list index out of range
print(tup1[-2])
# print(tup1[-8])       # IndexError: list index out of range

"""2.元组切片:tuple[a:b:c]
             其中，a表示起始切片的下标，省略时默认为0（步长为正）/最后一位下标（步长为负）；
                  b表示结束切片的下标，省略时默认为最后一位下标（步长为正）/0（步长为负）；
                  c表示步长，省略时默认为1。
                  输出时，包含起始下标，不包含结束下标
             输出子列表"""
print(tup1[3::])
print(tup1[:5:])
print(tup1[::2])
print(tup1[::-2])
print(tup1[2:5:])
print(tup1[3::2])
print(tup1[5::-2])
print(tup1[:3:2])
print(tup1[:2:-2])
print(tup1[1:6:3])
print(tup1[5:0:-2])
print(tup1[-1:-5:-2])
print(tup1[-5:-1:2])

"""3.遍历元组："""
for i in tup1:
    if i == tup1[-1]:
        print(i)
    else:
        print(i, end="\t")

"""4.查找元素："""

# （1）in 和 not in：
print("Elsa" in tup1, end="\t")
print("Eric" in tup1, end="\t")
print("寒公子" not in tup1)

# （2）index方法：查找元组中元素的位置。
#                tuple.index(查找元素, a, b)
#                其中，a表示开始查找的下标，省略时默认为0；
#                     b表示结束查找的下标，省略时默认为最后一位下标。
#                查找时，包含起始查找的下标，不包含结束查找的下标。
#                输出时，元素存在时，输出元素第一次出现时的首位下标；
#                       元素不存在时，报错！
tup3 = ("Elsa", "小艺", ["畅畅", "嘉嘉", "蒙蒙"], "小艺", "思雨", "歆歆")
print(tup3.index("思雨"), end="\t")
print(tup3.index("小艺", 1), end="\t")
# print(tup3.index("小艺", 2, 3)    # 不包含结束查找的下标
# print(tup3.index("筱雅"))         # ValueError: tuple.index(x): x not in tuple

# （3）count方法：查找元素出现次数。
#                tuple.count(查找的元素)
print(tup3.count("小艺"), end="\t")
print(tup3.count("思雨"), end="\t")
print(tup3.count("筱雅"))
