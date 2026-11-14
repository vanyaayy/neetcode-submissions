class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res =[]
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif start<=intervals[i][1]:
                newInterval = [min(start, intervals[i][0]), max(end, intervals[i][1])]
                start, end = newInterval
                # print(newInterval)
            else:
                res.append(intervals[i])
        res.append(newInterval)

        return res


        