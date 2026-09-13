class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in s:
            hashmapS[i]+=1
        for i in t:
            hashmapT[i]+=1
        if hashmapS == hashmapT:
            return True
        else:
            return False


# time : O(n+m) space: O(k) — where k is the number of distinct characters across the inputs. For a fixed lowercase English alphabet, this is O(1) because there are at most 26 possible keys per dictionary. With unrestricted characters, it can be O(n).