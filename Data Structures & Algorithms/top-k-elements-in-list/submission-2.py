class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = {}
        for num in nums:
            if num in nums_frequency:
                nums_frequency[num] += 1
            else:
                nums_frequency[num] = 1
        return heapq.nlargest(k, nums_frequency, key=nums_frequency.get)     
       
            