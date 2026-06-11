class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in h:
                return [h[diff], index]
            h[value] = index

    #Index is our pointing index
    #Value is the numeric value in our array

                
                     
        