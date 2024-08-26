class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Time Complexity: O(nlog(n)) + O(n^2) = O(n^2)
        # Auxiliary Space Complexity: O(1) usually
        
        nums.sort()
        result = []

        for i in range(len(nums)):

            # don't reuse same i to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum == 0:
                    subarray = [nums[i], nums[left], nums[right]]
                    result.append(subarray)

                    # continue and add left right so we can get all subarrays
                    left +=1
                    right-=1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
        return result