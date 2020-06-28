# fibonacci implementation
class Solution:
    def fibonacci(self, n):
        if n <= 1:
            return n
        
        first  = 0
        second = 1
        third  = 1

        for n in range(2, n+1):
            third  = first + second
            first  = second
            second = third

        return(third)

test = Solution()
for i in range(10):
    print(test.fibonacci(i))