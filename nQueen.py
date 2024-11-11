def isSafe(board , row , col , n):
    for i in range(col):
        if board[row][i]==1:
            return False
        
    i = row
    j = col
    while i >=0 and j >=0:
        if board[i][j] ==1:
            return False
        
        i-=1
        j-=1    

    i = row
    j = col
    while i <n and j >=0:
        if board[i][j] ==1:
            return False
        
        i+=1
        j-=1
    return True


def printQueen(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j] , end=' ')
        print()  

def solveQueen(board , col , n):
    if col == n :
        return True
    
    for i in range(n):
        if isSafe(board , i , col , n):
            board[i][col] =1

            if solveQueen(board , col+1 , n):
                return True
            board[i][col] = 0
    return False

def nQueen(n):
    board = [[0 for i in range (n)] for i in range (n)]

    if not solveQueen(board , 0 , n):
        print('Not Found')
        return False
    printQueen(board , n)


n = 4 
nQueen(n)