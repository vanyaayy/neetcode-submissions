class Solution:
    def validPalindrome(self, s: str) -> bool:
        reverse = s[::-1]
        if s==reverse:
            return True
        for i in range(len(s)):
            newstr = s[:i]+s[i+1:]
            rev = newstr[::-1]
            if newstr == rev:
                return True
    
        return False
        