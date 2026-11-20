def Bai1():
    a,b = map(float,input().split())
    S= a*b
    C = 2*(a+b)
    print(S,C)

def Bai2():
    r=float(input())
    S= 3.14*(r**2)
    C = 3.14*r*2
    print(S,C)

def Bai3():
    a,b,c=map(float,input().split())
    if a +b>c and a+c>b and b+c>a:
        if a==b==c:
            print("Tam giác đều")
        elif a==b or a==c or b==c:
            print("Tam giác cân")
        else:
            print("Tam giác thường")
        C= a+b+c
        p= C/2
        S=(p*(p-a)*(p-b)*(p-c))**(1/2)
        print(S,C)
    else:
        print("Không phải tam giác")

def Bai4():
    #ax+b=0
    a,b= map(float,input().split())
    if a==0:
        if b==0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print(f"{(-b)/a:.2f}")

def Bai5():
    #ax^2 +bx+c=0
    a,b,c=map(float,input().split())
    if a ==0:
        if b==0:
                if c==0:
                    print("Vô số nghiệm")
                else:
                    print("Vô nghiệm")
        else:
            print(f"{(-c)/b:.2f}")
    else:
        delta= b**2 - 4*a*c
        if delta<0:
            print("Vô nghiệm")
        elif delta ==0:
            print(f"Nghiệm kép: {-b/(2*a)}")
        else:
            print("Có 2 nghiệm")
            print(f"x1={(-b+delta**0.5)/(2*a)}")
            print(f"x1={(-b-delta**0.5)/(2*a)}")
    return 0

def Bai6():
    a,b,c,d=map(float,input().split())
    max = a
    lst=(a,b,c,d)
    for i in lst:
        if max < i:
            max=i
    return max 

def Bai7():
    a,b,c,d=map(float,input().split())
    min = a
    lst=(a,b,c,d)
    for i in lst:
        if min > i:
            min=i
    return min 

def Bai8():
    #ax+by=m
    #cx+dy=n
    a,b,c,d,m,n=map(float,input().split())
    if a*d-b*c==0:
        print("Vô nghiệm")
    elif a==c and b==d and m==n:
        print("Vô số nghiệm")
    else:
        print(f"x={(m*d-n*b)/(a*d-b*c)}")
        print(f"y={(n*a-m*c)/(a*d-b*c)}")

def Bai9():
    x = int(input())
    gio = x//3600
    phut = x%3600//60
    giay = x%60
    print(f"{gio}gio,{phut}phut,{giay}giay")

def Bai10():
    x0,y0,R=map(float,input().split())
    x1,y1=map(float,input().split())
    test= (x1-x0)**2 +(y1-y0)**2
    if test == R**2:
        print("Thuoc duong tron")
    else:
        print("Khong thuoc duong tron")

def Bai11():
    x,y=map(float,input().split())
    if x ==0 and y ==0:
        print("Không xác định")
    else:
        print(x**y)