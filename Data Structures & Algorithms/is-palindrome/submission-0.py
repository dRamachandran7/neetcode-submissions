class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s.lower() if c.isalnum())

        for i, char in enumerate(cleaned):
            if i == len(cleaned) - i - 1:
                break
            if cleaned[i] != cleaned[len(cleaned) - i - 1]:
                return False
        
        return True
        