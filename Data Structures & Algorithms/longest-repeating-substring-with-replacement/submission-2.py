class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_substr = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            if (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            max_substr = max(max_substr, r - l + 1)
        return max_substr




            


        