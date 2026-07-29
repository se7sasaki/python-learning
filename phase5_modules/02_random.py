import random

print(random.random())
print(random.randint(1,6))
print(random.choice(["A","B","C"]))

cards = [1,2,3,4,5]
random.shuffle(cards)
print(cards)

for i in range(3):
    print(random.randint(1,6))

things = ["rock", "scissors", "paper"]
print(random.choice(things))

computer = random.randint(1,100)
while True:
    player = int(input("number:"))
    if player > computer:
        print("もっと小さい")
    elif player < computer:
        print("もっと大きい")
    else:
        print("正解")
        break