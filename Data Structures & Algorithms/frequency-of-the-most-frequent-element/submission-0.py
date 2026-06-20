class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        best = 0
        window_sum = 0
        for right in range(len(nums)):
            target = nums[right]
            window_sum += nums[right]
            window_size = right - left +1 
            operations_needed = (target * window_size - window_sum)

            while operations_needed > k:
                window_sum -= nums[left]
                left += 1
                window_size = right - left +1 
                operations_needed = (target * window_size - window_sum)

            best = max(best, window_size)
        return best     
