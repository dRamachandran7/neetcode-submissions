from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        res = [num for num, count in freqs.most_common(k)]
        
        return res
        