# Leetcode 3245: Alternating Groups III
# https://leetcode.com/problems/alternating-groups-iii/
# Solved on 25th of November, 2025
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of alternating groups of a certain minimum size after a series of color updates.

        Args:
            colors: A list of integers representing the initial colors of the groups.
            queries: A list of queries, where each query is either a type 1 query (calculate alternating groups of size sz) or a type 2 query (update color at index idx to col).
        Returns:
            A list of integers, where each element is the answer to a type 1 query.
        """
        n = len(colors)

        bit_cnt = [0] * (n + 1)
        bit_sum = [0] * (n + 1)

        def bit_add(bit, idx, val):
            i = idx
            while i <= n:
                bit[i] += val
                i += i & (-i)

        def bit_query(bit, idx):
            s = 0
            i = idx
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        def add_len(l):
            bit_add(bit_cnt, l, 1)
            bit_add(bit_sum, l, l)

        def remove_len(l):
            bit_add(bit_cnt, l, -1)
            bit_add(bit_sum, l, -l)

        tree_n = 1
        while tree_n <= n:
            tree_n *= 2
        tree = [0] * (2 * tree_n)

        def st_update(idx, val):
            pos = idx + tree_n
            if tree[pos] == val: return
            tree[pos] = val
            while pos > 1:
                pos //= 2
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

        def get_prev(idx):
            pos = idx + tree_n
            curr = pos
            found = False
            while curr > 1:
                if curr % 2 == 1:
                    if tree[curr - 1] > 0:
                        curr -= 1
                        found = True
                        break
                curr //= 2
            if found:
                while curr < tree_n:
                    curr *= 2
                    if tree[curr + 1] > 0:
                        curr += 1
                return curr - tree_n
            if tree[1] > 0:
                curr = 1
                while curr < tree_n:
                    curr *= 2
                    if tree[curr + 1] > 0: curr += 1
                return curr - tree_n
            return -1

        def get_next(idx):
            pos = idx + tree_n
            curr = pos
            found = False
            while curr > 1:
                if curr % 2 == 0:
                    if tree[curr + 1] > 0:
                        curr += 1
                        found = True
                        break
                curr //= 2
            if found:
                while curr < tree_n:
                    curr *= 2
                    if tree[curr] == 0:
                        curr += 1
                return curr - tree_n
            if tree[1] > 0:
                curr = 1
                while curr < tree_n:
                    curr *= 2
                    if tree[curr] == 0:
                        curr += 1
                return curr - tree_n
            return -1

        bad_indices = []
        for i in range(n):
            if colors[i] == colors[(i + 1) % n]:
                bad_indices.append(i)
                st_update(i, 1)

        if not bad_indices:
            pass
        else:
            m = len(bad_indices)
            for i in range(m):
                curr = bad_indices[i]
                nxt = bad_indices[(i + 1) % m]
                length = (nxt - curr) % n
                if length == 0:
                    length = n
                add_len(length)

        res = []

        for q in queries:
            if q[0] == 1:
                sz = q[1]
                if tree[1] == 0:
                    res.append(n if n >= sz else 0)
                else:
                    cnt = bit_query(bit_cnt, n) - bit_query(bit_cnt, sz - 1)
                    sm = bit_query(bit_sum, n) - bit_query(bit_sum, sz - 1)
                    res.append(sm - cnt * (sz - 1))
            else:
                idx, col = q[1], q[2]
                if colors[idx] == col:
                    continue
                colors[idx] = col

                for edge_idx in [(idx - 1) % n, idx]:
                    is_bad = (colors[edge_idx] == colors[(edge_idx + 1) % n])
                    was_bad = (tree[edge_idx + tree_n] == 1)

                    if is_bad == was_bad:
                        continue

                    if is_bad:
                        if tree[1] == 0:
                            add_len(n)
                        else:
                            p = get_prev(edge_idx)
                            nxt = get_next(edge_idx)
                            old_l = (nxt - p) % n
                            if old_l == 0:
                                old_l = n
                            remove_len(old_l)
                            l1 = (edge_idx - p) % n
                            if l1 == 0:
                                l1 = n
                            l2 = (nxt - edge_idx) % n
                            if l2 == 0:
                                l2 = n
                            add_len(l1)
                            add_len(l2)
                        st_update(edge_idx, 1)
                    else:
                        st_update(edge_idx, 0)
                        if tree[1] == 0:
                            remove_len(n)
                        else:
                            p = get_prev(edge_idx)
                            nxt = get_next(edge_idx)
                            l1 = (edge_idx - p) % n
                            if l1 == 0:
                                l1 = n
                            l2 = (nxt - edge_idx) % n
                            if l2 == 0:
                                l2 = n
                            remove_len(l1)
                            remove_len(l2)
                            new_l = (nxt - p) % n
                            if new_l == 0:
                                new_l = n
                            add_len(new_l)

        return res
