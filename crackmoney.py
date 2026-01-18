class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        result = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            else:
                anagram_map[sorted_word].append(word)
