# Leetcode 3295: Report Spam Message
# https://leetcode.com/problems/report-spam-message/
# Solved on 4th of November, 2025
class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        """
        Determines if a message should be reported as spam based on the presence of banned words.

        Args:
            message: A list of strings representing the words in the message.
            bannedWords: A list of strings representing words that are considered spam.
        Returns:
            True if two or more banned words are found in the message, False otherwise.
        """
        bannedSet = set(bannedWords)
        spamCount = 0

        for word in message:
            if word in bannedSet:
                spamCount += 1

            if spamCount == 2:
                return True

        return False