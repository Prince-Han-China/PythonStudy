
"""制表符：\t          充当空格，与前面的字符串构成“四位”的整数倍"""
print("Elsa")
print("\tElsa")
print("\t\tElsa")
print("0\t|")
print("00\t|")
print("000\t|")
print("0000\t|")
print("00000\t|")

"""换行符：\n"""
print("第一行\n第二行\n第三行")

# 反斜杠符号：\\          取消 \ 的转义作用，输出位“一个 \ ”
print("D:\tools\abc")
print("D:\\tools\\abc")

print('I said,"I love you, Elsa."')      # 输出语句内包含双引号，外边使用单引号界定
print("You're my true love.")           # 输出语句内包含单引号，外边使用双引号界定
# 转义引号：\'和\"          转义语句中的 ' 和 " ，用于既有 " 又有 " 的语句
print("I said,\"I love you, Elsa.You\'re my true love.\"")

"""原生字符串：r" "           取消转义"""
print(r"D:\tools\abc")
