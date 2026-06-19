class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["bat","bag","bank","band"]
        #                      i
        #                       s
        # res = "ba"
        # current = [b,a]

        res = list(strs[0])

        for s in strs:
            curr = []
            
            for i in range(min(len(res), len(s))):
                if s[i] == res[i]:
                    curr.append(s[i])
                else: 
                    break
            
            if len(curr) < len(res):
                res = curr
        
        return "".join(res)

