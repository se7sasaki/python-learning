with open("sample.txt", "r") as f:
    lines = f.readlines()

print(type(lines))

for i,line in enumerate(lines):
    print(str(i + 1) + "行目:" + line)
    