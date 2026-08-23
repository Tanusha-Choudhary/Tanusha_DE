list1 = [4,3,8,2,1,5,10,6]

def sort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

sort(list1)
print(list1)