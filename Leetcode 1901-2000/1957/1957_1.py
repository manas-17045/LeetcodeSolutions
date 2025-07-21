# Leetcode 1957: Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Solved on 21st of July, 2025
class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Deletes characters from a string such that no three consecutive characters are the same.
        :param s: The input string.
        :return: The fancy string.
        """
        resultList = []
        for currentChar in s:
            if len(resultList) < 2 or not ((resultList[-1] == currentChar) and (resultList[-2] == currentChar)):
                resultList.append(currentChar)
        return "".join(resultList)