class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop() + stack.pop())
            elif ele == "*":
                stack.append(stack.pop() * stack.pop())
            elif ele == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            elif ele == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(ele))

        return stack[0]
        