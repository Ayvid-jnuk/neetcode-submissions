class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
            }

        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != pairs[bracket]:
                    return False
                stack.pop()
        return len(stack) == 0





        