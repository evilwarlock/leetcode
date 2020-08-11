class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s.isupper():
            return -1
        
        n = len(s)
        sum = 0
        for char in s:
            print(s)
            base = ord(char) - ord('A') + 1
            # print(ord(char))
            # print(base)
            # print(n)
            sum = sum + base * 26 ** (n - 1) 
            print(sum)
            n = n - 1

        return sum

test = Solution()
print(test.titleToNumber('BA'))