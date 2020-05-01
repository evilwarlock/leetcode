# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brutal force version

        # for i in range(n):
        #     if isBadVersion(i+1) == True:
        #         return i+1
        
        # binary search
        
        start = 0
        mid = 0
        end = n
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
        if isBadVersion(mid) == True:
            return mid
        else:
            return end