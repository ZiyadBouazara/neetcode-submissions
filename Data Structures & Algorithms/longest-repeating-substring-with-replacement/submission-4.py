class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABBB k = 2
        # AAABABB
        # count = { A:1, B: 3}

        # length of substr - maxf = k (number of replacements)

        res = 1

        for i in range(len(s)):
            countmap, maxf = {s[i]: 1}, 0
            for j in range(i+1, len(s)):
                countmap[s[j]] = countmap.get(s[j], 0) + 1
                maxf = max(maxf, countmap[s[j]])

                curr_k = ((j - i) + 1) - maxf
                if curr_k <= k:
                    res = max(res, (j - i) + 1)

        return res
