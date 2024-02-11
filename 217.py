# Problem No. 217: Contains Duplicate
# Difficulty Level: Easy
# Runtime: 417ms
# Memory consumption: 32MB


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # hashset = set()
        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False

        # alternative solution
        # Runtime: 466ms
        # Memory consumption: 28.3MB
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
