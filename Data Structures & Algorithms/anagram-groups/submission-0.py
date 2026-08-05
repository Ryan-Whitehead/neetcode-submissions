class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i, word in enumerate(strs):
            wordSorted = "".join(sorted(word))
            if wordSorted in anagrams:
                anagrams[wordSorted].append(word)
            else:
                anagrams[wordSorted] = [word]

        return list(anagrams.values())    