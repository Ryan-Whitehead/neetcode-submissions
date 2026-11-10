class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        #compare the sorted version with the 
        for word in strs:
            key = ''.join(sorted(word))
            if key in grouped:
                grouped[key].append(word)
            else: 
                grouped[key] = [word]
        return list(grouped.values())        