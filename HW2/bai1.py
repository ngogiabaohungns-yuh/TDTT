n=int(input())
if n <=50:
    money = n*1500
elif n <=100:
    money = 50*1500 + (n-50)*2000
else:
    money = 50*1500 +50*2000 +(n-100)*3000
total = (1.05*money)
print(f"{total:.0f}")