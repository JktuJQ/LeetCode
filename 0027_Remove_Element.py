class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            while nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                if j < i:
                    return i
            i += 1
        return j + 1
