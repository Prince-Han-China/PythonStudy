
# 字符串类型变量str：

# 1.单行字符串：
寒公子 = '冰雪门掌门'             # 用单引号界定
print(寒公子, type(寒公子))
小鱼儿 = "寒公子"                # 用双引号界定
print(小鱼儿, type(小鱼儿))

# 2.多行字符串：
傲雪 = '''小鱼儿
寒公子
冰雪门掌门'''                    # 用三个单引号界定
print(傲雪, type(傲雪))
雪儿 = """傲雪
小鱼儿
寒公子
冰雪门掌门"""                    # 用三个双引号界定
print(雪儿, type(雪儿))

# 字符串与字节串的编码转换：
str1 = "你是我的真爱！"
str1_bytes = str1.encode("utf_8")
print(str1_bytes, type(str1_bytes))

str2_bytes = b'\xe4\xbd\xa0\xe6\x98\xaf\xe6\x88\x91\xe7\x9a\x84\xe7\x9c\x9f\xe7\x88\xb1\xef\xbc\x81'
str2 = str2_bytes.decode("utf_8")
print(str2, type(str2))

# 字符串运算符：

"""1. + ：相连字符串直接无间隔连接形成一个新的字符串"""
str3 = "Elsa"
str4 = "I love you！"
print(str3 + str4, sep="……")
print(str3, str4, sep="……")

"""2. * : 重复输入字符串，每遍之间无间隔"""
print("Elsa" * 3)

"""3.in & not in"""
str5 = "You're my true love."
print("Elsa" in str5, end="\t")
print("love" in str5, end="\t")
print("Elsa" not in str5, end="\t")
print("love" not in str5)

"""4. [] : 索引"""

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# [a]：a表示下标。
#      a为非负数时，从0开始从左到右排列下标
#      a为负数时，从-1开始从右到左排列下标
print(alphabet[0], end="")        # a
print(alphabet[1], end="")        # b
print(alphabet[2], end="")        # c
print(alphabet[3], end="")        # d
print(alphabet[4], end="")        # e
print(alphabet[5], end="")        # f
print(alphabet[6], end="")        # g
print(alphabet[7], end="")        # h
print(alphabet[8], end="")        # i
print(alphabet[9], end="")        # j
print(alphabet[10], end="")       # k
print(alphabet[11], end="")       # l
print(alphabet[12], end="")       # m
print(alphabet[13], end="")       # n
print(alphabet[14], end="")       # o
print(alphabet[15], end="")       # p
print(alphabet[16], end="")       # q
print(alphabet[17], end="")       # r
print(alphabet[18], end="")       # s
print(alphabet[19], end="")       # t
print(alphabet[20], end="")       # u
print(alphabet[21], end="")       # v
print(alphabet[22], end="")       # w
print(alphabet[23], end="")       # x
print(alphabet[24], end="")       # y
print(alphabet[25], end="")       # z
print(alphabet[26], end="")       # A
print(alphabet[27], end="")       # B
print(alphabet[28], end="")       # C
print(alphabet[29], end="")       # D
print(alphabet[30], end="")       # E
print(alphabet[31], end="")       # F
print(alphabet[32], end="")       # G
print(alphabet[33], end="")       # H
print(alphabet[34], end="")       # I
print(alphabet[35], end="")       # J
print(alphabet[36], end="")       # K
print(alphabet[37], end="")       # L
print(alphabet[38], end="")       # M
print(alphabet[39], end="")       # N
print(alphabet[40], end="")       # O
print(alphabet[41], end="")       # P
print(alphabet[42], end="")       # Q
print(alphabet[43], end="")       # R
print(alphabet[44], end="")       # S
print(alphabet[45], end="")       # T
print(alphabet[46], end="")       # U
print(alphabet[47], end="")       # V
print(alphabet[48], end="")       # W
print(alphabet[49], end="")       # X
print(alphabet[50], end="")       # Y
print(alphabet[51])               # Z

# 切片操作[a:b:c]：a表示起始切片的下标，省略时默认为0（步长为正）/最后一位下标（步长为负）；
#                 b表示结束切片的下标，省略时默认为最后一位下标（步长为正）/0（步长为负）；
#                 c表示步长，省略时默认为1。
#                 输出时，包含起始下标，不包含结束下标
print(alphabet[::])
print(alphabet[10::])
print(alphabet[:20:], end="\t")
print(alphabet[10:20:], end="\t")
print(alphabet[::5])
print(alphabet[10::5], end="\t")
print(alphabet[:20:5], end="\t")
print(alphabet[10:20:5])
print(alphabet[20:10:-1], end="\t")
print(alphabet[-10:-20:-2], end="\t")
print(alphabet[-20:-10:3])

# 与字符串有关的内置函数：

"""1.查找子字符串："""

str6 = "I love you, Elsa! You are my true love! Do you want to be my girlfriend?"
# (1)find方法：查找子字符串位置。
#             "字符串"/字符串对应的变量.find("子字符串"/子字符串对应的变量, a, b)
#             其中，a表示开始查找的下标，省略时默认为0；
#                  b表示结束查找的下标，省略时默认为最后一位下标。
#             查找时，包含起始下查找的下标，不包含结束查找的下标
#             输出时，子字符串存在时，输出子字符串第一次出现时的首位下标；
#                    子字符串不存在时，输出 -1
print(str6.find("i"), end="\t")
print(str6.find("you"), end="\t")
print(str6.find("you", 8), end="\t")
print(str6.find("you", 9, 45), end="\t")
print(str6.find("e", 32), end="\t")
print(str6.find("e", 6, 32), end="\t")
print(str6.find("e", 6, 24))

