class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        dict1 = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in dict1:
                return [dict1[difference], index]
            dict1[number] = index