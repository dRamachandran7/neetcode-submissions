class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in complements:
                smaller = i
                bigger = complements[complement]
                if complements[complement] < smaller: 
                    smaller = complements[complement]
                    bigger = i
                return [smaller, bigger]
            complements[n] = i
        
        return [0,0]

        