# (2)index方法：查找子字符串位置。
#             "字符串"/字符串对应的变量.index("子字符串"/子字符串对应的变量, a, b)
#             其中，a表示开始查找的下标，省略时默认为0；
#                  b表示结束查找的下标，省略时默认为最后一位下标。
#             查找时，包含起始查找的下标，不包含结束查找的下标。
#             输出时，子字符串存在时，输出子字符串第一次出现时的首位下标；
#                    子字符串不存在时，报错！
print(str6.index("i"), end="\t")
print(str6.index("you"), end="\t")
print(str6.index("you", 8), end="\t")
print(str6.index("e", 30), end="\t")
print(str6.index("e", 6, 30))

# (3)count方法：查找子字符串数目。
#              "字符串"/字符串对应的变量.count("子字符串"/子字符串对应的变量, a, b)
#              其中，a表示开始查找的下标，省略时默认为0；
#                   b表示结束查找的下标，省略时默认为最后一位下标。
#              查找时，包含起始查找的下标，不包含结束查找的下标
#              输出时，输出子字符串出现次数。
print(str6.count("e"), end="\t")
print(str6.count("e", 6), end="\t")
print(str6.count("e", 6, 32), end="\t")
print(str6.count("you"), end="\t")
print(str6.count("you", 9, 44))

"""2.修改字符串："""

str7 = "I feel privileged to love you. I will love you forever."
# (1)replace方法：进行子字符串的替换。
#                "字符串"/字符串对应的变量.replace("被替换的子字符串"/被替换的子字符串对应的变量, "新的字符串"/新的字符串对应的变量, a)
#                其中，a表示替换的次数。
print(str7.replace("love", "like"))
print(str7.replace("love", "like", 1))

# (2)split方法：分割字符串。
#              "字符串"/字符串对应的变量.split(分隔符, a)
#              其中，分隔符 省略时默认为 空白分隔符 ；
#                   a表示分割次数，省略时默认为 -1，表示不限次数分割。
#              输出时，若所设定的分隔符不存在，则不分割。
print(str7.split())
print(str7.split("."))
print(str7.split(" ", 6))
print(str7.split("@"))

# (3)strip方法：去除字符串中 左右两侧 的某些字符。
#              "字符串" / 字符串对应的变量.strip("去除的字符")
#              其中，"去除的字符"省略时默认为 空格
str8 = "    上海自来水来自海上  "
print(str8.strip())
print(str8.strip("上"))
print(str8.strip("上 "))

# (4)upper方法：将字符串中的小写字母转换为大写字母。
str9 = ("As a representative of our STUDENT UNION, I feel privileged to have "
        "a chance to deliver a speech, which titled \"THE FUTURE OF US\".")
print(str9.upper())

# (4)lower方法：将字符串中的大写字母转换为小写字母。
print(str9.lower())

"""3.检查字符串："""

str10 = ("Congratulations! Knowing that you\'ve got the admission to the"
         " Beijing University, I feel absolutely proud of you. "
         "Yours, "
         "Han")
# (1)startswith方法：检查字符串的前缀。
#                   "字符串" / 字符串对应的变量.startswith("前缀"/前缀字符串对应的变量, a, b)
#                   其中，a表示开始检查的下标，省略时默认为0；
#                        b表示结束检查的下标，省略时默认为最后一位下标。
#                   检查时，包含起始检查的下标，不包含结束检查的下标
#                   输出True/False
print(str10.startswith("Congratulations!"), end="\t")
print(str10.startswith("congratulations!"), end="\t")
print(str10.startswith("Know", 17), end="\t")
print(str10.startswith("Know", 17, 20))

# (2)endswith方法：检查字符串的后缀。
#                  "字符串" / 字符串对应的变量.endswith("后缀"/后缀字符串对应的变量, a, b)
#                  其中，a表示开始检查的下标，省略时默认为0；
#                       b表示结束检查的下标，省略时默认为最后一位下标。
#                  检查时，包含起始检查的下标，不包含结束检查的下标。
#                  输出True/False
print(str10.endswith("Han"), end="\t")
print(str10.endswith("han"), end="\t")
print(str10.endswith("Yours", 1, 119), end="\t")
print(str10.endswith("Yours", 1, 118), end="\t")
print(str10.endswith("Yours", 115, 119), end="\t")
print(str10.endswith("Yours", 1, 120))

# (3)isupper方法：检查字符串中的字母字符是否为全为大写。
#                输出True/False
str11 = "STUDENT UNION 1"
str12 = "I love you, Elsa!"
print(str11.isupper(), end="\t")
print(str12.isupper())

# (3)islower方法：检查字符串中的字母字符是否为全为小写。
#                输出True/False
str13 = "deliver a speech"
str14 = "I love you, Elsa!"
print(str13.islower(), end="\t")
print(str14.islower())
