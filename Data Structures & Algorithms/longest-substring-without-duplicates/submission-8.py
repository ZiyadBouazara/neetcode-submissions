class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # z, x, y, z
        # set()
        # double loop through s -> try to compute longest substring -> if duplicate stop
        res = 0
        for i in range(len(s)):
            substring = set(s[i])
            curr_count = 1
            for j in range(i+1, len(s)):
                if s[j] in substring:
                    break
                substring.add(s[j])
                curr_count += 1
            res = max(res, curr_count)
        
        return res
    
    # res = 3
    # curr_count = 3
    # substring = { x, y, z }