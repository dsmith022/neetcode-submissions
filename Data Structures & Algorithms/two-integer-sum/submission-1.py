class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxs = [0, 0]
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in nums:
                continue
            else:
                indxs[0] = i
                for n in range(i + 1, len(nums)):
                    if nums[n] == difference:
                        indxs[1] = n
                        return indxs
