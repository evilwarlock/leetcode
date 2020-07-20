# reverse word in string-151.py
class Solution:
    def reverseWords(self, s: str) -> str:
        return(" ".join(s.split()[::-1]))