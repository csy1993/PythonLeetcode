'''
* @File: a35_搜索插入位置.py
* @Author: CSY
* @Date: 2019/7/27 - 15:04
'''
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        sub=0
        for i in range(len(nums)):
            if target > nums[i]:
                if i==len(nums)-1:
                    return sub+1
                sub+=1
            else:
                return sub
if __name__ == "__main__":
    # nums = [1,3,5,6]
    # target = 5
    # nums=[1,3,5,6]
    # target=2
    # nums=[1, 3, 5, 6]
    # target=7
    nums=[1,3,5,6]
    target=0
    s1 = Solution()
    print(s1.searchInsert(nums, target))