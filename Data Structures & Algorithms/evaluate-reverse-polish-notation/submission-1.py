class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = list()
        for tkn in tokens:
            if tkn in "+-*/":
                stack.append(math.floor(eval(f"{stack.pop()} {tkn} {stack.pop()}")))
            else:
                stack.append(tkn)
        return stack[0]