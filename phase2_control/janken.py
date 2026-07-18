import random

user = input("あなたが出すのは:")

computer = random.choice(["グー","チョキ","パー"])
print(f"あなた:{user} コンピュータ:{computer}")

if user == computer:
    print("あいこ")

elif (computer == "グー" and user == "パー") or (computer == "チョキ" and user == "グー") or (computer == "パー" and user == "チョキ"):
    print("あなたの勝ち")

else:
    print("あなたの負け")