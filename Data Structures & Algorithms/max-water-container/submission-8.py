class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Width of container is j - i where i, j are the indices of
        # the bar. height is min(i,j). If we use standard two pointer
        # approach, width is already maximized.

        l, r = 0, len(heights) - 1
        res = 0

        while (l < r):
            smaller = heights[l] if heights[l] < heights[r] else heights[r]
            p = smaller * (r - l)

            if p > res:
                res = p
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res





        