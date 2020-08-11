class Solution:
    def hIndex(self, citations):
        print(citations)
        if not len(citations):
            return -1
        res = 0
        citations.sort(reverse=True)
        # print(citations)
        if citations[-1] > len(citations):
            return len(citations)
        
        for i in range(1, len(citations) + 1):
            if i > citations[i-1]:
                res = i - 1
                break
        return res


test = Solution()
testcase = [3,0,6,1,5]
print(testcase.sort())
print(test.hIndex(testcase))