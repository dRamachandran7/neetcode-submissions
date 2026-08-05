import math

class Solution:
    def calcTimeToEatPile(self, piles: List[int], k: int) -> int:
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        valid_speeds = []

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
        
            time = self.calcTimeToEatPile (piles, mid)

            if time <= h:
                valid_speeds.append(mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return min(valid_speeds)
        