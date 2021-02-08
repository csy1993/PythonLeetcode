'''
* @File: 1-两数之和.py
* @Author: CSY
* @Date: 2019/7/26 - 14:34
'''
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i] in nums and i != nums.index(target - nums[i])):
                return [i, nums.index(target - nums[i])]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s1 = Solution()
    print(s1.twoSum(nums, target))
