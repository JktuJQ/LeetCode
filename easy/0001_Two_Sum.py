class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = dict()

        for i in range(len(nums)):
            searching = target - nums[i]
            need = found.get(searching)
            if need is not None:
                return [need, i]
            found[nums[i]] = i
