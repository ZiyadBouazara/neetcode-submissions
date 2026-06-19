class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for each in s
        # if letter in t -> delete letter from t, else return false
        # return true
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in t:
                t = t.replace(letter, '', 1)
            else:
                return False
        
        return True