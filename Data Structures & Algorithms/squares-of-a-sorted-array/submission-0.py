class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        pos = len(nums) -1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:

                res[pos] = left_square
                left += 1
            else:
                res[pos] = right_square
                right -=1
            pos -=1
        return res    


        