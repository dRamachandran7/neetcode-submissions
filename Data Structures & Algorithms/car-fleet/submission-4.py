class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip pos and speed together, then sort, then find times
        # as a stack

        pos_speed = sorted(list(zip(position, speed)), reverse = True)

        # calculate times

        stack = []

        for p, s in pos_speed:
            time = (target - p) / s

            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
    