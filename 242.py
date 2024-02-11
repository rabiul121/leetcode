# Problem No. 242. Valid Anagram
# Difficulty Level: Easy
# Runtime: 43ms
# Memory consumption: 16.81MB


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True"""

        # Solution 2
        # Runtime: 40ms
        # Memory consumption: 17MB

        # return Counter(s) == Counter(t)

        # Solution 3
        # Runtime: 50ms
        # Memory consumption: 17.5MB

        return sorted(s) == sorted(t)

        # The first solution is the most efficient, but the third solution is the most readable. The second solution is the most concise.
