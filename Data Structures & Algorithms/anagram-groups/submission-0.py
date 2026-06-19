class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use sorting for comparison
        # dict of sorted_word: [corresponding_words]
        # return a list of the values of the dict
        match_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in match_dict:
                match_dict[sorted_word].append(word)
            else:
                match_dict[sorted_word] = [word]
        
        return [value for key, value in match_dict.items()]