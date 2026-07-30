class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window should be len(s1) size?
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            substring = s2[l:r + 1]
            if sorted(substring) == sorted(s1):
                return True
            l += 1
            r += 1
        
        return False
