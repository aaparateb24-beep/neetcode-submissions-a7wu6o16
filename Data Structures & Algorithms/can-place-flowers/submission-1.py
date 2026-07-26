class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            # Check if the left plot is empty.
            # If we're at the first plot, treat the left side as empty.
            left_empty = (i == 0 or flowerbed[i -1] == 0)
            # Check if the right plot is empty.
            # If we're at the last plot, treat the right side as empty.
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
            # We can plant only if:
            # 1. Current plot is empty.
            # 2. Left plot is empty.
            # 3. Right plot is empty.
            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                # If we've planted all required flowers,
                # return True immediately.
                if n == 0 :
                    return True
        return n <= 0            