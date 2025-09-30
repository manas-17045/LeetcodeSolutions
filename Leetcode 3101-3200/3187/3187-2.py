# Leetcode 3187: Peaks in Array
# https://leetcode.com/problems/peaks-in-array/
# Solved on 30th of September, 2025
class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Counts the number of peaks in given ranges and updates the array.
        :param nums: The input array of integers.
        :param queries: A list of queries. Each query is either a type 1 query [1, l, r] to count peaks in range [l, r],
                        or a type 2 query [2, idx, val] to update nums[idx] to val.
        :return: A list of integers, where each element is the answer to a type 1 query.
        """
        n = len(nums)

        def isPeak(i):
            if i <= 0 or i >= n - 1:
                return False
            return nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        tree = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = 0
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                tree[node] = tree[2 * node] + tree[2 * node + 1]

        def update(node, start, end, idx):
            if start == end:
                tree[node] = 1 if isPeak(start) else 0
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2 * node, start, mid, idx)
                else:
                    update(2 * node + 1, mid + 1, end, idx)
                tree[node] = tree[2 * node] + tree[2 * node + 1]

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            leftSum = query(2 * node, start, mid, l, r)
            rightSum = query(2 * node + 1, mid + 1, end, l, r)
            return leftSum + rightSum

        build(1, 0, n - 1)

        for i in range(n):
            if isPeak(i):
                update(1, 0, n - 1, i)

        result = []

        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                if r - l < 2:
                    result.append(0)
                else:
                    count = query(1, 0, n - 1, l + 1, r - 1)
                    result.append(count)
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                for i in range(max(1, idx - 1), min(n - 1, idx + 2)):
                    update(1, 0, n - 1, i)

        return result