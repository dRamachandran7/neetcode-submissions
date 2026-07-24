from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        res = []

        for n in freqs.most_common(k):
            res.append(n[0])
        
        return res
        