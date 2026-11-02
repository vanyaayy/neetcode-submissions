class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l,r = 0, rows-1
                
        def binarysearch(row, t):
            l,r=0, len(row)-1
            while l<=r:
                mid = (l+r)//2
                if target<row[mid]:
                    r = mid -1
                elif target > row[mid]:
                    l=mid+1
                else:
                    return True
            return False

        while l<=r:
            mid = (l+r)//2
            if target>= matrix[mid][0] and target <=matrix[mid][cols-1]:
                return binarysearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        return False



