class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
    hash = {}
    for i in range(len(nums)):
      if nums[i] in hash:
        return True
      hash[nums[i]] = i
    return False