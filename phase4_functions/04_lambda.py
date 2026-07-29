def square(x):
    return x ** 2

square = lambda x: x ** 2

print(square(5))

total = lambda a,b:a + b

print(total(2,5))

name = input("Your name:")
greed = lambda name :name + "さんこんにちは"
print(greed(name))

numbers = [5,2,8,1,9,3]
numbers.sort(key=lambda x: x, reverse=True)
print(numbers)