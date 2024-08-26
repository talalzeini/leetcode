class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # n => number of strings
        # m => average length of a string
        #
        # Time Complexity: O(n * m * 26) => O(n * m)
        # Space Complexity: O(n)

        ans = defaultdict(list)

        for string in strs:
            count = [0] * 26
            print(count)
            for character in string:
                count[ord(character) - ord('a')] += 1
            ans[tuple(count)].append(string)
        print(ans)
        return ans.values()
