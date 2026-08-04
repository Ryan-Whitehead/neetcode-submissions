class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:   
        # O(n^2) time complexity     
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                