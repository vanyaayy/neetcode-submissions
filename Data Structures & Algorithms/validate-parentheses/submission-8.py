class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i not in hashMap:
                stack.append(i)
            else:
                if stack and hashMap[i]==stack.pop():
                    continue
                else:
                    return False
        return True if stack ==[] else False


        