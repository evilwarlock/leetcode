class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lengthcnt = 0
        for r in ransomNote:
            for m in magazine:
                if r == m:
                    lengthcnt = lengthcnt + 1
                    magazine = magazine.replace(m, "", 1)              
                    break
        
        if lengthcnt == len(ransomNote):
            return True
        else:
            return False
                    