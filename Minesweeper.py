class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if len(board) == 0:
            return board
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)] # U D L R UR UL LR LL
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        def countMines(board, click):
            count = 0
            for dir1 in dirs:
                nr = click[0] + dir1[0]
                nc = click[1] + dir1[1]
                if m > nr >= 0  and n > nc>= 0 and board[nr][nc] == "M":
                    count = count + 1
            return count
        def dfs(board, click):
            #base
            if not (0 <= click[0] < m and 0 <= click[1] < n) or board[click[0]][click[1]] != "E":
                return 
            #logic
            mines_count = countMines(board,click) # check if neighbours have mines
            if mines_count == 0:
                board[click[0]][click[1]] = "B"
                for dir1 in dirs:
                    nr = click[0] + dir1[0]
                    nc = click[1] + dir1[1]
                    dfs(board, [nr, nc])
            else:
                board[click[0]][click[1]] = str(mines_count)

        dfs(board,click)
        return board

    # TC : O(mn)
    # SC : O(mn)