class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB k = 1
        # count = { A:3, B: 2 }
        # maxf = 4
        # res = 5


        # length of substr - maxf = k (number of replacements)

        countmap = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            countmap[s[r]] = countmap.get(s[r], 0) + 1
            maxf = max(maxf, countmap[s[r]])

            while ((r - l + 1) - maxf) > k:
                countmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            
