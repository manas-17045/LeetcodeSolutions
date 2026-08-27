# Leetcode 4006: Count Valid Prefixes
# https://leetcode.com/problems/count-valid-prefixes/
# Solved on 27th of August, 2026
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        """
        Calculates the number of prefixes of a binary string that can be rearranged
        to form an alternating string.

        Parameters:
            s (str): The input binary string.

        Returns:
            int: The total count of valid alternating prefixes.
        """
        vpCount = 0
        zCount = 0
        oCount = 0

        for charValue in s:
            if charValue == "0":
                zCount += 1
            else:
                oCount += 1
            
            if abs(zCount - oCount) <= 1:
                vpCount += 1
        
        return vpCount