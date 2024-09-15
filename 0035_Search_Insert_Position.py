class Solution:
    def binary(nums, x):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < x:
                left = middle + 1
            else:
                right = middle - 1
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return Solution.binary(nums, target)
