'''
* @File: a14_最长公共前缀.py
* @Author: CSY
* @Date: 2019/7/27 - 10:24
'''
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


if __name__ == "__main__":
    # strs=["flower","flow","flight"]
    strs = ["dog", "racecar", "car"]
    s1 = Solution()
    print(s1.longestCommonPrefix(strs))
