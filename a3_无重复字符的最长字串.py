'''
* @File: a3_无重复字符的最长字串.py
* @Author: CSY
* @Date: 2019/7/27 - 17:10
'''
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        res = []
        for x in s:
            if x not in l:
                l.append(x)
            else:
                res.append(len(l))
                i = l.index(x)
                l = l[i + 1:]
                l.append(x)
        res.append(len(l))
        return max(res) if res else 0
if __name__ == "__main__":
    # str="abcabcbb"
    # str="bbbbb"
    str="pwwkew"
    s1 = Solution()
    print(s1.lengthOfLongestSubstring(str))