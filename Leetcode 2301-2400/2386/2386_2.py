# Solved on 16th of June, 2025
import heapq


class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        """
        Finds the k-th largest sum of a subarray of `nums`.

        The problem can be reframed as finding the k-th smallest "deviation"
        from the maximum possible sum (which is the sum of all positive numbers).
        A deviation is the sum of absolute values of the elements that are
        excluded from the maximum sum.

        We first calculate the maximum possible sum by summing all positive numbers.
        Then, we convert all numbers to their absolute values and sort them.
        We use a min-heap to explore possible deviations. The heap stores tuples
        of (current_deviation, index). The index indicates the last element
        considered for the current deviation.

        We repeatedly extract the smallest deviation from the heap and explore
        two possibilities: including the next absolute value or replacing the last
        included absolute value with the next one.
        """
        # Base sum = take all positives
        sumPos = 0
        A = []
        for x in nums:
            if x > 0:
                sumPos += x
                A.append(x)
            elif x < 0:
                A.append(-x)
        # Sort costs ascending
        A.sort()

        # We want the k-th smallest subset-sum of A.
        res = [0]
        if k == 1 or not A:
            return sumPos  # the largest subseq-sum is sumPos

        # min-heap of (subset_sum, last_index_used)
        heap = [(A[0], 0)]

        #Eextract k-1 additional smallest sums
        for _ in range(k - 1):
            s, i = heapq.heappop(heap)
            res.append(s)

            if i + 1 < len(A):
                # Include A[i+1] alongside everything that contributed to s
                heapq.heappush(heap, (s + A[i+1], i+1))
                # Swap out A[i] for A[i+1]
                heapq.heappush(heap, (s - A[i] + A[i+1], i+1))

        # The k-th smallest cost is res[k-1]; subtract from sumPos
        return sumPos - res[k-1]