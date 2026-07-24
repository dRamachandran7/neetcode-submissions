class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for x in nums:
            if x not in seen:
                seen.append(x)
            else:
                return True
        return False

        