# 150. 逆波兰表达式求值
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                a,b = stack.pop(),stack.pop()
                stack.append(str(int(eval(b+token+a))))
            else:
                stack.append(token)

        return int(stack[-1])

