# Leetcode 1723: Find Minimum Time to Finish All Jobs
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
# Solved on 25th of August, 2025
class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        """
        Calculates the minimum possible maximum workload among all workers.

        Args:
            jobs: A list of integers representing the time required for each job.
            k: An integer representing the number of workers available.

        Returns:
            An integer representing the minimum possible maximum workload.
        """
        jobs.sort(reverse=True)
        n = len(jobs)
        lo, hi = max(jobs), sum(jobs)

        def can_finish(limit: int) -> bool:
            workloads = [0] * k

            def dfs(idx: int) -> bool:
                if idx == n:
                    return True

                job = jobs[idx]
                seen = set()
                for i in range(k):
                    if workloads[i] in seen:
                        # Skip equivalent states
                        continue
                    if workloads[i] + job <= limit:
                        seen.add(workloads[i])
                        workloads[i] += job
                        if dfs(idx + 1):
                            return True
                        workloads[i] -= job

                    if workloads[i] == 0:
                        break

                return False

            return dfs(0)

        # Binary search for minimum feasible maximum workload
        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo