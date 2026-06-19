class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_map, t_map = {}, {}

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        matches, need = 0, len(t_map) 
        l = 0
        indices, min_len = (-1, -1), float("inf")

        for r in range(len(s)):
            # increase window size from right
            s_map[s[r]] = s_map.get(s[r], 0) + 1

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                matches += 1

            # shrink window size from left
            while matches == need:
                if (r - l + 1) < min_len:
                    indices = (l, r)
                    min_len = r - l + 1

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    matches -= 1
                l += 1
        l, r = indices
        return s[l:r + 1]