class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = (len(s) - 1)

        while start < end:
            if not (self.isAlnum(s[start])):
                start += 1
                continue
            elif not (self.isAlnum(s[end])):
                end -= 1
                continue
            
            elif s[start].upper() != s[end].upper():
                return False
            
            start += 1
            end -= 1
        
        return True

    def isAlnum(self, char: str) -> bool:
        return (
            (ord(char) >= ord("0") and ord(char) <= ord("9")) or
            (ord(char) >= ord("a") and ord(char) <= ord("z")) or
            (ord(char) >= ord("A") and ord(char) <= ord("Z"))
        )



        