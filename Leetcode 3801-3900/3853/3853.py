# Leetcode 3853: Merge Close Characters
# https://leetcode.com/problems/merge-close-characters/
# Solved on 1st of March, 2026
class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        """
        Merges identical characters in a string if they are within a distance of k.

        :param s: The input string to process.
        :param k: The maximum distance between two identical characters to allow a merge.
        :return: The resulting string after all possible merges are performed.
        """
        stringList = list(s)

        while True:
            hasMerged = False
            listLen = len(stringList)
            for leftIndex in range(listLen):
                for rightIndex in range(leftIndex + 1, min(leftIndex + k + 1, listLen)):
                    if stringList[leftIndex] == stringList[rightIndex]:
                        stringList.pop(rightIndex)
                        hasMerged = True
                        break

                if hasMerged:
                    break

            if not hasMerged:
                break

        return "".join(stringList)