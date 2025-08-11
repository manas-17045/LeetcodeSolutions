# Leetcode 3257: Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/
# Solved on 11th of August, 2025
class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        """
        Finds the most common response across multiple days, considering only unique responses per day.
        If there's a tie in frequency, the lexicographically smallest response is returned.

        Args:
            responses: A list of lists of strings, where each inner list represents responses for a day.

        Returns:
            The most common response string.
        """
        counts = {}
        for day in responses:
            # Remove duplicates within the day
            for resp in set(day):
                counts[resp] = counts.get(resp, 0) + 1

        # Find maximum count
        max_count = max(counts.values())

        # Among responses with max_count choose lexicographically smallest
        best = None
        for resp, cnt in counts.items():
            if cnt == max_count:
                if best is None or resp < best:
                    best = resp

        return best