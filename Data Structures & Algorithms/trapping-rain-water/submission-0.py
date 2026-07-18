class Solution:
    def trap(self, height: List[int]) -> int:

        # the amount of water that can be held at any index i of the
        # array where i != 0 or len(height) - 1, is min(height[i -1], height[i + 1])
        # - height[i] where the adjacent heights are non zero. 

        l, left_max = 0, height[0]
        r, right_max = len(height) - 1, height[len(height) - 1]
        capacities = []

        while (l < r):
            if height[l] < height[r]:
                #left moves, so calculate capacity at left then move
                capacities.append(min(left_max, right_max) - height[l])
                l += 1
                if height[l] > left_max:
                    left_max = height[l]
            else:
                #right moves
                capacities.append(min(left_max, right_max) - height[r])
                r -= 1
                if height[r] > right_max:
                    right_max = height[r]
        
        return sum(capacities)