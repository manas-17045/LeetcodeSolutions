# Leetcode 1807: Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# Solved on 27th of November, 2025
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        """
        Evaluates a string by replacing bracketed keys with their corresponding values from a knowledge base.
        If a key is not found, it is replaced with a '?'.

        Args:
            s (str): The input string containing bracketed keys.
            knowledge (list[list[str]]): A list of key-value pairs, where each inner list is [key, value].

        Returns:
            str: The evaluated string with keys replaced by their values or '?'.
        """
        knowledgeMap = dict(knowledge)
        resultList = []
        currentKey = []
        isParsingKey = False

        for char in s:
            if char == '(':
                isParsingKey = True
            elif char == ')':
                isParsingKey = False
                keyString = "".join(currentKey)
                if keyString in knowledgeMap:
                    resultList.append(knowledgeMap[keyString])
                else:
                    resultList.append("?")
                currentKey = []
            elif isParsingKey:
                currentKey.append(char)
            else:
                resultList.append(char)

        return "".join(resultList)