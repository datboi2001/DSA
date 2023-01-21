class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        :param tokens: list of strings
        :return: integer
        """
        # Main idea: use a stack. If the current token is a number,
        # push it to the stack. If the current token is an operator,
        # pop the last two numbers from the stack, perform the operation
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack.pop()