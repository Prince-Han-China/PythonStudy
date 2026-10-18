
# 用途：获取容器对象的长度
"""容器对象：列表，元组，字典，集合等"""
str = ("Congratulations! Knowing that you\'ve got the admission to the"
         " Beijing University, I feel absolutely proud of you. "
         "Yours, "
         "Han")
print(len(str), end="\t")
li = [1, "Elsa", True, [2, 3], (4, 5), {"尊称": "寒公子", "昵称": "小鱼儿"}, {6, 7}]
print(len(li), end="\t")
tup = (1, "Elsa", "小艺", ["畅畅", "嘉嘉", "蒙蒙"], "小艺", "思雨", "歆歆")
print(len(tup), end="\t")
dict = {1001: 18, True: True, "绰号": "龙颜", ("尊称", "昵称"): ["寒公子", "小鱼儿"], 10101.101: (42, 10),
        "账号信息": {"email": "suntianrui25@mails.ucas.ac.cn", "password": "****************"},
        (1, 2, 3, 4): {"a", "b", "c", "d"}}
print(len(dict), end="\t")
set = {1, 3.14, "Elsa", True, (2, 3)}
print(len(set))
