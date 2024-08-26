class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Time Complexity: O(s + t) => O(n)
        # Space Complexity: O(s + t) => O(n)
        
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}
        
        for i in range(len(s)):
            if s[i] in sCount:
                sCount[s[i]] += 1
            else:
                sCount[s[i]] = 1
            if t[i] in tCount:
                tCount[t[i]] += 1
            else:
                tCount[t[i]] = 1
        return sCount == tCount
