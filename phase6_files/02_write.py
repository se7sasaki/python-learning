with open ("text.txt","a") as f:
    f.write("AAA\n")

with open("text.txt","a") as f:
    f.write("BBB\n")

with open("text.txt", "r") as f:
    print(f.read())