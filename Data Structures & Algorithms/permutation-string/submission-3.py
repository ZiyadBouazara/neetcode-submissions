class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        hmap_s1, hmap_s2 = {}, {}
        for c in s1:
            hmap_s1[c] = hmap_s1.get(c, 0) + 1

        k = len(s1)
        l = 0
        for r in range(len(s2)):
            hmap_s2[s2[r]] = hmap_s2.get(s2[r], 0) + 1

            if r - l + 1 == k:
                if hmap_s1 == hmap_s2:
                    return True
                
                # slide window
                hmap_s2[s2[l]] -= 1
                if hmap_s2[s2[l]] == 0:
                    del hmap_s2[s2[l]]
                l += 1

        return False	

        