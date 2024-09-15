class Solution:
    def binary(nums, x):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            element = nums[middle]
            if element < x:
                left = middle + 1
            else:
                right = middle - 1
        return [left, right]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_bound = Solution.binary(nums, target - 0.5)
        right_bound = Solution.binary(nums, target + 0.5)
        
        if left_bound[0] != right_bound[0]:
            return [left_bound[0], right_bound[1]]
        return [-1, -1]
