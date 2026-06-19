class Solution:
    # [9,2,2,4,6,1,5]
    # [1,2,2,4,5,6,9]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i+1, total+candidates[i], curr)
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            curr.pop()
            dfs(i+1, total, curr)
        
        dfs(0, 0, [])

        return res