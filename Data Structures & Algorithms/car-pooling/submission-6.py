class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        arr = [0]*1001
        for t in trips:
            arr[t[1]]+=t[0]
            arr[t[2]]-=t[0]
        cur = 0
        for i in range(len(arr)):
            cur+=arr[i]
            if cur>capacity:
                return False
        return True

            

        