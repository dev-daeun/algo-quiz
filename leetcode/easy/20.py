class Solution:
    def isValid(self, s: str) -> bool:
        opened = ('(', '{', '[')

        stack = list()
        for p in s:
            if p in opened:
                stack.append(p)
                continue

            try:
                top = stack[-1]
            except IndexError:
                stack.append(p)
                continue

            if (top == '(' and p == ')') or (top == '{' and p == '}') or (top == '[' and p == ']'):
                stack.pop()
                continue

            stack.append(p)

        return not stack
