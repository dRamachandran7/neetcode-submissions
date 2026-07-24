from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            t = tuple(sorted(s))
            res[t].append(s)

        return list(res.values())
            



        