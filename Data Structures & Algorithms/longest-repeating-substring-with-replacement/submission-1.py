class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {} # O(26) lookup since alphabet
        l, r = 0, 0
        max_substr = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            
            if ((r - l + 1) - max(hashmap.values())) > k:
                hashmap[s[l]] -= 1
                l += 1

            max_substr = max(r - l + 1, max_substr)
        return max_substr



            


        