class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        h1, h2 = {}, {}

        for c in s1:
            h1[c] = h1.get(c, 0) + 1

        l = 0

        for r in range(len(s2)):
            h2[s2[r]] = h2.get(s2[r], 0) + 1

            if h1 == h2:
                return True

            if len(s1) == r - l + 1:
                h2[s2[l]] -= 1

                if h2[s2[l]] == 0:
                    del h2[s2[l]]
                
                l += 1

        return False

# s1="ab"
# s2="lecabee"