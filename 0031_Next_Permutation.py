class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        
        change = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                change = i - 1
                break
        
        swap_index = len(nums) - 1
        while swap_index > change:
            if nums[swap_index] > nums[change]:
                break
            swap_index -= 1

        if swap_index != change:
            nums[change], nums[swap_index] = nums[swap_index], nums[change]
        else:
            nums[change], nums[-1] = nums[-1], nums[change]

        left = change + 1
        right = len(nums) - 1
        while left <= right:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                right -= 1
