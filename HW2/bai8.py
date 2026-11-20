a,b = map(int,input().split())
so_uoc_max=0
location=0
for i in range(a, b+1):
    so_uoc=0
    for k in range (1, i+1):
        if i % k == 0:
            so_uoc +=1
    if so_uoc > so_uoc_max:
        so_uoc_max = so_uoc
        location= i
print(location, so_uoc_max)