age = int(input("年齢:"))

if age >= 20:
    print("成人です")
elif age >= 13:
    print("中高生です")
else:
    print("子供です")

score = int(input("点数:"))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")

number = int(input("数字:"))
if number % 2 == 0:
    print("偶数")
else:
    print("奇数")

name = input("名前:")
if not name:
    print("名前を入力してください")