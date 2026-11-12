class Solution:
    def simplifyPath(self, path: str) -> str:
        cur =""
        res =""
        stack =[]
        path = path+"/"
        for i in path:
            if i !="/":
                cur+=i
            else:
                if cur!="":
                    if cur =="..":
                        if stack:
                            stack.pop()
                    elif cur ==".":
                        cur=""
                        continue
                    else:
                        stack.append(cur)
                    cur=""
        
        res="/"+"/".join(stack)
        return res

            

        