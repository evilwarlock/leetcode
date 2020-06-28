# find town judge
def findJudge( N: int, trust):
        a = [0] * N
        for i in trust:
            # print(i)
            # print(i[1])
            a[i[1]-1] += 1 
        flag_unique = 0   
        index = 0
        for j in range(N):
            if a[j] == N-1:
                flag_unique += 1
                index = j
        
        if flag_unique == 1:
            return index + 1
        else:
            return -1

test = [[1,2]]
result = findJudge(2,test)
print(result)