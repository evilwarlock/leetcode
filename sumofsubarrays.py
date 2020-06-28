#sumofsubarrays

class solution:
    def sumOfSubArrays(self, tsum):
        lo, hi = 1, 2
        result = []
        # tmp = []
        if tsum < 3:
            return 0

        while(lo < hi):
            curSum = (lo + hi)*(hi - lo + 1)/2
            if curSum == tsum:
                tmp = []
                for i in range(lo, hi +1):
                    tmp.append(i)
                result.append(tmp)
                lo = lo + 1
            elif curSum < tsum:
                hi = hi + 1
            elif curSum > tsum:
                lo = lo + 1
        return result

test = solution()
print(test.sumOfSubArrays(5))
