'''
* @File: a27_移除元素.py
* @Author: CSY
* @Date: 2019/7/27 - 11:33
'''
"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    # nums = [3, 2, 2, 3]
    # val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 1
    s1 = Solution()
    print(s1.removeElement(nums, val))
