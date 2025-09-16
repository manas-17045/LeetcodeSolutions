# Leetcode 1659: Maximize Grid Happiness
# https://leetcode.com/problems/maximize-grid-happiness/
# Solved on 16th of September, 2025
from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        """
        Calculates the maximum grid happiness achievable by placing introverts and extroverts.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            introvertsCount (int): The total number of introverts available.
            extrovertsCount (int): The total number of extroverts available.
        Returns:
            int: The maximum grid happiness.
        """

        # Precompute
        max_mask = 3 ** n

        # helper pair interaction for adjacent occupied cells (sum of both people's delta)
        # (1=introvert, 2=extrovert)
        pair_effect = {
            (1, 1): -60,  # -30 + -30
            (1, 2): -10,  # -30 + 20
            (2, 1): -10,
            (2, 2): 40  # 20 + 20
        }

        mask_cells = [None] * max_mask
        mask_intro = [0] * max_mask
        mask_extra = [0] * max_mask
        intra_hap = [0] * max_mask  # base happiness + horizontal adjacency

        for mask in range(max_mask):
            tmp = mask
            cells = [0] * n
            for j in range(n):
                cells[j] = tmp % 3
                tmp //= 3
            mask_cells[mask] = cells

            hap = 0
            icnt = 0
            ecnt = 0
            # Base happiness per person and horizontal adjacency effect
            for j in range(n):
                v = cells[j]
                if v == 1:
                    hap += 120
                    icnt += 1
                elif v == 2:
                    hap += 40
                    ecnt += 1
                # Horizontal neighbor to the left (only once per pair)
                if j > 0:
                    left = cells[j - 1]
                    if left != 0 and v != 0:
                        hap += pair_effect[(left, v)]
            mask_intro[mask] = icnt
            mask_extra[mask] = ecnt
            intra_hap[mask] = hap

        # Vertical interaction between two row masks
        inter_hap = [[0] * max_mask for _ in range(max_mask)]
        for a in range(max_mask):
            ca = mask_cells[a]
            for b in range(max_mask):
                cb = mask_cells[b]
                s = 0
                for j in range(n):
                    if ca[j] != 0 and cb[j] != 0:
                        s += pair_effect[(ca[j], cb[j])]
                inter_hap[a][b] = s

        @lru_cache(None)
        def dp(row: int, prev_mask: int, i_left: int, e_left: int) -> int:
            if row == m:
                return 0
            best = -10 ** 9
            # Try every possible current-row mask
            for cur in range(max_mask):
                ic = mask_intro[cur]
                ec = mask_extra[cur]
                if ic > i_left or ec > e_left:
                    continue
                cur_score = intra_hap[cur] + inter_hap[cur][prev_mask]
                total = cur_score + dp(row + 1, cur, i_left - ic, e_left - ec)
                if total > best:
                    best = total
            return best

        return dp(0, 0, introvertsCount, extrovertsCount)