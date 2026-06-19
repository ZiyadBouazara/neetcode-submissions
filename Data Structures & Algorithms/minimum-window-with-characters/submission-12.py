class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_map, s_map = {}, {}

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        indices, min_len = (-1, -1), float("inf")
        l = 0
        matches, need = 0, len(t_map)

        for r in range(len(s)):
            c = s[r]
            s_map[c] = s_map.get(c, 0) + 1

            if c in t_map and s_map[c] == t_map[c]:
                matches += 1
            
            while matches == need:
                if r - l + 1 < min_len:
                    indices = (l, r)
                    min_len = r - l + 1

                s_map[s[l]] -= 1
                if s[l] in t_map and t_map[s[l]] > s_map[s[l]]:
                    matches -= 1
            
                if s_map[s[l]] == 0:
                    del s_map[s[l]]

                l += 1

        return s[indices[0]: indices[1] + 1]
