class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = defaultdict(int)
        for i,char in enumerate(order):
            hashmap[char]=i
        for j in range(len(words)-1):
            w1,w2 = words[j], words[j+1]
            for k in range(len(w1)):
                if k==len(w2):
                    return False
                if w1[k]!=w2[k]:
                    if hashmap[w1[k]]>hashmap[w2[k]]:
                        return False
                    break
        return True
                    
                


        