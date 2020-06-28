# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#        if len(coordinates) == 2:
#            return True

def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    # print(len(coordinates))
    P = 0
    for cords in coordinates:
        # print(cords[1]-coordinates[0][1])
        # colinear P = 0 if (x2-x1)(y3-y1)-(y2-y1)(x3-x1) = 0
        P += (coordinates[1][0] - coordinates[0][0])*(cords[1]-coordinates[0][1]) - (coordinates[1][1]-coordinates[0][1])*(cords[0]-coordinates[0][0])
        # print(P)
    if P == 0:
        return True
    else:
        return False


a =  [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result_a = checkStraightLine(a)
print(result_a)

b = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
result_b = checkStraightLine(b)
print(result_b)