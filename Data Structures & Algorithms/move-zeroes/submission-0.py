class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0 
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        while write in range(len(nums)):
            nums[write] = 0 
            write += 1            


        
        