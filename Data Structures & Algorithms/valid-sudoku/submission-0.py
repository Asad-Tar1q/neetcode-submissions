class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = [[] for i in range(9)]
        rows = [[] for i in range(9)]
        cells = [[] for i in range(9)]

        n = len(board)



        for i in range(n):
            for j in range(n):
                d = board[i][j]
                cell_row = i//3
                cell_col = j//3

                if cell_row == 0:
                    cell = cell_col
                if cell_row == 1:
                    cell = 3 + cell_col
                if cell_row == 2:
                    cell = 6 + cell_col
 
                if d != ".":
                    if d in rows[i] or d in cols[j] or d in cells[cell]:
                        print(i,j)
                        return False
                    

                    
                    cols[j].append(d)
                    rows[i].append(d)
                    cells[cell].append(d)
                print(f"cells : {cells}")
                print(f"rows: {rows}")
                print(f"columns: {cols}")
        
        return True
                
            
        