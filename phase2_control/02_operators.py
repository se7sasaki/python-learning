age = int(input("年齢:"))

if age >= 18 and age < 65:
    print("労働世代です")

score = int(input("点数:"))

if score >= 60 and score < 90:
    print("合格")

number = int(input("数字:"))

if number != 0:
    print("ゼロじゃない")
else:
    print("ゼロ")


day = input("曜日:")

if day == "土" or day ==  "日":
    print("休日")
else:
    print("平日")