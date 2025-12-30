# Leetcode 3612: Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/
# Solved on 30th of December, 2025
class Solution:
    def processStr(self, s: str) -> str:
        """
        Processes a string with special operations based on specific characters.
        :param s: The input string to be processed.
        :return: The processed string after applying all operations.
        """
        resultList = []
        for char in s:
            if char == '*':
                if resultList:
                    resultList.pop()
            elif char == '#':
                resultList.extend(resultList)
            elif char == '%':
                resultList.reverse()
            else:
                resultList.append(char)

        return "".join(resultList)