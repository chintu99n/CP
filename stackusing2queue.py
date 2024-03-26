class Solution:
    def evaluate_rpn(self, tokens):
        stack = []
        
        for token in tokens:
            if self.is_operator(token):
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.perform_operation(token, operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()

    def is_operator(self, token):
        return token in ["+", "-", "*", "/"]

    def perform_operation(self, operator, operand1, operand2):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            # Integer division in Python 3
            return int(operand1 / operand2)
        else:
            raise ValueError("Invalid operator: " + operator)

if __name__ == "__main__":
    solution = Solution()

    # Input the RPN expression as space-separated tokens
    tokens = input("Enter the RPN expression as space-separated tokens: ").split()

    # Evaluate the RPN expression
    result = solution.evaluate_rpn(tokens)

    # Output the result
    print("Result:", result)
