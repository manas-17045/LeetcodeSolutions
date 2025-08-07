# Leetcode 2092: Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/
# Solved on 7th of August, 2025
class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        """
        Finds all people who eventually learn the secret.

        Args:
            n (int): The total number of people, labeled from 0 to n - 1.
            meetings (list[list[int]]): A list of meetings, where each meeting is [x, y, time]
                                       indicating that person x and person y met at time.
            firstPerson (int): The first person to know the secret, besides person 0.

        Returns:
            list[int]: A list of all people who eventually learn the secret.
        """
        parent = list(range(n))
        size = [1] * n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                if size[rootI] < size[rootJ]:
                    rootI, rootJ = rootJ, rootI
                parent[rootJ] = rootI
                size[rootI] += size[rootJ]
        
        def reset(i):
            parent[i] = i
            size[i] = 1

        union(0, firstPerson)
        
        meetings.sort(key=lambda m: m[2])
        
        i = 0
        numMeetings = len(meetings)
        
        while i < numMeetings:
            j = i
            while j + 1 < numMeetings and meetings[j + 1][2] == meetings[i][2]:
                j += 1
            
            peopleInBatch = set()
            for k in range(i, j + 1):
                p1, p2, _ = meetings[k]
                union(p1, p2)
                peopleInBatch.add(p1)
                peopleInBatch.add(p2)
            
            secretRoot = find(0)
            for person in peopleInBatch:
                if find(person) != secretRoot:
                    reset(person)
            
            i = j + 1
            
        result = []
        secretRoot = find(0)
        for person in range(n):
            if find(person) == secretRoot:
                result.append(person)
        
        return result