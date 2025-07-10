# Leetcode 3440: Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
# Solved on 10th of July, 2025
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        """
        Calculates the maximum free time achievable by rescheduling at most one meeting.

        Args:
            eventTime: The total duration of the event.
            startTime: A list of start times for existing meetings.
            endTime: A list of end times for existing meetings.

        Returns:
            The maximum free time.
        """
        n = len(startTime)

        if n == 0:
            return eventTime

        initialGaps = []
        initialGaps.append(startTime[0])
        for i in range(n - 1):
            initialGaps.append(startTime[i + 1] - endTime[i])
        initialGaps.append(eventTime - endTime[n - 1])

        maxFree = 0
        if initialGaps:
            maxFree = max(initialGaps)

        if n < 2:
            duration = endTime[0] - startTime[0]
            return max(maxFree, (eventTime - duration))

        numGaps = n + 1
        prefixTop2 = [(-1, -1)] * numGaps
        suffixTop2 = [(-1, -1)] * numGaps

        prefixTop2[0] = (initialGaps[0], -1)
        for i in range(1, numGaps):
            val = initialGaps[i]
            prevMax, prevSecMax = prefixTop2[i - 1]
            if val >= prevMax:
                prefixTop2[i] = (val, prevMax)
            elif val > prevSecMax:
                prefixTop2[i] = (prevMax, val)
            else:
                prefixTop2[i] = (prevMax, prevSecMax)

        suffixTop2[numGaps - 1] = (initialGaps[numGaps - 1], -1)
        for i in range(numGaps - 2, -1, -1):
            val = initialGaps[i]
            nextMax, nextSecMax = suffixTop2[i + 1]
            if val >= nextMax:
                suffixTop2[i] = (val, nextMax)
            elif val > nextSecMax:
                suffixTop2[i] = (nextMax, val)
            else:
                suffixTop2[i] = (nextMax, nextSecMax)

        def mergeTop2(t1, t2):
            nums = [x for x in [t1[0], t1[1], t2[0], t2[1]] if x != -1]
            if not nums:
                return (-1, -1)
            nums.sort()
            resMax = nums[0]
            resSecMax = nums[1] if len(nums) > 1 else -1
            return resMax, resSecMax

        for k in range(n):
            durationK = endTime[k] - startTime[k]

            newLenK = 0
            if k == 0:
                newLenK = startTime[1]
            elif k == (n - 1):
                newLenK = eventTime - endTime[n - 2]
            else:
                newLenK = startTime[k + 1] - endTime[k - 1]

            otherGapsTop2 = (-1, -1)
            if k == 0:
                if numGaps > 2:
                    otherGapsTop2 = suffixTop2
            elif k == (n - 1):
                if (n - 2) >= 0:
                    otherGapsTop2 = prefixTop2[n - 2]
            else:
                otherGapsTop2 = mergeTop2(prefixTop2[k - 1], suffixTop2[k + 2])

            lMax, lSecMax = otherGapsTop2
            if lMax == -1:
                lMax = 0
            if lSecMax == -1:
                lSecMax = 0

            currentLMax = 0
            currentLSecMax = 0
            if newLenK >= lMax:
                currentLMax = newLenK
                currentLSecMax = lMax
            elif newLenK > lSecMax:
                currentLMax = lMax
                currentLSecMax = newLenK
            else:
                currentLMax = lMax
                currentLSecMax = lSecMax

            candidateMaxFree = 0
            if durationK <= currentLSecMax:
                candidateMaxFree = currentLMax
            else:
                candidateMaxFree = max((currentLMax - durationK), currentLSecMax)

            maxFree = max(maxFree, candidateMaxFree)

        return maxFree