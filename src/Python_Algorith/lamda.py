list1=[1,2,3,4,66,5,8,6,9,7]
# 1
def even(a):
    if a %2 == 0:
        return True
    else:
        return False
out1= filter(even,list1)
for i in out1:
    print(i)
    # OR
# 2
out2 = list(filter(lambda a:a%2 ==0,list1)  )
print(out2)