'''
* @File: a18_有效的括号.py
* @Author: CSY
* @Date: 2019/7/27 - 11:23
'''
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
if __name__ == "__main__":
    # s="()"
    # s="()[]{}"
    # s="(]"
    # s="([)]"
    s="{[]}"
    s1 = Solution()
    print(s1.isValid(s))