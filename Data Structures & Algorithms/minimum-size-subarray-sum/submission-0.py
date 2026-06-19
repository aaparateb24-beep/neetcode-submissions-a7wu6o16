class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        window_sum = 0 
        min_len = float('inf')
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            while window_sum >= target:
                
                curr_len = right - left + 1
                min_len = min(curr_len, min_len)

                window_sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        return min_len    
                
        