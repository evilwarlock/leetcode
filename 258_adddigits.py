# digital root
class Solution:
    def addDigits(self, num: int) -> int:
        # if num == 0:
        #     return 0
        # elif num % 9 == 0:
        #     return 9
        # else:
        #     return num % 9
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9
