# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 0:
            median_index = (l1 + l2) // 2 - 1
            is_len_sum_even = True
        else:
            median_index = (l1 + l2) // 2
            is_len_sum_even = False
        i, j = 0, 0
        result = []
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
        if i == l1:
            result += nums2[j:]
        if j == l2:
            result += nums1[i:]
        if is_len_sum_even:
            return (result[median_index] + result[median_index+1]) / 2
        return result[median_index]


if __name__ == '__main__':
    solution = Solution()
    l1 = [1, 3]
    l2 = [2]
    res = solution.findMedianSortedArrays(l1, l2)
    print(res)