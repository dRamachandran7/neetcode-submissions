from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        res = 0
        l, r = 0, 0



        while r < len(s):
            counts = Counter(s[l:r + 1])
            top_count = max(counts.values())

            if (((r - l + 1) - top_count) <= k):
                res = max(res, r - l + 1)
                r += 1

            else:
                # move l until window is valid, then break
                valid = False
                while valid == False:
                    counts = Counter(s[l:r + 1])
                    top_count = max(counts.values())

                    if ((r - l + 1) - top_count) <= k:
                        res = max(res, r - l + 1)
                        valid = True
                    else:
                        l += 1
            
        return res
            
            

        