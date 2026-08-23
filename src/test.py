list = [2,4,5,71,7,9]
n = 5
pos =-1
def search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            globals()['pos'] = int(i) #Declaring it as global variable
            return True
    return False

if search(list,n):
    print(f"Found at pos {pos}")
else:
    print("Not Found")