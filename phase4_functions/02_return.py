a = int(input("a:"))
b = int(input("b:"))

def max_num(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "a = b"
result = max_num(a,b)
print(result)

def tax(price):
    tax = price * 1.1
    return tax

ramen = tax(800)
sushi = tax(1500)
total = ramen + sushi
print(total)

def greeting(name):
    return "こんにちは、"+ name +"さん"

name = input("名前:")
print(greeting(name))