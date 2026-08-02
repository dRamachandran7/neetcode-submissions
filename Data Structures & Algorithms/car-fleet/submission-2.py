class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip pos and speed together, then sort, then find times
        # as a stack

        pos_speed = sorted(list(zip(position, speed)))

        # calculate times

        times = []

        for pos in pos_speed:
            times.append((target - pos[0]) / float(pos[1]))

        fleets = 1

        while len(times) > 1:
            if (times[-2] > times [-1]):
                fleets += 1
                times.pop()
            else:
                times[-2] = times[-1]
                times.pop()
        
        return fleets