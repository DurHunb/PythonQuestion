class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    # 给定一个只包括'('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
    # 输入: "()[]{}"
    # 输出: true