# Leetcode 1705: Maximum Number of Eaten Apples
# https://leetcode.com/problems/maximum-number-of-eaten-apples/
# Solved on 22nd of November, 2025
import heapq


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        """
        Calculates the maximum number of apples that can be eaten.

        Args:
            apples: A list of integers where apples[i] is the number of apples grown on day i.
            days: A list of integers where days[i] is the number of days apples[i] will last.
        Returns:
            The maximum number of apples that can be eaten.
        """
        minHeap = []
        eatenCount = 0
        currentDay = 0
        n = len(apples)

        while currentDay < n:
            if apples[currentDay] > 0:
                heapq.heappush(minHeap, [currentDay + days[currentDay], apples[currentDay]])

            while minHeap and minHeap[0][0] <= currentDay:
                heapq.heappop(minHeap)

            if minHeap:
                minHeap[0][1] -= 1
                eatenCount += 1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)

            currentDay += 1

        while minHeap:
            while minHeap and minHeap[0][0] <= currentDay:
                heapq.heappop(minHeap)

            if not minHeap:
                break

            rotDay, appleCount = heapq.heappop(minHeap)
            canEat = min(appleCount, rotDay - currentDay)
            eatenCount += canEat
            currentDay += canEat

        return eatenCount