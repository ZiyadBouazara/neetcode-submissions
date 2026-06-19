class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(n * k log k) where k is length of a word and n the number of strs
        # this solution iterates through the array and sorts each word
        # sorting is O(klogk) and the loop is n
        match_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            match_dict[sorted_word].append(word)
        
        return [value for key, value in match_dict.items()]