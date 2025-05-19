# Leetcode 1728: Cat and Mouse II
# https://leetcode.com/problems/cat-and-mouse-ii/
# Solved on 19th of May, 2025

class Solution:
    MOUSE_WINS = 0
    CAT_WINS = 1

    grid_rows, grid_cols = 0, 0
    game_grid = None
    cat_jump_len, mouse_jump_len = 0, 0
    food_loc = None
    memo_cache = {}
    cardinal_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    MAX_PLY_IN_STATE_heuristic = 0
    ABSOLUTE_TIMEOUT_PLIES = 1000   # Max plies from problem

    def _get_valid_moves(self, r_start: int, c_start: int, jump_ability: int, is_mouse_moving: bool, other_player_pos: tuple[int, int]) -> list[tuple[int, int]]:

        # Use set to avoid duplicates easily
        possible_next_pos_set = set()

        for dr, dc in self.cardinal_dirs:
            for dist in range(1, jump_ability + 1):
                path_valid = True
                dest_r_final, dest_c_final = -1, -1 # Store final destination of this jump

                for step in range(1, dist + 1):
                    inter_r, inter_c = r_start + dr * step, c_start + dc * step

                    if not(0 <= inter_r < self.grid_rows and 0 <= inter_c < self.grid_cols):
                        path_valid = False
                        break
                    if self.game_grid[inter_r][inter_c] == '#':
                        path_valid = False
                        break

                    if not is_mouse_moving and (inter_r, inter_c) == other_player_pos and step < dist:
                        path_valid = False
                        break

                    if step == dist:    # This is the destination cell for current jump length `dist`
                        dest_r_final, dest_c_final = inter_r, inter_c

                if not path_valid:
                    break

                if dest_r_final != -1:  # Ensure destination was actually determined
                    possible_next_pos_set.add((dest_r_final, dest_c_final))

        return list(possible_next_pos_set)

    def _solve_recursive(self, mouse_pos: tuple[int, int], cat_pos: tuple[int, int], current_player_turn: int, total_plies_made: int) -> int:

        memo_ply = min(total_plies_made, self.MAX_PLY_IN_STATE_heuristic)
        state_key = (mouse_pos, cat_pos, current_player_turn, memo_ply)

        if state_key in self.memo_cache:
            return self.memo_cache[state_key]

        if mouse_pos == self.food_loc:
            self.memo_cache[state_key] = self.MOUSE_WINS
            return self.MOUSE_WINS

        if cat_pos == self.food_loc:
            self.memo_cache[state_key] = self.CAT_WINS
            return self.CAT_WINS

        if cat_pos == mouse_pos:
            self.memo_cache[state_key] = self.CAT_WINS
            return self.CAT_WINS

        if total_plies_made >= self.ABSOLUTE_TIMEOUT_PLIES:
            self.memo_cache[state_key] = self.CAT_WINS
            return self.CAT_WINS

        # Heuristic: If plies exceed MAX_PLY_IN_STATE_heuristic, assume it leads to ABSOLUTE_TIMEOUT
        # This prunes search for very long games IF this heuristic is smaller than ABSOLUTE_TIMEOUT
        if ((total_plies_made >= self.MAX_PLY_IN_STATE_heuristic) and (self.MAX_PLY_IN_STATE_heuristic < self.ABSOLUTE_TIMEOUT_PLIES)):
            self.memo_cache[state_key] = self.CAT_WINS
            return self.CAT_WINS

        if current_player_turn == 0:    # Mouse's turn
            valid_mouse_moves = self._get_valid_moves(mouse_pos[0], mouse_pos[1], self.mouse_jump_len, True, cat_pos)

            # If stay is always an option, this list should not be empty unless grid is 1x1 and M is on F/C.
            # The problem guarantees distinct M,C,F, and R,C>=1. Min cells = 3.
            # An empty valid_mouse_moves implies mouse is completely blocked, even from staying.
            # This seems unlikely with "stay" allowed unless some edge case in _get_valid_moves.
            # If truly no moves (e.g., if "stay" was conditional), it would be Cat Win.
            # Given "stay" rule, this means no valid moves only if current state is already game-ending.
            # The base cases should catch this.
            for next_m_pos in valid_mouse_moves:
                if self._solve_recursive(next_m_pos, cat_pos, 1, total_plies_made + 1) == self.MOUSE_WINS:
                    self.memo_cache[state_key] = self.MOUSE_WINS
                    return self.MOUSE_WINS
            self.memo_cache[state_key] = self.CAT_WINS
            return self.CAT_WINS

        else:   # Cat's turn
            valid_cat_moves = self._get_valid_moves(cat_pos[0], cat_pos[1], self.cat_jump_len, False, mouse_pos)
            # Cat is trapped (unlikely with "stay")
            if not valid_cat_moves:
                # If cat is trapped, mouse plays next
                outcome = self._solve_recursive(mouse_pos, cat_pos, 0, total_plies_made + 1)
                self.memo_cache[state_key] = outcome
                return outcome

            for next_c_pos in valid_cat_moves:
                if self._solve_recursive(mouse_pos, next_c_pos, 0, total_plies_made + 1) == self.CAT_WINS:
                    self.memo_cache[state_key] = self.CAT_WINS
                    return self.CAT_WINS
            self.memo_cache[state_key] = self.MOUSE_WINS
            return self.MOUSE_WINS

    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        """
        Determines if the mouse can win the game given the grid, cat's jump length, and mouse's jump length.

        Args: grid: A list of strings representing the game grid. 'M' for mouse, 'C' for cat, 'F' for food,
        '#' for obstacle, '.' for empty cell.
        catJump: The maximum jump length of the cat.
        mouseJump: The maximum jump length of the mouse.

        Returns:
            True if the mouse can win, False otherwise.
        """
        self.grid_rows = len(grid)
        self.grid_cols = len(grid[0])
        self.game_grid = grid
        self.cat_jump_len = catJump
        self.mouse_jump_len = mouseJump
        self.memo_cache.clear()

        # Set heuristic depth for memoization state
        # Effective game states may repeat configuration before this many plies, leading to timeout.
        # Typically 2 * R * C is used. Let's use that and cap it.
        calculated_heuristic_depth = 2 * self.grid_rows * self.grid_cols
        # Ensure a minimum reasonable depth for small grids (e.g., for 1x3, 2*3=6, too small)
        # Max grid size is 8x8 -> 2*64 = 128.
        # A floor like 70-80 might be reasonable if problem has tricky short cycles.
        # Let's use a simple minimum, e.g., 50, or scale by grid size e.g. 8 * (R+C)
        min_heuristic_depth = 2 * (self.grid_rows + self.grid_cols) * 2
        if min_heuristic_depth < 30:
            min_heuristic_depth = 30    # Absolute floor

        self.MAX_PLY_IN_STATE_heuristic = max(calculated_heuristic_depth, min_heuristic_depth)
        if self.MAX_PLY_IN_STATE_heuristic > self.ABSOLUTE_TIMEOUT_PLIES:   # Cannot exceed actual timeout
            self.MAX_PLY_IN_STATE_heuristic = self.ABSOLUTE_TIMEOUT_PLIES
        # This chosen MAX_PLY_IN_STATE_heuristic for 8x8 grid is 128 (from 2*R*C). min_heuristic_depth = 2*(8+8)*2 =
        # 64. So 128.

        initial_mouse_pos, initial_cat_pos = None, None
        temp_food_loc = None
        for r_idx in range(self.grid_rows):
            for c_idx in range(self.grid_cols):
                if grid[r_idx][c_idx] == 'M':
                    initial_mouse_pos = (r_idx, c_idx)
                elif grid[r_idx][c_idx] == 'C':
                    initial_cat_pos = (r_idx, c_idx)
                elif grid[r_idx][c_idx] == 'F':
                    temp_food_loc = (r_idx, c_idx)
        self.food_loc = temp_food_loc

        if not initial_mouse_pos or not initial_cat_pos or not self.food_loc:
            return False

        final_outcome = self._solve_recursive(initial_mouse_pos, initial_cat_pos, 0, 0)
        return final_outcome == self.MOUSE_WINS