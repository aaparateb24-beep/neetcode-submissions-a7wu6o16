class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i ,n in enumerate(nums): #enumerate for both index and value
            complement = target - n
            if complement in map:
                return[map[complement],i]
            map[n] = i    #if n not present then add 

        