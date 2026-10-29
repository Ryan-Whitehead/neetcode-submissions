class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original = []

        for num in nums:
            if num not in original:
                original.append(num)
            elif num in original: 
                return True

        return False