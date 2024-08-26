class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        numsSet = set(nums)
        if len(nums) != len(numsSet):
            return True
        return False