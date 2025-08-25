# Leetcode 1723: Find Minimum Time to Finish All Jobs
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
# Solved on 25th of August, 2025
class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        """
        Finds the minimum time required to finish all jobs given k workers.

        Args:
            jobs (list[int]): A list of integers representing the time taken by each job.
            k (int): The number of workers available.
        Returns:
            int: The minimum time required to finish all jobs.
        """
        numJobs = len(jobs)
        jobs.sort(reverse=True)

        low = jobs[0]
        high = sum(jobs)
        ans = high

        def isPossible(timeLimit):
            workerTimes = [0] * k

            def backtrack(jobIndex):
                if jobIndex == numJobs:
                    return True

                currentJob = jobs[jobIndex]

                for i in range(k):
                    if workerTimes[i] + currentJob <= timeLimit:
                        workerTimes[i] += currentJob
                        if backtrack(jobIndex + 1):
                            return True
                        workerTimes[i] -= currentJob

                    if workerTimes[i] == 0:
                        break

                return False

            return backtrack(0)

        while low <= high:
            mid = low + (high - low) // 2
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans