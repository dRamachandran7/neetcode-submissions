class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        # calculate prefix products

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])

        # calcualte suffix products, need to be reversed

        for i in range(1, len(nums)):
            suffix.append(nums[len(nums) - i] * suffix[i - 1])
        
        suffix.reverse()

        # build res

        res = []

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res

        

        