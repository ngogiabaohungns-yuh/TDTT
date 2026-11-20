n = int(input())
max = 0
cur = 0
while n>1:
        cur+=1
        if n %2==0:
            n= n/2
        else:
            n = 3*n+1
        if max <n:
            max = n
print(f"{cur} {max:.0f}")
    
    