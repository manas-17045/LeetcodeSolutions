# Leetcode 3433: Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/
# Solved on 10th of December, 2025
class Solution:
    def countMntions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        """
        Counts the number of mentions each user receives based on a series of events.

        Args:
            numberOfUsers (int): The total number of users, indexed from 0 to numberOfUsers - 1.
            events (list[list[str]]): A list of events, where each event is a list of strings.
                                      Events can be "OFFLINE", "MENTION ALL", "MENTION HERE", or "MENTION <user_ids>".

        Returns:
            list[int]: A list where the i-th element is the total number of mentions for user i.
        """
        mentions = [0] * numberOfUsers
        backOnlineTime = [0] * numberOfUsers

        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event in events:
            eventType = event[0]
            timestamp = int(event[1])

            if eventType == "OFFLINE":
                userId = int(event[2])
                backOnlineTime[userId] = timestamp + 60
            else:
                mentionString = event[2]
                if mentionString == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentionString == "HERE":
                    for i in range(numberOfUsers):
                        if timestamp >= backOnlineTime[i]:
                            mentions[i] += 1
                else:
                    ids = mentionString.split()
                    for idStr in ids:
                        userId = int(idStr[2:])
                        mentions[userId] += 1

        return mentions