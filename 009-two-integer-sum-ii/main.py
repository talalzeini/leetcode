class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)):
            
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left+1, right+1]
            
            if twoSum > target:
                right -= 1
            else:
                left += 1