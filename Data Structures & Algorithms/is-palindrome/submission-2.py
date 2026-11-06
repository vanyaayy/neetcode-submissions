class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r"[^a-zA-z0-9]","", s).lower()
        if st[::-1]==st:
            return True
        else:
            return False

        
        