class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c.upper() for c in s if c.isalnum())
        return clean_s == clean_s[::-1]
        