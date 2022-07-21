class Solution:
    def isValid(self, s: str) -> bool:
        stack_s = []

        for i in s:
            if i == "(":
                stack_s.append("(")
            elif i == "{":
                stack_s.append("{")
            elif i == "[":
                stack_s.append("[")
            elif i == ")":
                if len(stack_s) == 0 or stack_s.pop() != "(":
                    return False
            elif i == "}":
                if len(stack_s) == 0 or stack_s.pop() != "{":
                    return False
            elif i == "]":
                if len(stack_s) == 0 or stack_s.pop() != "[":
                    return False
        if len(stack_s) == 0:
            return True