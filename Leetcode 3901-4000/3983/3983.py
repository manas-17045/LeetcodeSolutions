# Leetcode 3983: Subsequence After One Replacement
# https://leetcode.com/problems/subsequence-after-one-replacement/
# Solved on 1st of August, 2026
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        """
        Checks if string t can be obtained from string s by deleting zero or more
        characters from s and then replacing at most one character in the resulting
        string with any other character.
        
        Args:
            s: The first string.
            t: The second string.
            
        Returns:
            True if t can be obtained from s by deleting zero or more
            characters from s and then replacing at most one character in the
            resulting string with any other character, False otherwise.
        """
        sLen = len(s)
        tLen = len(t)

        if sLen > tLen:
            return False

        if sLen == 1:
            return True

        prefMatch = [float('inf')] * sLen
        tIndex = 0

        for sIndex in range(sLen):
            while tIndex < tLen and t[tIndex] != s[sIndex]:
                tIndex += 1
            if tIndex < tLen:
                prefMatch[sIndex] = tIndex
                tIndex += 1
            else:
                break

        if prefMatch[sLen - 1] < float('inf'):
            return True
        
        suffMatch = [float('-inf')] * sLen
        tIndex = tLen - 1

        for sIndex in range(sLen - 1, -1, -1):
            while tIndex >= 0 and t[tIndex] != s[sIndex]:
                tIndex -= 1
            if tIndex >= 0:
                suffMatch[sIndex] = tIndex
                tIndex -= 1
            else:
                break

        if suffMatch[1] >= 1:
            return True

        if prefMatch[sLen - 2] <= tLen - 2:
            return True

        for sIndex in range(1, sLen - 1):
            if prefMatch[sIndex - 1] < float('inf') and suffMatch[sIndex + 1] > float('-inf'):
                if suffMatch[sIndex + 1] - prefMatch[sIndex - 1] >= 2:
                    return True

        return False