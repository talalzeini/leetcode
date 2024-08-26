class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Time Complexity: O(log(n))
        # Space Complexity: O(1)
        
        low = 0
        high = len(nums) - 1

        while low <= high: # <=
            mid = low + ((high - low) // 2) # important to be inside loop
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            if target > nums[mid]:
                low = mid + 1
        return -1
            
