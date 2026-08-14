class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0 
        nums.sort()
        answer = float('inf')
        for i in range(len(nums) -k + 1):
            lowest = nums[i]
            highest = nums[ i + k - 1]
            difference = highest - lowest 
            answer = min(difference, answer)
        return answer    
