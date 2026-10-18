
# int函数：

"""1.float -> int：只保留整数部分"""
print(int(1.2), end="\t")
print(int(-1.8))
n1 = input("请输入数据：")
print(int(float(n1) + 0.5))    # 正数四舍五入
n2 = input("请输入数据：")
print(int(float(n2) - 0.5))    # 负数四舍五入

"""2.bool -> int：True == 1，False == 0"""
print(int(True), end="\t")
print(int(False))

"""3.str -> int：只能转换纯整数的字符串"""
print(int("4213"), end="\t")
print(int("+4213"), end="\t")
print(int("-4213"))
# print(int("1 + 1"))          # 字符串中有除数字和正负号以外的符号会报错！

# float函数：

"""1.int -> float：小数部分添加 .0 """
print(float(4213), end="\t")
print(float(-4213))

"""2.bool -> float：True == 1.0，False == 0.0"""
print(float(True), end="\t")
print(float(False))

"""3.str -> float：能转换纯数字的字符串"""
print(float("42.13"), end="\t")
print(float("4213"), end="\t")
print(float("-4213"))

# bool函数：

"""1.int/float -> bool：0/0.0转换为False，其他的转换为True"""
print(bool(0), end="\t")
print(bool(0.0), end="\t")
print(bool(4213), end="\t")
print(bool(42.13))

"""2.str/list/tuple/dictionary/set -> bool：空元素转换为False，其他的转换为True"""
print(bool(""), end="\t")
print(bool("Elsa"), end="\t")
print(bool([]), end="\t")
print(bool([1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]), end="\t")
print(bool(()), end="\t")
print(bool((1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7})), end="\t")
print(bool({}), end="\t")
print(bool({1001: 18, True: True, "绰号": "龙颜", ("尊称", "昵称"): ["寒公子", "小鱼儿"], 10101.101: (42, 10),
            "账号信息": {"email": "suntianrui25@mails.ucas.ac.cn", "password": "****************"},
            (1, 2, 3, 4): {"a", "b", "c", "d"}}), end="\t")
print(bool(set()), end="\t")
print(bool({1, 3.14, "Elsa", True, (2, 3)}))

# str函数：int/float/bool/list/tuple/dictionary/set -> str

# eval函数：str -> 运算式/int/float/bool/list/tuple/dictionary/set
print(eval("2 + 3"))
print(eval("3"))

# list函数：转换可迭代对象

"""1.str -> list："""
print(list("Elsa"))
print(list("I feel privileged to love you. I will love you forever."))

"""2.tuple/set -> list："""
print(list((1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7})))
print(list({1, 3.14, "Elsa", True, (2, 3)}))

"""3.dictionary -> list："""
dict1 = {1001: 18, True: True, "绰号": "龙颜", ("尊称", "昵称"): ["寒公子", "小鱼儿"], 10101.101: (42, 10),
         "账号信息": {"email": "suntianrui25@mails.ucas.ac.cn", "password": "****************"},
         (1, 2, 3, 4): {"a", "b", "c", "d"}}
print(list(dict1))
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

"""4.range对象 -> list："""
print(list(range(1, 6)))

# tuple函数：转换可迭代对象

"""1.str -> tuple："""
print(tuple("Elsa"))
print(tuple("I feel privileged to love you. I will love you forever."))

"""2.list/set -> tuple："""
print(tuple([1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]))
print(tuple({1, 3.14, "Elsa", True, (2, 3)}))

"""3.dictionary -> tuple："""
print(tuple(dict1))
print(tuple(dict1.keys()))
print(tuple(dict1.values()))
print(tuple(dict1.items()))

"""4.range对象 -> list："""
print(tuple(range(1, 6)))

# dict函数：

"""1.使用参数："""
print(dict(尊称="寒公子", 昵称="小鱼儿"))

"""2.list -> dictionary："""
print(dict([(1001, 18), (True, True), ('绰号', '龙颜'), (('尊称', '昵称'), ['寒公子', '小鱼儿']), (10101.101, (42, 10)),
            ('账号信息', {'email': 'suntianrui25@mails.ucas.ac.cn', 'password': '****************'}),
            ((1, 2, 3, 4), {'d', 'a', 'b', 'c'})]))

"""3.tuple -> dictionary："""
print(dict(((1001, 18), (True, True), ('绰号', '龙颜'), (('尊称', '昵称'), ['寒公子', '小鱼儿']), (10101.101, (42, 10)),
            ('账号信息', {'email': 'suntianrui25@mails.ucas.ac.cn', 'password': '****************'}),
            ((1, 2, 3, 4), {'d', 'a', 'b', 'c'}))))

"""4.set -> dictionary："""
print(dict({(1001, 18), (True, True), ('绰号', '龙颜'), (10101.101, (42, 10))}))

# set函数：转换可迭代对象

"""1.str -> set："""
print(set("Elsa"))
print(set("I feel privileged to love you. I will love you forever."))

"""2.list/tuple -> set："""
print(set([1, "Elsa", True, (4, 5)]))
print(set((1, 3.14, "Elsa", True, (2, 3))))

"""3.dictionary -> set："""
dict1 = {1001: 18, True: True, "绰号": "龙颜", 10101.101: (42, 10)}
print(set(dict1))
print(set(dict1.keys()))
print(set(dict1.values()))
print(set(dict1.items()))

"""4.range对象 -> list："""
print(set(range(1, 6)))
