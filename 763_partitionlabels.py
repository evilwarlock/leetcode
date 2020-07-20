# partitionlabels-763.py
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        first={}
        last={}
        for i in S:
            if i not in first:
                first[i] = S.find(i)
            if i not in last:
                last[i] = S.rfind(i)
        start=S[0]
        cnt=0
        result=[]
        for letter in S:
            if last[letter]<=last[start]:
                start = letter
                cnt+=1
            else:
                if first[letter]<last[start]:
                    start=letter
                    cnt+=1
                else:
                    start=letter
                    result.append(cnt)
                    cnt=1
        result.append(cnt)    
        return result
        