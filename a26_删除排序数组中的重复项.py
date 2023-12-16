'''
* @File: a26_删除排序数组中的重复项.py
* @Author: CSY
* @Date: 2019/7/27 - 11:28
'''
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        s=list(set(nums))
        s.sort(key=nums.index)
        nums[:len(s)]=s
        return len(s)
if __name__ == "__main__":
    # nums = [1,1,2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s1 = Solution()
    print(s1.removeDuplicates(nums))