class Solution:
    PAIRS = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:

        # approach: keep adding chars to a stack. when a 'closing'
        # bracket is added, check that it matches the last open 
        # bracket, then pop both. if it doesn't match, false

        if (len(s) == 0):
            return False
        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            # check if its a closer
            if char in self.PAIRS:
                # check if it matches the last element
                if len(stack) == 0 or stack[-1] != self.PAIRS[char]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(char)

        # stack should be empty by the end
        return not stack
        