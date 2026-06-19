class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            substr = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] in substr:
                    break
                else:
                    substr.add(s[j])
            count = max(count, len(substr))

        return count

        