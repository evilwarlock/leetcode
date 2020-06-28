#jumpladder
# n ladders, can jump 1 or 2 at a time, what's the total number of solutions
# assumpe f(n) =  # of total solution of n steps.
# at step 1, f(n) = f(n-1) + f(n-2), i.e., either jump 1 which which leads to f(n-1) or jump 2 which leads to f(n-2)

class solution:
    def jumpladder(self, number):
        if number <= 0:
            return 0
        elif number < 3:
            return number
        
        first  = 1
        second = 2
        third  = 3

        for i in range(3, number):
            third  = first + second
            second = third
            first  = second

        return third

test = solution()
result = test.jumpladder(10)
print(result)