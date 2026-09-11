
# 作用：命名

# 规定：

"""1.只能由“数字、字母、下划线（_）”组成"""

"""2.标识符外可加()"""
(Elsa) = "Love"
print(Elsa, end="\t")
print((Elsa))

"""3.不能以数字开头，可以以“字母/下划线”开头"""

"""4.不能是关键字"""
import keyword
print(keyword.kwlist)

"""5.严格区分大小写"""
name = "小鱼儿"
Name = "寒公子"
print(name, end="\t")
print(Name)
