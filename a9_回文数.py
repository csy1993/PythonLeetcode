'''
* @File: a9_回文数.py
* @Author: CSY
* @Date: 2019/7/27 - 10:03
'''
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    # x = 121
    # x=-121
    x = 10
    s1 = Solution()
    print(s1.isPalindrome(x))
