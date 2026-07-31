class Solution:
    OPERATORS = {'+', '-', '*', '/'}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in self.OPERATORS:
                arg1 = stack.pop()
                arg2 = stack.pop()

                if token == '+':
                    stack.append(int(arg1 + arg2))
                elif token == '-':
                    stack.append(int(arg2 - arg1))
                elif token == '*':
                    stack.append(int(arg1 * arg2))
                else:
                    stack.append(int(arg2 / arg1))
            else:
                stack.append(int(token))

        return stack[0]    