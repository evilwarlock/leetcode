# minimumABCB.py
counter = 0
for A in range(10):
    # print(A)
    # print(A)
    for B in range(10):
        # if B == A:
        #     continue
        # print(str(A)+str(B))
        for C in range(10):
            # if C == B or C == A:
            #     continue

            for D in range(10):
                if D == C or B == C or D == B or D == A or C == A or A == B:
                    continue
                # print(str(A)+str(B)+str(C)+str(D))
                counter = counter + 1
                # if A == 1 and B == 2 and C == 7 and D == 6:
                    # print((A*10+B)*(C*10+D)+(A*10+B)+(C*10+D))
                    # print("yes")
                if ((A*10+B)*(C*10+D)+(A*10+B)+(C*10+D))% 1000 == 0:
                    
                    print(str(A)+str(B)+str(C)+str(D))
                    break
                else:
                    no_answer_flag = 1
        
# if no_answer_flag:
    # print("no answer")
    # print(counter)
