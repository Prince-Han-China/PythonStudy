
# 可变类型变量：

li1 = [1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]

"""1.列表list："""
print(li1, end="\t")
print(f"修改前的地址：{id(li1)}")
li1.append(8)
print(li1, end="\t")
print(f"修改后的地址：{id(li1)}")

"""2.字典dict："""
print(li1[5], end="\t")
print(f"修改前的地址：{id(li1[5])}")
li1[5]["绰号"] = "龙颜"
print(li1[5], end="\t")
print(f"修改后的地址：{id(li1[5])}")

"""3.集合set："""
print(li1[6], end="\t")
print(f"修改前的地址：{id(li1[6])}")
li1[6].add(9)
print(li1[6], end="\t")
print(f"修改后的地址：{id(li1[6])}")

"""可变类型变量操作前后地址不变"""

# 不可变类型变量：

"""1.数值类型：int，float，bool，complex"""
n1 = 10
print(n1, end="\t")
print(f"修改前的地址：{id(n1)}")
n1 += 5
print(n1, end="\t")
print(f"修改后的地址：{id(n1)}")
n2 = 3.14
print(n2, end="\t")
print(f"修改前的地址：{id(n2)}")
n2 -= 0.14
print(n2, end="\t")
print(f"修改后的地址：{id(n2)}")
n3 = True
print(n3, end="\t")
print(f"修改前的地址：{id(n3)}")
n3 = not n3
print(n3, end="\t")
print(f"修改后的地址：{id(n3)}")
n4 = 3 + 4j
print(n4, end="\t")
print(f"修改前的地址：{id(n4)}")
n4 += 5j
print(n4, end="\t")
print(f"修改后的地址：{id(n4)}")

"""2.字符串str："""
str1 = "I feel privileged to love you. I will love you forever."
print(str1, end="\t")
print(f"修改前的地址：{id(str1)}")
str2 = str1.replace("love", "like")
print(str2, end="\t")
print(f"修改后的地址：{id(str2)}")

"""3.元组tuple"""

"""不可变类型变量操作前后地址改变"""


"""注：直接更改变量(可变类型变量或不可变类型变量)地址会发生改变"""
print(li1, end="\t")
print(f"修改前的地址：{id(li1)}")
li1 = [2, 3]
print(li1, end="\t")
print(f"修改后的地址：{id(li1)}")
