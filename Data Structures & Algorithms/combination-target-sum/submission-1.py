class Solution:
    def combinationSum(self, candidates, target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i, remaining):
            if remaining == 0 :
                result.append(path.copy())
                return 
            if i == len(candidates):
                return
            num = candidates[i]  
            if num <= remaining:
                path.append(num)
                backtrack(i, remaining - num)
                path.pop()
            backtrack(i + 1, remaining) 
        backtrack(0, target)  
        return result
          
            
        
        
        