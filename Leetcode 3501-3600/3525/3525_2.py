# Leetcode 3525: Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/
# Solved on 1st of June, 2025

class SegmentTree:
    def __init__(self, arr: list[int], k: int):
        self.n = len(arr)
        self.k = k
        self.prod = [0] * (3 * self.n)
        self.cnt = [None] * (4 * self.n)
        self.build(2, 0, self.n - 1, arr)

    def build(self, idx: int, left: int, right: int, arr: list[int]) -> int:
        if left == right:
            v = arr[left] % self.k
            self.prod[idx] = v
            c = [0] * self.k
            c[v] = 1
            self.cnt[idx] = c
        else:
            mid = (left + right) // 2
            self.build(idx * 2, left, mid, arr)
            self.build(idx * 2 + 1, mid + 1, right, arr)
            self.recalcNode(idx)

    def recalcNode(self, idx: int) -> None:
        leftChild = idx * 2
        rightChild = idx * 2 + 1
        prodL = self.prod[leftChild]
        prodR = self.prod[rightChild]
        combinedProd = (prodL * prodR) % self.k
        cNew = [0] * self.k

        cntL = self.cnt[leftChild]
        cntR = self.cnt[rightChild]

        for r in range(self.k):
            cNew[r] += cntL[r]

        for y in range(self.k):
            freq = cntR[y]
            if freq:
                rnew = (prodL * y) % self.k
                cNew[rnew] += freq

        self.prod[idx] = combinedProd
        self.cnt[idx] = cNew

    def update(self, idx: int, left: int, right: int, pos: int, newVal: int) -> None:
        if left == right:
            v = newVal % self.k
            self.prod[idx] = v
            c = [0] * self.k
            c[v] = 1
            self.cnt[idx] = c
        else:
            mid = (left + right) // 2
            if pos <= mid:
                self.update(idx * 2, left, mid, pos, newVal)
            else:
                self.update(idx * 2 + 1, mid + 1, right, pos, newVal)

            self.recalcNode(idx)

    def mergeNodes(self, leftNode, rightNode):
        if leftNode is None:
            return rightNode
        if rightNode is None:
            return leftNode

        prodL, cntL = leftNode
        prodR, cntR = rightNode
        combinedProd = (prodL * prodR) % self.k

        cNew = [0] * self.k
        for r in range(self.k):
            cNew[r] += cntL[r]

        for y in range(self.k):
            freq = cntR[y]
            if freq:
                rnew = (prodL * y) % self.k
                cNew[rnew] += freq

        return (combinedProd, cNew)

    def query(self, idx: int, left: int, right: int, ql: int, qr: int):
        if qr < left or ql > right:
            return None
        if ql <= left and right <= qr:
            return (self.prod[idx], self.cnt[idx])

        mid = (left + right) // 2
        leftRes = self.query(idx * 2, left, mid, ql, qr)
        rightRes = self.query(idx * 2 + 1, mid + 1, right, ql, qr)
        return self.mergeNodes(leftRes, rightRes)

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of subarrays starting from a given index whose product modulo k is equal to x,
        after applying a series of updates to the initial array.

        Args:
            nums: The initial array of integers.
            k: The modulus.
            queries: A list of queries, where each query is [idx, newVal, start, x].

        Returns:
            A list of integers, where each element is the answer to the corresponding query.
        """
        n = len(nums)
        # Build an array of nums[i] % k
        arrMod = [v % k for v in nums]
        st = SegmentTree(arrMod, k)

        answer = []
        for (idx, newVal, start, x) in queries:
            # Update the tree in O(log (n.k))
            st.update(1, 0, n - 1, idx, newVal % k)

            # We want exactly the subarray [start...(n - 1)]
            if start >= n:
                # If start is beyond the last index, there is no "non-empty" left-over, so answer = 0.
                answer.append(0)
            else:
                node = st.query(1, 0, n - 1, start, n - 1)
                # node == (prod_subarray, cnt_list). We only need cnt_list[x].
                if node is None:
                    answer.append(0)
                else:
                    (_, cntList) = node
                    answer.append(cntList[x])

        return answer