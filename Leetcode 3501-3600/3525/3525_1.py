# Leetcode 3525: Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/
# Solved on 1st of June, 2025

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        """
        Finds the count of subarrays starting from a given index whose product modulo k equals a target value.

        This function uses a segment tree to efficiently handle updates to the array and queries about
        subarray products modulo k. Each node in the segment tree stores the counts of subarray products
        modulo k for the range it covers, and the total product modulo k for that range.

        Args:
            nums: The input array of integers.
            k: The modulo value.
            queries: A list of queries, where each query is [qIdx, qVal, qStart, qxValTarget].
                     qIdx: The index in nums to update.
                     qVal: The new value for nums[qIdx].
                     qStart: The starting index for the subarray query.
                     qxValTarget: The target product modulo k for the subarray.

        Returns:
            A list of integers, where each element is the count of subarrays starting from qStart
            whose product modulo k equals qxValTarget after the update specified by the query.
        """
        N = len(nums)

        tree = [None] * (4 * N)

        # Helper function to combine results from two children nodes or query parts
        def combineResults(leftCounts, leftTotalProd, rightCounts, rightTotalProd, kVal):
            combinedTotalProd = (leftTotalProd * rightTotalProd) % kVal
            combinedCounts = list(leftCounts)

            for valRModK in range(kVal):
                if rightCounts[valRModK] > 0:
                    newProdModK = (leftTotalProd * valRModK) % kVal
                    combinedCounts[newProdModK] += rightCounts[valRModK]

            return (combinedCounts, combinedTotalProd)

        # Segment Tree build function
        # node_idx: current node index in tree array
        # L, R: range [L, R] covered by this node (0-indexed based on nums).
        def build(node_idx, L, R):
            if L == R:
                val_mod_k = nums[L] % k
                counts = [0] * k
                tree[node_idx] = (counts, val_mod_k)
                return

            M = (L + R) // 2
            build(2 * node_idx, L, M)
            build(2 * node_idx + 1, M + 1, R)

            leftResCounts, leftResTotalProd = tree[2 * node_idx]
            rightResCounts, rightResTotalProd = tree[2 * node_idx + 1]
            # Store combined result in tree.
            tree[node_idx] = combineResults(leftResCounts, leftResTotalProd, rightResCounts, rightResTotalProd, k)

        # Segment Tree update function
        # targetIdx: index in nums to update
        # newVal: new value for nums[target_idx]
        def updateTree(node_idx, L, R, target_idx, newVal):
            if L == R:
                val_mod_k = newVal % k
                counts = [0] * k
                counts[val_mod_k] = 1
                # Store updated data in tree
                tree[node_idx] = (counts, val_mod_k)
                return

            M = (L + R) // 2
            if target_idx <= M:
                updateTree(2 * node_idx, L, M, target_idx, newVal)
            else:
                updateTree(2 * node_idx + 1, M + 1, R, target_idx, newVal)

            # After child update, re-combine results from children for this node.
            leftResCounts, leftResTotalProd = tree[2 * node_idx]
            rightResCounts, rightResTotalProd = tree[2 * node_idx + 1]
            # Store recombined result in a tree.
            tree[node_idx] = combineResults(leftResCounts, leftResTotalProd, rightResCounts, rightResTotalProd, k)

        # Segment Tree query function
        # queryL, queryR: range for which to calculate aggregated prefix counts
        def queryTree(node_idx, L, R, queryL, queryR):
            if queryL > queryR:
                return [0] * k, 1

            if L == queryL and R == queryR:
                return tree[node_idx]

            M = (L + R) // 2

            resL = queryTree(2 * node_idx, L, M, queryL, min(M, queryR))

            resR = queryTree(2 * node_idx + 1, M + 1, R, max(M + 1, queryL), queryR)

            return combineResults(resL[0], resL[1], resR[0], resR[1], k)

        # Main logic of resultArray function from here.
        if N == 0:
            return []

        # Initial construction of the Segment Tree
        build(1, 0, N - 1)

        ans = []
        # Process each query.
        for qIdx, qVal, qStart, qxValTarget in queries:
            nums[qIdx] = qVal
            updateTree(1, 0, N - 1, qIdx, qVal)

            if qStart >= N:
                ans.append(0)
            else:
                final_counts, _ = queryTree(1, 0, N - 1, qStart, N - 1)
                ans.append(final_counts[qxValTarget])

        return ans