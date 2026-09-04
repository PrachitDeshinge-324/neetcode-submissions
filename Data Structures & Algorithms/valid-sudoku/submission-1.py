class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isvalidrow(row):
            temp = {}
            for i in row:
                temp[i] = temp.get(i,0) + 1
                if temp[i] > 1 and i != '.':
                    return False
            return True

        def vaildsub(sub):
            temp = {}
            for i in range(0,3):
                for j in range(0,3):
                    temp[sub[i][j]] = temp.get(sub[i][j],0) + 1;
                    if temp[sub[i][j]] > 1 and sub[i][j] != '.':
                        return False
            return True

        for i in range(0,len(board)):
            temp = board[i][:]
            if isvalidrow(temp) == False:
                return False
                
        for i in range(0,len(board)):
            column = [row[i] for row in board]
            if isvalidrow(column) == False:
                return False

        for i in range(0,3):
            for j in range(0,3):
                sub = [row[j*3:(j+1)*3] for row in board[i*3:(i+1)*3]]
                if vaildsub(sub) == False:
                    return False
        return True