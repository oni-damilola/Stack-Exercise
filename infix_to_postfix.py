# Question 7

class InfixToPostfix:
    def __init__(self):
        self.infx = ""
        self.pfx = ""

    def getInfix(self, expression):
        self.infx = expression

    def showInfix(self):
        print("Infix Expression:", self.infx)

    def showPostfix(self):
        print("Postfix Expression:", self.pfx)

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 0

    def convertToPostfix(self):
        stack = []
        self.pfx = ""

        for sym in self.infx:
            if sym.isalnum():
                self.pfx += sym
            elif sym == '(':
                stack.append(sym)
            elif sym == ')':
                while stack and stack[-1] != '(':
                    self.pfx += stack.pop()
                stack.pop()  # Discard '(' from stack
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(sym):
                    self.pfx += stack.pop()
                stack.append(sym)

        while stack:
            self.pfx += stack.pop()

# Test expressions
expressions = [
    "A + B - C",
    "(A + B) * C",
    "(A + B) * (C - D)",
    "A + ((B + C) * (E - F) - G) / (H - I)",
    "A + B * (C + D) - E / F * G + H"
]

for expression in expressions:
    infix_to_postfix = InfixToPostfix()
    infix_to_postfix.getInfix(expression.replace(" ", ""))  # Remove spaces for ease of processing
    infix_to_postfix.convertToPostfix()
    infix_to_postfix.showInfix()
    infix_to_postfix.showPostfix()
    print()
