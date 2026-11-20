l1,r1,l2,r2=map(int,input().split())
if l2 >r1:
    print("None")
else:
    n = r1-l2 +1
    start=l2
    stop = r1
    print(start, stop, n)