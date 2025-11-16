# Leetcode 2284: Sender With Largest Word Count
# https://leetcode.com/problems/sender-with-largest-word-count/
# Solved on 16th of November, 2025
from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        """
        Calculates the sender with the largest total word count. If multiple senders have the same largest word count,
        the sender whose name is lexicographically largest is returned.

        Args:
            messages (list[str]): A list of strings representing the messages sent.
            senders (list[str]): A list of strings representing the senders of the corresponding messages.
        Returns:
            str: The name of the sender with the largest total word count.
        """
        senderCounts = defaultdict(int)

        for message, sender in zip(messages, senders):
            wordCount = message.count(' ') + 1
            senderCounts[sender] += wordCount

        maxSender = ""
        maxCount = 0

        for sender, count in senderCounts.items():
            if count > maxCount:
                maxCount = count
                maxSender = sender
            elif count == maxCount and sender > maxSender:
                maxSender = sender

        return maxSender