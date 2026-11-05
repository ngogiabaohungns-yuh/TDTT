#Bai 1:
def Bai1():
    n = int(input())
    print(n*2)
    return (n*2)

#Bai 2:
def Bai2():
    a, b = map(float, input().split())
    vuichoi= 3.14* ((a/2)**2)
    S = a*b - vuichoi
    return S

#Bai 3:
def Bai3():
    kitu=input()
    if kitu.islower():
        print(kitu.upper())
    else:
        print(kitu.lower())
    return 0

#Bai 4:
def Bai4():
    c = input()
    if c.isalpha():
        print(f"{c} là kí tự alphabet")
    else:
        print(f"{c} không phải là kí tự alphabet")
    return 0

#Bai 5:
def Bai5():
    chu = input()
    chu = ord(chu)
    chu += 31
    print(chr(chu))
    return 0

#Bai 6:
def Bai6():
    a,b,c = map(float, input().split())
    if a +b>c and a+c>b and b+c>a:
        p= (a +b +c)/2
        area =(p*(p-a)*(p-b)*p-c)**0.5
        return(area)
    else:
        print("Khong phai 3 canh cua tam giac")
        return("Khong phai 3 canh cua tam giac")

#Bai 7:
def Bai7():
    a= input()
    k = 0
    for i in a:
        k += 1
        if k == 5:
            print(i)
        if k == 9:
            print(i)
    return 0

#Bai 8:
def Bai8():
    Ten = input("Ten chu ho: ")
    a = int(input("Chi so thang truoc: "))
    b = int(input("Chi so thang nay: "))
    n = b - a
    money = 0
    if n>0 and n <=50:
        money += n*1984
    elif n>50 and n <=100:
        money += 50*1984 + (n-50)*2050
    elif n >100 and n <=200:
        money += 50*1984 + 50*2050 + (n-100)*2380
    elif n >200 and n<=300:
        money += 50*1984 + 50*2050 + 100*2380 + (n-200)*2998
    elif n >300 and n<=400:
        money += 50*1984 + 50*2050 + 100*2380 + 100*2998 + (n-300)*3350
    else:
        money += 50*1984 + 50*2050 + 100*2380 + 100*2998 + 100*3350 + (n-400)*3460
    print("Ten chu ho: ", Ten)
    print(f"Tien phai tra la: {money*(1.08)}")
    return money*(1.08)


## Bài tập thêm
#1
def Bai1_them():
    x =int(input())
    if x % 2 == 0:
        print("là số chẵn")
    else:
        print("là số lẻ")
    return 0

#2
def Bai2_them():
    x =int(input())
    if x % 5 == 0:
            print(True)
    else:
            print(False)
    return 0

#3
def Bai3_them():
    x=int(input())
    if x %3==0 and x%5==0:
        print(True)
    else:
        print(False)
    return 0

#4
def Bai4_them():
    x = int(input())
    olds= 2026- x
    if olds >= 18:
        print("Du tuoi")
    else:
        print("Chua du tuoi")

#5
def Bai5_them():
    a,b = map(int, input().split())
    if a > b:
        print(a)
    elif a <b:
        print(b)
    else:
        print("a=b")
    return 0

#6
def Bai6_them():
    x = input()
    if x.isalpha():
        print("chữ")
    elif x.isdigit():
        print("số")
    else:
        print("không phải chữ hay số")
    return 0

#7
def Bai7_them():
    x =float(input())
    if x >= 8.0:
        print("Giỏi")
    elif x >=6.5 and x <8.0:
        print("Khá")
    elif x >=5.0 and x <6.5:
        print("Trung bình")
    else:
        print("Yếu")
    return 0

#8
def Bai8_them():
    c = int(input())
    if c %400 ==0 or (c%4==0 and c%100 !=0):
        print("Năm nhuận")
    else:
        print("Năm không nhuận")
    return 0

#9
def Bai9_them():
    so =[0,1,2,3,4,5,6,7,8,9]
    chu = ["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
    x = int(input())
    for i in so:
        if x==i:
            print(chu[i])
    return 0

#10
def Bai10_them():
    x = float(input())
    if x >=4:
        print("Qua môn")
    else:
        print("Thi lại")
    return 0

#11
def Bai11_them():
    x = int(input())
    olds= 2025- x
    if olds >= 18:
        print("Du tuoi")
    else:
        print("Chua du tuoi")
    

