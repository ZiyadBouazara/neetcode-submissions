class Solution:
    def isValid(self, s: str) -> bool:
        # s = "()][]{}"
        # if stack and ...
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in brackets:
                # compare top of stack with value of the key -> if match -> pop from stack
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0