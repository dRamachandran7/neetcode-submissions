class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduped = sorted(list(set(nums)))

        if len(deduped) == 0:
            return 0

        if len(deduped) == 1:
            return 1

        cur = 1
        best = 1

        for i in range(1, len(deduped)):
            if (deduped[i] == (deduped[i - 1] + 1)):
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 1
        
        return best

