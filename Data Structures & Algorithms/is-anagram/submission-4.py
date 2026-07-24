from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        t_counts = Counter(t)
        bigger = s
        if len(s) < len(t):
            bigger = t

        for char in bigger:
            if s_counts[char] != t_counts[char]:
                return False
        
        return True
        