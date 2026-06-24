# Leetcode 3955: Valid Binary Strings With Cost Limit
# https://leetcode.com/valid-binary-strings-with-cost-limit/
# Solved on 24th of June, 2026
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        """
        Generates valid binary strings using backtracking.
        
        :param n: The length of the binary string.
        :param k: The cost limit.
        :return: The list of valid binary strings.
        """
        resultList = []

        def findStrings(currentIndex, currentCost, prevChar, currentString):
            if currentIndex == n:
                resultList.append("".join(currentString))
                return

            currentString.append("0")
            findStrings(currentIndex + 1, currentCost, "0", currentString)
            currentString.pop()

            if prevChar != "1" and currentCost + currentIndex <= k:
                currentString.append("1")
                findStrings(currentIndex + 1, currentCost + currentIndex, "1", currentString)
                currentString.pop()

        findStrings(0, 0, "1", [])
        return resultList