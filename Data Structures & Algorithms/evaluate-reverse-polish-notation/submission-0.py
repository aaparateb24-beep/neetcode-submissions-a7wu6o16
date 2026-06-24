class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:

            # Addition
            if token == "+":
                b = stack.pop()
                a = stack.pop()

                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()

                stack.append(a - b) 

            elif token == "*":
                b = stack.pop()
                a = stack.pop()

                stack.append(a * b)     
            elif token == "/":
                b = stack.pop()
                a = stack.pop()

                stack.append(int(a / b))
            else:

                # Number found
                stack.append(int(token))
        return stack[0]     