class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

        # if len(s) < len(t):
        #     return ""

        # s_map, t_map = {}, {}
        # matches = 0

        # for c in t:
        #     t_map[c] = t_map.get(c, 0) + 1

        # l = 0
        # indices, min_len = (0, 0), float("inf")

        # for r in range(len(s)):
        #     # increase window size from right
        #     s_map[s[r]] = s_map.get(s[r], 0) + 1

        #     if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
        #         matches += 1

        #     # shrink window size from left
        #     while matches == len(t):
        #         if (r - l + 1) < min_len:
        #             indices = (l, r)
        #             min_len = r - l + 1

        #         s_map[s[l]] -= 1
        #         if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
        #             matches -= 1
        #         l += 1
        # l, r = indices
        # return s[l:r + 1] if min_len != float("inf") else ""