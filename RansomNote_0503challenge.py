class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lengthcnt = 0
        for r in ransomNote:
            for m in magazine:
                if r == m:
                    lengthcnt = lengthcnt + 1
                    magazine = magazine.replace(m, "", 1)   # remove current character in the magazine   
                    break
        
        if lengthcnt == len(ransomNote):
            return True
        else:
            return False
                    

# optimal version
# generate [0]*26 vector and keep count for both ransom note and magazine 
# +1 in magzine and -1 for ransom note
# if negative, return False