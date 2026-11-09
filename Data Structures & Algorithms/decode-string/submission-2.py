class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        cur,s1 ="",""
        res=""
        num=""
        for char in s:
            if char.isdigit():
                num+=char
            elif char=="[":
                stack.append(int(num))
                stack.append("[")
                num = ""
            elif char.isalpha():
                stack.append(char)
            else:
                a = stack.pop()
                cur+=a
                while a!="[":
                    a = stack.pop()
                    if a.isalpha():
                        cur = a+cur
                b = stack.pop()
                cur=cur*b
                stack.append(cur)
                cur=""

        while stack:
            s1 = stack.pop()
            res=s1+res
        return res

                

        