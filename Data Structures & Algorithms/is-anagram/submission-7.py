class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for letter in s:
            s_count[letter] = 1 + s_count.get(letter, 0)
        for letter in t:
            t_count[letter] = 1 + t_count.get(letter, 0)

        return s_count == t_count