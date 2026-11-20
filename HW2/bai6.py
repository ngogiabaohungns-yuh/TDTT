n = int(input())
lst=list()
for i in range(2, n+1):
    so_lan = 0
    while n %i ==0:
        n = n/i
        so_lan +=1
    if so_lan !=0:
        print(f"{i}^{so_lan}", end=" ")