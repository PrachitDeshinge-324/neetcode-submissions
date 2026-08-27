class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i:i[0])
        output = [intervals[0]]
        for s,e in intervals[1:]:
            last = output[-1][1]
            if s <= last:
                output[-1][1] = max(e, last)
            else:
                output.append([s,e])
        # print(output)
        return output