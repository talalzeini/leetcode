class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        count = {}
        arr = [[] for i in range(len(nums) + 1)] # array of max len(n)
        result = []

        for number in (nums):
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
                
        for n, c in count.items():
            arr[c].append(n)  

        for subarray in range(len(arr) - 1, 0, -1):
            for j in arr[subarray]:
                result.append(j)
                if len(result) == k:
                    return result
