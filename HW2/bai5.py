n = int(input())
chu_so = list()
m = n
so = 0
count=0
sum=0
while m > 1:
    m = m/10
    so +=1
for i in range(so):
    chu_so.append((n//(10**i))%10)
    match chu_so[i]:
        case 2|3|5|7:
            count +=1
            sum += chu_so[i]
print(count, end=" ")
print(sum, end=" ")
for k in range (so):
    if chu_so[0]==0:
        if k+1 < so:
            print(chu_so[k+1], end="")
    else:
        print(chu_so[k], end="")

