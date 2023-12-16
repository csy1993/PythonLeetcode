'''
* @File: g_整数反转.py
* @Author: CSY
* @Date: 2019/7/27 - 9:45
'''
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0


if __name__ == "__main__":
    # x = 123
    # x=-123
    x = 120
    s1 = Solution()
    print(s1.reverse(x))
