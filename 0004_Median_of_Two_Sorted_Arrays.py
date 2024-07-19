class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            left1 = nums1[cut1 - 1] if cut1 - 1 >= 0 else -math.inf
            right1 = nums1[cut1] if cut1 < m else math.inf

            left2 = nums2[cut2 - 1] if cut2 - 1 >= 0 else -math.inf
            right2 = nums2[cut2] if cut2 < n else math.inf
            
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            
            if left2 > right1:
                left = cut1 + 1
            else:
                right = cut1 - 1
