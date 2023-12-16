'''
* @File: a27_实现strStr().py
* @Author: CSY
* @Date: 2019/7/27 - 14:59
'''
"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    # haystack = "hello"
    # needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    s1 = Solution()
    print(s1.strStr(haystack, needle))
