#1237. Find Positive Integer Solution for a Given Equation
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        start = 0
        end = z
        while start <= z and end >= 1: # 2 pointer search
            if customfunction.f(start, end) == z:
                result.append((1, end))
                start = start + 1
                end = end -1
            elif customfunction.f(start, end) < z:
                start = start + 1
            else:
                end = end - 1
        return result