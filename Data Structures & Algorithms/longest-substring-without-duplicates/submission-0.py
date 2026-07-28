class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # should keep track of chars that have been seen in the 
        # window so far

        seen = set()
        
        max_streak = 1

        l = 0
        r = 1

        seen.add(s[l])

        while r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    l += 1
                    seen.remove(s[l - 1])
            else:
                seen.add(s[r])
                r += 1
                max_streak = max(max_streak, r - l)


    
        return max_streak


        