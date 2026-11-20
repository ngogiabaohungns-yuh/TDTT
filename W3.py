def W3A1():
    a = int(input())
    if a <=999 and a>=100:
        c1= a % 10
        c2= (a//10)%10
        c3 =(a//100)
        print(c1,c2,c3, sep="")
    else:
        print("INVALID") 
    return(0)

def W3A2():
    a,b = map(int,input().split())
    c = a^b
    a = c^a
    b = c^b
    print(a,b)
    return (a,b)

def W3A3():
    n = int(input())
    if n & (n-1)==0:
        print("Luy thua cua 2")
    else:
        print("Khong phai luy thua cua 2")
    return (0)

def W3A6():
    x = int(input())
    if x % 2 == 0:
        print(x, "là số chẵn")
    else:
        print(x, "là số lẻ")

    return(0)

def W3A7():
    a,b= map(int,input().spilt())
    if a < 0 and b<0:
        print("Yes")
    else:
        print("No")

def W3A8():
    a = input()
    b = input()
    dai_a=0
    dai_b=0
    for i in a:
        dai_a += 1
    for i in b:
        dai_b +=1

    if dai_a>dai_b:
        print(True)
    else:
        print(False)

    return(0)

def W3A9(a:float, b:float, c:float):
    if a +b>c and a+c>b and b+c>a:
        print("Yes")
        return(True)
    else:
        print("No")
        return(False)

def W3A10():
    a,b,c,d= map(int,input().split())
    lst= [a,b,c,d]
    max = a
    for i in lst:
        if i > max:
            max = i
    print(max)
    return (max)

def W3A11(a:int, b:int, c:int):
    if a +b>c and a+c>b and b+c>a:
        if a==b==c:
            print("Tam giác đều")
        elif a==b or a==c or b==c:
            print("Tam giác cân")
        else:
            print("Tam giác thường")
    else:
        print("Không phải tam giác")
    return(0)

def W3A12(a:float):
    if (a%4==0 and a%100 !=0) or a%400==0:
        print("Yes")
    else:
        print("No")
    return(0)

def W3A14():
    a,b= map(float,input().split())
    if a==0:
        if b==0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print(f"{(-b)/a:.2f}")
    return 0

def W3A15():
    a= float(input())
    if a >= 8.0:
        print("Giỏi")
    elif a>=6.5:
        print("Khá")
    elif a>=5.0:
        print("Trung bình")
    else:
        print("Yếu")
    return 0

def W3A16():
    a = float(input())
    if a >=0:
        songuyen= (a+ 0.5)//1
        pass
    else:
        songuyen= (a-0.5)//1
        pass
    print(songuyen)

def W3A17(a:float, b:float, c:float, d:float):
    q = b/a
    if c == q*b and d == q*c:
        print("cong boi")
    else:
        print("khong phai cong boi")
