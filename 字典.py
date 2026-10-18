
# 定义字典：

"""1.键名的类型：不可变类型。如数值类型、str、tuple等
     值的类型：可以是数值类型、str、列表、元组、字典、集合等"""
dict1 = {1001: 18, True: True, "绰号": "龙颜", ("尊称", "昵称"): ["寒公子", "小鱼儿"], 10101.101: (42, 10),
         "账号信息": {"email": "suntianrui25@mails.ucas.ac.cn", "password": "****************"},
         (1, 2, 3, 4): {"a", "b", "c", "d"}}
print(dict1, type(dict1))

"""2.建不可以重复，值可以重复
     若键名重复，新的值会覆盖旧的值"""
dict2 = {"name": "历冬", "name": "寒公子"}
print(dict2, end="\t")
dict3 = {"姓名": "寒公子", "尊称": "寒公子"}
print(dict3)

"""3.空字典："""
dict4 = {}
print(type(dict4))

# 操作字典：

"""1.查找元素："""

# （1）in 和 not in：查找键名是否存在
print("账号信息" in dict1, end="\t")
print("龙颜" in dict1, end="\t")
print((42, 10) not in dict1)

# （2）键值对：寻找键对应的值。
#            dictionary[key]
print(dict1[("尊称", "昵称")])
# print(dict1[18])                  # KeyError

# （3）get方法：dictionary.get(查找的键名，默认输出值)
#              默认返回值省略时默认为None
print(dict1.get(("尊称", "昵称")), end="\t")
print(dict1.get(18), end="\t")
print(dict1.get(18, 0))

"""2.修改键对应的值：dictionary[已有的key] = 新的值"""
dict1[True] = "正确"
print(dict1)

"""3.添加键值对：dictionary[新的key] = 对应的值"""
dict1["girlfriend"] = "Elsa"
print(dict1)

"""4.删除元素："""

# （1）del方法：del dictionary[已有的key]
del dict1[1001]
print(dict1)

# （2）clear方法：dictionary.clear()
dict2.clear()
print(dict2)

# （3）pop方法：dictionary.pop(key, 默认输出值)
print(dict1.pop(10101.101))
print(dict1)
# print(dict1.pop("sex"))                      # KeyError
print(dict1.pop("sex", "Not found!"))
print(dict1)

"""5.遍历列表："""

# （1）for循环：遍历键
for i in dict1:
    if i == "girlfriend":
        print(i)
    else:
        print(i, end="\t")

# （2）keys方法：dictionary.keys()
#              获取建的视图对象
keys = dict1.keys()
print(keys, type(keys))
for i in keys:
    if i == "girlfriend":
        print(i)
    else:
        print(i, end="\t")

# （3）values方法：dictionary.values()
#                获取值的视图对象
values = dict1.values()
print(values, type(values))
for i in values:
    if i == "Elsa":
        print(i)
    else:
        print(i, end="\t")

# （4）items方法：dictionary.items()
#                获取键值对的视图对象
items = dict1.items()
print(items, type(items))
for i in items:
    if i == (('尊称', '昵称'), ['寒公子', '小鱼儿']) or i == ("girlfriend", "Elsa"):
        print(i)
    else:
        print(i, end="\t")

"""注：keys/values/items方法输出的视图会时时更新"""
dict1["girlfriend"] = "歆歆"
print(keys)
print(values)
print(items)
