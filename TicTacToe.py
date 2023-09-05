def TTT():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win= ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def choice():
        while True:
            
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("invalid")
                        continue
                except Error:
                   print("invalid")
                   continue
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def player1():
        n = choice()
        if board[n] == "X" or board[n] == "O":
            print("invalid")
            player1()
        else:
            board[n] = "X"

    def player2():
        n = choice()
        if board[n] == "X" or board[n] == "O":
            print("invalid")
            player2()
        else:
            board[n] = "O"

    
    def check_board():
        count = 0
        for a in win:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins")
                
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins")
                
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("tie")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1")
        player1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2")
        player2()
        print()
TTT()