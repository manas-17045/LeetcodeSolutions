# Leetcode 3999: Minimum Number of String Groups Through Transformations
# https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/
# Solved on 21st of August, 2026
class Solution:
    def minimumGroups(self, words:list[str]) -> int:
        """
        Calculates the number of unique equivalence groups formed by the input words
        based on the canonical rotations of their even-indexed and odd-indexed characters.

        Args:
            words (List[str]): A list of strings to be grouped.

        Returns:
            int: The total count of distinct groups.
        """
        uniqueGroups = set()

        for currentWord in words:
            evenChars = currentWord[0::2]
            oddChars = currentWord[1::2]

            evenSignature = self.getSmallestRotation(evenChars)
            oddSignature = self.getSmallestRotation(oddChars)

            uniqueGroups.add((evenSignature, oddSignature))

        return len(uniqueGroups)
    
    
    def getSmallestRotation(self, stringValue: str) -> str:

        stringLength = len(stringValue)

        if stringLength == 0:
            return ""

        indexI = 0
        indexJ = 1
        matchCount = 0

        while indexI < stringLength and indexJ < stringLength and matchCount < stringLength:
            charI = stringValue[(indexI + matchCount) % stringLength]
            charJ = stringValue[(indexJ + matchCount) % stringLength]

            if charI == charJ:
                matchCount += 1
            elif charI > charJ:
                indexI += matchCount + 1

                if indexI <= indexJ:
                    indexI = indexJ + 1

                matchCount = 0
            else:
                indexJ += matchCount + 1

                if indexJ <= indexI:
                    indexJ = indexI + 1

                matchCount = 0

        startIndex = min(indexI, indexJ)
        
        return stringValue[startIndex:] + stringValue[:startIndex]