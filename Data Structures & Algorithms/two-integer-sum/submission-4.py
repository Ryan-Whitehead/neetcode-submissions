class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i,num in enumerate(nums):
            solution = target - num
            if solution in complement:
                return [complement[solution], i]
            complement[num] = i
