#
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         str1=''
#         l_1=len(word1)
#         l_2=len(word2)
#         if l_1 > l_2:
#             for i in range(0,l_2):
#                 str1 = str1+word1[i]+word2[i]
#             str1 = str1+word1[l_2::]
#         else:
#             for i in range(0,l_1):
#                 str1 = str1+word1[i]+word2[i]
#             str1 = str1+word2[l_1::]
#         return str1
# LEETCODE 75
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         def gcp(m,n):
#             if n == 0:
#                 return m
#             return(gcp(n,m%n))
#         if (str1+str2 == str2+str1):
#             gcp_l = gcp(len(str1),len(str2))
#             return str1[:gcp_l]
#         else:
#             return ""


# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         list_n = []
#         for i in candies:
#             if (i + extraCandies) >= max(candies):
#                 list_n.append(True)
#             else:
#                 list_n.append(False)
#         return list_n

#
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowel = set("aeiouAEIOU")
#         st = 0
#         ei = len(s) - 1
#         arr = list(s)
#         while st < ei:
#             if arr[st] not in vowel:
#                 st += 1
#             elif arr[ei] not in vowel:
#                 ei -= 1
#             else:
#                 arr[st], arr[ei] = arr[ei], arr[st]
#                 st += 1
#                 ei -= 1
#         res = "".join(arr)
#         return res

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         str2 = s.split()
#         str3 = ""
#         for i in str2[::-1]:
#             str3 = str3+i+" "
#         return str3.rstrip()
# 0(n^2) Not good apprOACH
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#
#         len_l = len(nums)
#         for i in range(0, len(nums)):
#             pd = 1
#             for j in range(0, len(nums)):
#                 if i == j:
#                     pass
#                 else:
#                     pd = pd * nums[j]
#             answer.append(pd)
#         return answer
# O(1) good approach:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         answer =[1] * n
#         prefix = 1
#         for i in range(n):
#             answer[i] = prefix
#             prefix *= nums[i]
#         suffix = 1
#         for i in range(n-1,-1,-1):
#             answer[i] *= suffix
#             suffix *= nums[i]
#         return answer








