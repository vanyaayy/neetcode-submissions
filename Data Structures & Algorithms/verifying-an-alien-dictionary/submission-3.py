class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            less = min(len(words[i]), len(words[i+1]))
            c=0
            s1,s2 = words[i], words[i+1]
            for j in range(less):
                if s1[j]!=s2[j]:
                    if orderInd[s1[j]]<orderInd[s2[j]]:
                        break
                    else:
                        return False
                else:
                    c+=1
            if c==len(s2):
                return False
        return True

        