class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        res = 0 
        left = 0
        right = len(heights) - 1

        while left < right:
            # keep track of maximum area
            # replace it with anything higher
            # two pointer left and right, take lower height and multiply it by horizontal
            # check if it's bigger than our current maximum area tracked
            res = max(res, min(heights[left], heights[right]) * (right - left))
            # keep on finding bigger heights
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
