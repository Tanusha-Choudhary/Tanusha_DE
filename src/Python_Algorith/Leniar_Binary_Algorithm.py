list1 = [2,3,4,5,6,7,8,9]
target = 11
def linear_search(list1, target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i
    return -1
def binary_search(list1, target):
    left =0
    right = len(list1)-1
    while left <= right:
        mid = (left+right)//2
        if list1[mid] == target:
            return mid
        elif list1[mid] < target:
            left = mid+1
        elif list1[mid] > target:
            right = mid-1
    return -1
num1 = linear_search(list1, target)
num2 = binary_search(list1, target)
print(f"Position of Linear Search number is at {num1}")
print(f"Position of Binary Search number is at {num2}")