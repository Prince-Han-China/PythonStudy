
# 定义集合：
"""1.集合中的元素不可变：数值类型、字符串、元组"""
set1 = {1, 3.14, "Elsa", True, (2, 3)}
print(set1, type(set1))

"""2.集合中重复元素不重复输出："""
set2 = {1, 2, 4, 3, 1, 4}
print(set2, type(set2))

"""3.集合中元素输出时无序："""
set3 = {"b", "d", "c", "a"}
print(set3, type(set3))

"""4.集合中True == 1，False == 0："""
set4 = {True, 1, 0, False}
print(set4)
set5 = {1, True, False, 0}
print(set5)

"""5.空集合："""
set6 = set()
print(set6, type(set6))

# 添加元素：

"""1.add方法：添加单个元素
             set.add(添加的元素)"""
set1.add(False)
print(set1)

"""2.update方法：添加多个元素
                set.update(要添加的元素形成的可迭代对象1, 要添加的元素形成的可迭代对象2, ……)"""
set1.update("abc")
print(set1)
set1.update("abc", [4, 5])
print(set1)
set1.update("abc", [4, 5], {"尊称": "寒公子", "昵称": "小鱼儿"})
print(set1)

# 删除元素：

"""1.remove方法：删除已存在的元素"""
set1.remove(1)
print(set1)

"""2.discard方法：删除存在或不存在的元素"""
set1.discard("a")
print(set1)
set1.discard("d")               # 删除不存在的元素时不进行任何操作
print(set1)

# 集合的数学操作：

"""1.交集运算："""

# （1）& ：
print(set1 & set2, end="\t")
print(set1 & set2 & set3)

# （2）intersection方法：
print(set1.intersection(set2), end="\t")
print(set1.intersection(set2, set3), end="\t")
print(set1.intersection(set2).intersection(set3))

"""2.并集运算："""

# （1）| ：
print(set1 | set2)
print(set1 | set2 | set3)

# （2）union方法：
print(set1.union(set2))
print(set1.union(set2, set3))
print(set1.union(set2).union(set3))

# in 和 not in：
print(0 in set1, end="\t")
print("E" in set1)

# 遍历列表：
for i in set1:
    print(i, end="\t")
