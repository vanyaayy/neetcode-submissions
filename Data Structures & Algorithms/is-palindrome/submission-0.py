class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        newstr = ""
        for i in st:
            newstr=i+newstr
        if newstr == st:
            return True
        else:
            return False

        