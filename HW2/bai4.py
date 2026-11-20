#Taking input
name=[1,2,3]
score=[1,2,3]
absence=[1,2,3]
for i in range(3):
    name[i], score[i], absence[i]= input().split()
    score[i]= int(score[i])
    absence[i]=int(absence[i])
#Sorting
location = 0
for i in range (2):
    if score[i] >=50 and absence[i] >=0:
        if score[i] < score[i+1]:
            location = i + 1
        elif score[i] == score[i+1]:
            if absence[i] > absence[i+1]:
                location = i + 1
            elif absence [i] == absence [i+1]:
                if name[i] > name[i+1]:
                    location = i + 1
if score[location] < 50:
    print("NONE")
else:
    print(name[location])
