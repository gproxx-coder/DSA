# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Median of 2 sorted arrays
from typing import List


def get_median_f1(nums1: List[int], nums2: List[int]) -> float:
    len_1 = len(nums1)
    len_2 = len(nums2)
    i, j = 0, 0
    final = []

    while i < len_1 and j < len_2:
        if nums1[i] <= nums2[j]:
            final.append(nums1[i])
            i += 1
        else:
            final.append(nums2[j])
            j += 1

    if i == len_1 and not j == len_2:
        while j < len_2:
            final.append(nums2[j])
            j += 1

    if j == len_2 and not i == len_1:
        while i < len_1:
            final.append(nums1[i])
            i += 1

    new_len = len_1 + len_2
    dv = new_len // 2
    return float(final[dv]) if new_len % 2 != 0 else (final[dv-1] + final[dv])/2


def get_median_f2(nums1: List[int], nums2: List[int]) -> float:
    final = []
    while nums1 or nums2:
        if nums1 and nums2 and nums1[0] <= nums2[0]:
            final.append(nums1.pop(0))
        elif nums1 and not nums2:
            final.append(nums1.pop(0))
        elif nums2 and not nums1:
            final.append(nums2.pop(0))
        else:
            final.append(nums2.pop(0))

    full_len = len(final)
    return float(final[full_len//2]) if full_len % 2 != 0 else (final[(full_len//2)-1] + final[(full_len//2)])/2


nums1 = [1, 3]
nums2 = [2]

# nums1 = [1,2]
# nums2 = [3,4]

print(get_median_f2(nums1, nums2))



