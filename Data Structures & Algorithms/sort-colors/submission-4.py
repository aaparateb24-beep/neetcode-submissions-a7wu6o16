class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0 
        right = len(nums) -1 
        curr = 0 
        while curr <= right:
            #found a 0 
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr] , nums[left]
                left += 1
                curr += 1
            #found a 2
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
                # DON'T move curr
                # new value came from right

            # found a 1
            else:
                
                curr += 1
                        