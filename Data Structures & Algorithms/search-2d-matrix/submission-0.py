class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows-1
        rowFound = -1
        while l<=r:
            mid = (l+r)//2
            if target>=matrix[mid][0] and target<=matrix[mid][cols-1]:
                rowFound = mid
                l=r+1
            elif target< matrix[mid][0]:
                r = mid-1
            else:
                l=mid+1

        if rowFound >= 0:
            l, r = 0, cols-1
            while l<=r:
                mid = (l+r)//2
                if target<matrix[rowFound][mid]:
                    r = mid-1
                elif target>matrix[rowFound][mid]:
                    l = mid+1
                else:
                    return True
        return False
        
        