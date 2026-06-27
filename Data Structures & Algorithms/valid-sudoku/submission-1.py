class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = []

        for i in board:
            checker = {'1': 0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for j in i:
                if j in checker.keys():
                    checker[j] += 1
                    if checker[j] > 1:
                        return False
        for i in range(9):
            checker = {'1': 0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for j in board:
                if j[i] in checker.keys():
                    checker[j[i]] += 1
                    if checker[j[i]] > 1:
                        return False
        
        row_start = 0
        row_end = 3
        column_start = 0
        column_end = 3

        while row_end != 9:
            while column_end != 9:
                checker = {'1': 0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
                for i in board[row_start:row_end]:
                    for j in i[column_start:column_end]:
                        if j in checker.keys():
                            checker[j] += 1
                            if checker[j] > 1:
                                return False
                column_start += 3
                column_end += 3
            row_start += 3
            row_end += 3
            column_start = 0
            column_end = 3
        
        return True
            



        

            

        

        