class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        
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
                cur = ""
                while stack[-1]!="[":
                    cur = stack.pop()+cur
                stack.pop()
                k = stack.pop()
                stack.append(cur*k)
        return "".join(stack)

                

        