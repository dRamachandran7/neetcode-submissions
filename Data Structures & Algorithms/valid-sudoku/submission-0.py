class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_in_rows = [set() for _ in range(9)]
        seen_in_cols = [set() for _ in range(9)]
        seen_in_box = [set() for _ in range (9)]

        # go through rows and cols check everything

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                box_idx = (i // 3) * 3 + (j // 3)
                if val == ".":
                    continue
                
                if (val in seen_in_rows[i] or 
                    val in seen_in_cols[j] or
                    val in seen_in_box[box_idx]):
                    return False
                
                seen_in_rows[i].add(val)
                seen_in_cols[j].add(val)
                seen_in_box[box_idx].add(val)
        
        return True




        