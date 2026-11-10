class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for i, num in enumerate(nums):
            if num in found:
                return True
            found[num] = i
        return False              