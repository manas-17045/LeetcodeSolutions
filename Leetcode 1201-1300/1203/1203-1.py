# Leetcode 1203: Sort Items by Groups Respecting Dependencies
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# Solved on 24th of August, 2025
import collections


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        """
        Sorts items by groups respecting dependencies.

        Args:
            n (int): The number of items.
            m (int): The number of existing groups.
            group (list[int]): A list where group[i] is the group id of item i. -1 means no group.
            beforeItems (list[list[int]]): A list where beforeItems[i] is a list of items that must be placed before item i.
        Returns:
            list[int]: A list of item indices representing the sorted order, or an empty list if no valid order exists.
        """
        nextGroupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = nextGroupId
                nextGroupId += 1

        numGroups = nextGroupId

        itemGraph = collections.defaultdict(list)
        itemIndegree = [0] * n
        groupGraph = collections.defaultdict(list)
        groupIndegree = [0] * numGroups

        for i in range(n):
            for prevItem in beforeItems[i]:
                itemGraph[prevItem].append(i)
                itemIndegree[i] += 1

                groupPrev = group[prevItem]
                groupCurr = group[i]
                if groupPrev != groupCurr:
                    groupGraph[groupPrev].append(groupCurr)
                    groupIndegree[groupCurr] += 1

        def topologicalSort(graph, inDegree, count):
            sortedList = []
            queue = collections.deque()
            for i in range(count):
                if inDegree[i] == 0:
                    queue.append(i)

            while queue:
                node = queue.popleft()
                sortedList.append(node)

                if node in graph:
                    for neighbor in graph[node]:
                        inDegree[neighbor] -= 1
                        if inDegree[neighbor] == 0:
                            queue.append(neighbor)

            return sortedList if len(sortedList) == count else []

        sortedItems = topologicalSort(itemGraph, itemIndegree, n)
        sortedGroups = topologicalSort(groupGraph, groupIndegree, numGroups)

        if not sortedItems or not sortedGroups:
            return []

        itemsByGroup = collections.defaultdict(list)
        for item in sortedItems:
            itemsByGroup[group[item]].append(item)

        finalResult = []
        for groupId in sortedGroups:
            finalResult.extend(itemsByGroup[groupId])

        return finalResult