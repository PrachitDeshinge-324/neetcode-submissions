class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for i, val in enumerate(strs):
            t = "".join(sorted(val))
            temp[t].append(val)
        
        return list(temp.values())