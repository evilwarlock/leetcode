# mergeSort

class Solution():
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            l = self.sortArray(nums[:len(nums)//2])
            r = self.sortArray(nums[len(nums)//2:])

            output = []
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    output.append(l[i])
                    i = i + 1
                else:
                    output.append(r[j])
                    j = j + 1
            
            if i < len(l):
                output = output + l[i:]
            elif j < len(r):
                output = output + r[j:]
        return output

test = Solution()
array = [10,7,8,9,1,5]
print(test.sortArray(array))