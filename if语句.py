
# 简单if语句：
date = input("请输入日期:")
if date == "9.11":                  # if + 空格 + 条件 + ":"
    print("生日快乐!")

num1 = 5
if num1:
    print(f"{num1}相当于True")       # 在if语句中，非0数字相当于True，执行代码块

num2 = 0
if num2:
    print(f"{num2}相当于False")      # 在if语句中，0相当于False，不执行代码块

phrase1 = "I love you,Elsa."
if phrase1:
    print(f"{phrase1}相当于True")    # 在if语句中，非空语句相当于True，执行代码块

phrase2 = ""
if phrase2:
    print(f"{phrase2}相当于False")   # 在if语句中，空语句相当于False，不执行代码块

# if-else语句：
Elsa = input("请输入您女朋友的资产")
if int(Elsa) > 100000000:
    print("Elsa是女霸总")
else:
    print("Elsa是家庭主妇")

You_love_me = True
if You_love_me:
    print("I love you, too!")
else:
    print("Find your own love.")

"""三元表达式:if-else语句"""
print("I love you,too!") if You_love_me else print("Find your own love.")

# if-elif语句：
weather = input("请输入天气：")
if weather == "scorching":
    print("穿防晒的衣服，建议穿注意涂抹防晒霜")
elif weather == "sunny":
    print("穿清凉的衣服，建议穿短袖和长裤")
elif weather == "windy":
    print("穿挡风的衣服，建议穿长袖和长裤，注意保暖")
elif weather == "rainy":
    print("穿保暖的衣服，建议穿雨衣和雨靴，可以带伞")
elif weather == "snowy":
    print("穿抗冻的衣服，建议穿羽绒服和棉裤")

# if-elif-else语句：
if weather == "scorching":
    print("穿防晒的衣服，建议穿注意涂抹防晒霜")
elif weather == "sunny":
    print("穿清凉的衣服，建议穿短袖和长裤")
elif weather == "windy":
    print("穿挡风的衣服，建议穿长袖和长裤，注意保暖")
elif weather == "rainy":
    print("穿保暖的衣服，建议穿雨衣和雨靴，可以带伞")
elif weather == "snowy":
    print("穿抗冻的衣服，建议穿羽绒服和棉裤")
else:
    print("根据天气情况穿衣")

"""三元表达式:if-elif-else语句"""
Belen = input("请输入您的资产：")
# print("大老板") if int(Belen) > 10000000000 else print("小老板") if 1000000 < int(Belen) < 10000000000 else print("中产阶级")

# if嵌套：
if int(Belen) > 10000000000:
    print("继续合作")
    if int(Elsa) > 100000000:
        print("增加合作条款")
    else:
        print("就这样吧")
else:
    print("终止合作")
