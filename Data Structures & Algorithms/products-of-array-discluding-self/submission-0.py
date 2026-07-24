import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #trying out brute force solution first

        res = []

        for i, n in enumerate(nums):
            cur = 1
            for j in range(0, i):
                cur *= nums[j]
            for j in range(i+1, len(nums)):
                cur *= nums[j]
            
            res.append(cur)

        return res
        
        