class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Can't sort it lol
    
        for i in range(len(nums) - 1, -1, -1):
            difference = target - nums[i]
            if difference in nums:
                return [nums.index(difference), i]
