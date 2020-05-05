class Solution:
    def findComplement(self, num: int) -> int:
        tar = 1
        if(num == 0):
            return 1
        while(tar - 1 < num):
            tar = tar * 2
        return tar - num - 1