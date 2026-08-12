class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0 
        ans = 0 
        for num in nums:
            if num == 1:
                current += 1
                ans = max(current, ans)
            else:
                current = 0 
        return ans            