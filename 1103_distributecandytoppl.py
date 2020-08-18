class Solution:
    # def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    # def distributeCandies(self, candies, num_people):
    #     # 1-st row requires 1+2+3+..+n = n(n+1)/2 + 0*n^2,
    #     # 2-nd row requires (n+1)+(n+2)+...+(n+n) = n(n+1)/2 + 1*n^2
    #     # n-th row requires n(n+1)/2 + (turn-1)*n^2

    #     turn, rsd = 1, 0
    #     c, n = candies, num_people
    #     print(n)
    #     print(c)
    #     print(c-n*(n+1)/2)
    #     rsd = c
    #     while rsd > n*(n+1)/2: # more than 1 turn   
    #         turn = turn + 1
    #         print(turn)
    #         rsd  = rsd - n * (n + 1) / 2 - (turn - 1) * n ** 2 # obtain residule candies
    #         print(rsd)
    #     else:
    #         rsd  = c # only 1 turn case
    #         print(rsd)
    #     res_candies = [(turn - 1) * n] * n
    #     print(res_candies)
    #     print("start distribution")
    #     for i in range(n-1):
    #         if rsd == 0:
    #             return res_candies
    #         elif rsd > 2 * i + 1:
    #             print("rsd =", rsd)
    #             rsd = rsd - i - 1
                
    #             res_candies[i] = res_candies[i] + i + 1
    #             print("i =", i)
    #             print(res_candies)
    #             continue
    #         else:
    #             print("flag")
    #             print("rsd =", rsd)
    #             print("i =", i)
    #             res_candies[i] = res_candies[i] + i + 1 
    #             res_candies[i+1] = res_candies[i+1] + (rsd-i-1)
    #             return res_candies
    def distributeCandies(self, candies, num_people): # brutal force
        lo, hi = 0, candies
        K = 0
        while lo <= hi:
            k = (lo + hi)//2
            if k*(num_people*(num_people+1))//2 + (k*(k-1))//2 * num_people**2 <= candies:
                K = k
                lo = k + 1
            else:
                hi = k - 1
        result = [(i+1)*K+num_people*(K*(K-1))//2 for i in range(num_people)]
        candies -= sum(result)
        for i in range(num_people):
            add = min(candies, K * num_people + i + 1)
            result[i] += add
            candies -= add
            if candies == 0:
                break
        return result 





test = Solution()
print(test.distributeCandies(20,4))

