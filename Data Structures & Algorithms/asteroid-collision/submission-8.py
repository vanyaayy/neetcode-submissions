class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]
        a =-1
        for i in asteroids:
            a = i
            if i<0:
                while stack and stack[-1]>0:
                    ele = stack.pop()
                    if ele==abs(i):
                        a = 0
                        break
                    elif ele<abs(i):
                        a = i
                    else:
                        a= ele
                        break
                if a!=0:
                    stack.append(a)
            else:
                stack.append(i)
        
        return stack
                    



        