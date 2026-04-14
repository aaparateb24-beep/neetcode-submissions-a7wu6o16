from collections import Counter

class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        res = []
        
        for num in count: #iterting through nums one by one
            if count[num] > len(nums) // 3: #focus on num
                res.append(num)
                
        return res