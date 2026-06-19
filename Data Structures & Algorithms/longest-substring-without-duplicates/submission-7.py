class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        hashset = set()

        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[i])
            count = max(count, len(hashset))

        return count
        