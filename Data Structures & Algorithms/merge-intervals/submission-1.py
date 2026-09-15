class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for s,e in intervals:
            last = result[-1][1]
            if s <= last:
                result[-1][1] = max(e,last)
            else:
                result.append([s,e])
        return result