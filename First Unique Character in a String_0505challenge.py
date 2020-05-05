# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         a = [0]*26
        
#         for string in s:
#             a[ord(string) - ord('a')] += 1
            
#         for i in range(26):
#             if a[i] == 1:
#                 return i
#             else:
#                 return -1
            
def firstUniqChar(s: str):
    a = [0]*26
        
    for string in s:
        a[ord(string)-ord('a')] += 1
    # print(a)

    index = -1
    k = 0
    for i in s:
        if a[ord(i)-ord('a')] == 1:
            index = k
            break
        k += 1
    return index
       

        
 
test = firstUniqChar("leetcode")
print(test)