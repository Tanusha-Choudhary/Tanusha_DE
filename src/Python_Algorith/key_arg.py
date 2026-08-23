# list1=[20,1,3,4,5,6,7]
# def count_n(l):
#     even = 0
#     odd = 0
#     for i in l:
#         if  i%2 == 0:
#             even += i
#         else:
#             odd += i
#     return even,odd
#
# even,odd = count_n(list1)
# print(even)
# print(odd)
# FEBONNACI SERIES

# list = [0,1]
# n =  input("Type a number")
# n = int(n)
# if n ==0 or n == 1:
#     print(1)
# else:
#     for i in range(2,n+1):
#         next_n = list.append(list[i-2]+list[i-1])
# print(list)

#
# def fab(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return 0
#     else:
#         for i in range(2,n+1):
#             c= a+b
#             a = b
#             b = c
#             print(c)
# n = int(input("Your number"))
# fab(n)
# def fact(n):
#     f = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(n,1,-1):
#             f=f*i
#     print(f)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# fact(5)
# print(factorial(5))
# import sys
# print(sys.getrecursionlimit())

# y=0
# def greet():
#     global y
#     y+=1
#     print("Hello",y)
#     greet()
# greet()

# y = map(lambda x:x*x,[1,2,3,3])
# for i in y:
#     print(i)
# # or
# f = (lambda a,b:a+b)
# print(f(5,6))
for i in range(2):
    for j in range(5):
        print([i + j])
    print("Bye")