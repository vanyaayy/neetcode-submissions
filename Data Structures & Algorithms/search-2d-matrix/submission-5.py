class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l ,r = 0,rows-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            if target>matrix[mid][cols-1]:
                l = mid+1
            elif target<matrix[mid][0]:
                r = mid-1
            else:
                res = mid
                break
        if res ==-1:
            return False
        l2,r2 = 0,cols-1
        while l2<=r2:
            mid2 = (l2+r2)//2
            if target>matrix[res][mid2]:
                l2 = mid2+1
            elif target<matrix[res][mid2]:
                r2 = mid2-1
            else:
                return True

        return False

            

