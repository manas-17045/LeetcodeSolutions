# Leetcode 3636: Threshold Majority Queries
# https://leetcode.com/problems/threshold-majority-queries/
# Solved on 24th of November, 2025
import math


class Solution:
    def subarrayMajority(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Finds the majority element within specified subarrays for multiple queries.
        A majority element is defined as an element that appears at least 'threshold' times.

        Args:
            nums: A list of integers representing the main array.
            queries: A list of queries, where each query is [left, right, threshold].

        Returns:
            A list of integers, where each element is the majority element for the corresponding query, or -1 if no such element exists.
        """
        n = len(nums)

        # Coordinate Compression
        sorted_vals = sorted(list(set(nums)))
        val_map = {v: i for i, v in enumerate(sorted_vals)}
        inv_map = sorted_vals
        m = len(sorted_vals)
        mapped_nums = [val_map[x] for x in nums]

        # Mo's Algorithm Setup
        q_count = len(queries)
        block_size = int(n / math.sqrt(q_count)) + 1

        indexed_queries = []
        for i in range(q_count):
            indexed_queries.append((queries[i][0], queries[i][1], queries[i][2], i))

        # Sort queries to minimize pointer movement
        indexed_queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))

        # Data Structures
        cnt = [0] * m
        freq_cnt = [0] * (n + 1)

        val_block_size = int(math.sqrt(m)) + 1
        num_val_blocks = (m // val_block_size) + 1
        val_blocks = [[0] * (n + 1) for _ in range(num_val_blocks)]

        max_freq = 0
        l, r = 0, -1
        ans = [0] * q_count

        for ql, qr, qt, q_idx in indexed_queries:
            while r < qr:
                r += 1
                val = mapped_nums[r]
                old_f = cnt[val]

                if old_f > 0:
                    freq_cnt[old_f] -= 1
                    val_blocks[val // val_block_size][old_f] -= 1

                new_f = old_f + 1
                cnt[val] = new_f
                freq_cnt[new_f] += 1
                val_blocks[val // val_block_size][new_f] += 1

                if new_f > max_freq:
                    max_freq = new_f

            while r > qr:
                val = mapped_nums[r]
                old_f = cnt[val]

                freq_cnt[old_f] -= 1
                val_blocks[val // val_block_size][old_f] -= 1

                new_f = old_f - 1
                cnt[val] = new_f

                if new_f > 0:
                    freq_cnt[new_f] += 1
                    val_blocks[val // val_block_size][new_f] += 1

                if freq_cnt[max_freq] == 0:
                    max_freq -= 1
                r -= 1

            while l < ql:
                val = mapped_nums[l]
                old_f = cnt[val]

                freq_cnt[old_f] -= 1
                val_blocks[val // val_block_size][old_f] -= 1

                new_f = old_f - 1
                cnt[val] = new_f

                if new_f > 0:
                    freq_cnt[new_f] += 1
                    val_blocks[val // val_block_size][new_f] += 1

                if freq_cnt[max_freq] == 0:
                    max_freq -= 1
                l += 1

            while l > ql:
                l -= 1
                val = mapped_nums[l]
                old_f = cnt[val]

                if old_f > 0:
                    freq_cnt[old_f] -= 1
                    val_blocks[val // val_block_size][old_f] -= 1

                new_f = old_f + 1
                cnt[val] = new_f
                freq_cnt[new_f] += 1
                val_blocks[val // val_block_size][new_f] += 1

                if new_f > max_freq:
                    max_freq = new_f

            # Calculate Answer
            if max_freq < qt:
                ans[q_idx] = -1
            else:
                found_val = -1
                for b in range(num_val_blocks):
                    if val_blocks[b][max_freq] > 0:
                        start = b * val_block_size
                        end = min(start + val_block_size, m)
                        for v_check in range(start, end):
                            if cnt[v_check] == max_freq:
                                found_val = inv_map[v_check]
                                break
                        if found_val != -1:
                            break
                ans[q_idx] = found_val

        return ans