list1 = [3,4,5,6]
def list_funct(a):
    for i in a:
        list1.append(i)
    return list1
x = list_funct([3,6])
# print(x)
list2 = [4,7,7,0]
def number(a):
    # list2.append(a)
    num =list2 +[a]
    return num
def alphanum(a):
    # list2.append(a)
    alph =list2+[a]
    return alph
b = alphanum("tani")
print(b)
c=alphanum(100)
print(c)
