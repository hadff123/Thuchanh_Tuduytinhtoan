sec = float(input())
hour=sec//3600
min=(sec%3600)//60
giay=sec%60
print(f"{hour} gio, {min} phut, {giay} giay")