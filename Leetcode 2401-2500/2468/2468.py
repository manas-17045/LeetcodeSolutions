# Leetcode 2468: Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/
# Solved on 15th of November, 2025
class Solution:
    def splitMessage(self, message: str, limit: int) -> list[str]:
        """
        Splits a message into multiple parts, each respecting a given character limit.
        Each part will have a suffix like "<x/y>", where x is the current part number
        and y is the total number of parts.

        Args:
            message (str): The original message to be split.
            limit (int): The maximum character limit for each split part.
        Returns:
            list[str]: A list of strings, where each string is a split part of the message,
                       or an empty list if the message cannot be split according to the limit.
        """
        def getDigitsSum(k):
            if k == 0:
                return 0
            lenK = len(str(k))
            total = 0
            power = 1
            for i in range(1, lenK):
                count = power * 9
                total += count * i
                power *= 10
            count = k - power + 1
            total += count * lenK
            return total

        n = len(message)

        for totalParts in range(1, n + 1):
            lenB = len(str(totalParts))
            lastSuffixLen = 3 + lenB + lenB

            if lastSuffixLen >= limit:
                break

            prevPartsDigitsSum = getDigitsSum(totalParts - 1)

            contentInPrevParts = (limit - 3 - lenB) * (totalParts - 1) - prevPartsDigitsSum

            if n <= contentInPrevParts:
                continue

            contentInLastPart = limit - lastSuffixLen
            maxCapacity = contentInPrevParts + contentInLastPart

            if n <= maxCapacity:
                result = []
                msgIndex = 0
                for currentPart in range(1, totalParts + 1):
                    suffix = f"<{currentPart}/{totalParts}>"
                    suffixLen = len(suffix)
                    contentLen = limit - suffixLen

                    if currentPart < totalParts:
                        part = message[msgIndex: msgIndex + contentLen]
                        result.append(part + suffix)
                        msgIndex += contentLen
                    else:
                        part = message[msgIndex:]
                        result.append(part + suffix)
                return result

        return []