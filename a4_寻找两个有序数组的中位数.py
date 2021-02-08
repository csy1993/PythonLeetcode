'''
* @File: a4_寻找两个有序数组的中位数.py
* @Author: CSY
* @Date: 2019/7/28 - 8:59
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return sum(nums1[len(nums1)//2 - 1:len(nums1)//2 + 1:]) / 2
        else:
            return nums1[(len(nums1) - 1)//2]
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    s1 = Solution()
    print(s1.findMedianSortedArrays(nums1, nums2))