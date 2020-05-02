# Jewels and Stones


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels_cnt = 0
        
        if J == []:
            return -1
        if S == []:
            return 0
        
        for j in J:
            for s in S:
                if j == s:
                     jewels_cnt =  jewels_cnt + 1
                        
        return jewels_cnt
                    