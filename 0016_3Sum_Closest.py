class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float("+inf")

        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if abs(sum3 - target) < abs(closest - target):
                    closest = sum3

                if sum3 == target:
                    return sum3
                elif sum3 < target:
                    left += 1
                else:
                    right -= 1

        return closest
