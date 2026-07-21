person = {"name": "Sena","age":23}
print(person["name"])

for key,value in person.items():
    print(f"{key}:{value}")

person["name"] = "Sena"
person["age"] = 23
person["place"] = "Kanagawa"
person["hobby"] = "baseball"
print(person.values())

person["email"] = "sena@gmail.com"
del person["age"]

for key , value in person.items():
    print(f"{key}:{value}")