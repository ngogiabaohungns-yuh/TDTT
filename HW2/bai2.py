ngay,thang,nam=map(int,input().split())
#INVALID
def cong_ngay(so_ngay:int, ngay:int, thang:int, nam:int):
    if ngay >so_ngay:
        return("INVALID")
    elif ngay ==so_ngay:
        if thang==12:
            ngay =1
            thang =1
            nam +=1
        else:
            ngay=1
            thang +=1
    else:
        ngay +=1

    if ngay < 10 and thang <10:
        return(f"0{ngay}/0{thang}/{nam}")
    elif ngay <10 and thang >10:
        return(f"0{ngay}/{thang}/{nam}")
    elif ngay >10 and thang <10:
        return(f"{ngay}/0{thang}/{nam}")
    else:
        return(f"{ngay}/{thang}/{nam}")

match thang:
    case 1|3|5|7|8|10|12:
        so_ngay=31
        cong_ngay(so_ngay,ngay,thang,nam)
    case 4|6|9|11:
        so_ngay =30
        cong_ngay(so_ngay,ngay,thang,nam)
    case 2:
        if nam%400==0 or (nam%4==0 and nam%100!=0):
            so_ngay=29
            cong_ngay(so_ngay,ngay,thang,nam)
        else:
            so_ngay=28
            cong_ngay(so_ngay,ngay,thang,nam)

print(cong_ngay(so_ngay,ngay,thang,nam))