class Solution:
    def isValid(self, s: str) -> bool:

        # approach: keep adding chars to a stack. when a 'closing'
        # bracket is added, check that it matches the last open 
        # bracket, then pop both. if it doesn't match, false

        if (len(s) == 0) or (len(s) == 1):
            return False

        pairs = {}
        pairs[')'] = '('
        pairs[']'] = '['
        pairs['}'] = '{'

        closers = {']', ')', '}'}

        stack = []

        for char in s:
            # check if its a closer
            if char in pairs:
                # check if it matches the last element
                if len(stack) == 0 or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(char)

        # stack should be empty by the end'
        if len(stack) == 0:
            return True
        return False
        