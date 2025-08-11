# Leetcode 3257: Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/
# Solved on 11th of August, 2025
class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        """
        Finds the most common response across all days, considering only unique responses per day.
        If there's a tie in frequency, the lexicographically smallest response is returned.

        :param responses: A list of lists of strings, where each inner list represents responses for a day.
        :return: The most common response as a string, or an empty string if no responses are provided.
        """
        freq = {}
        for day in responses:
            uniqueDay = set(day)
            for response in uniqueDay:
                if response not in freq:
                    freq[response] = 0
                freq[response] += 1

        if not freq:
            return ""
        maxFreq = max(freq.values())
        candidates = [response for response, count in freq.items() if count == maxFreq]
        return min(candidates)