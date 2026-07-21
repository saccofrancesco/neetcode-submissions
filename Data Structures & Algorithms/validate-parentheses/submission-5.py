class Solution:
    def isValid(self, s: str) -> bool:
        brackets: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack: List[int] = list()
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != brackets[char]:
                return False
        return not stack