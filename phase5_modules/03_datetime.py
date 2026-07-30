from datetime import datetime

now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y年%m月%d日"))

today = datetime(2026, 7, 19)
print(today.strftime("%Y年%m月%d日"))

print(now.strftime("%H時%M分"))

birthday = datetime(2003, 7, 3)
total = datetime.now() - birthday
print(total.days)