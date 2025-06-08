# Leetcode 2301: Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/
# Solved on 8th of June, 2025
import collections


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        """
        Given two strings s and sub, and a list of character mappings,
        determine if sub is a substring of s after replacing some characters
        in sub according to the mappings.

        Args:
            s: The main string.
            sub: The substring to match.
            mappings: A list of character mappings [oldChar, newChar].
        Returns:
            True if sub can be matched in s after replacements, False otherwise.
        """
        mappingDict = collections.defaultdict(set)
        for oldChar, newChar in mappings:
            mappingDict[oldChar].add(newChar)

        sLen = len(s)
        subLen = len(sub)

        if subLen > sLen:
            return False

        for i in range(sLen - subLen + 1):
            for j in range(subLen):
                subChar = sub[j]
                sChar = s[i + j]

                if subChar != sChar and sChar not in mappingDict[subChar]:
                    break
            else:
                return True

        return False