
 
def single_game(cur_player):
 
    values = [' ' for x in range(9)]
     
    player_pos = {'X':[], 'O':[]}
     
    while True:
        print_tic_tac_toe(values)
         
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
 
        values[move-1] = cur_player
 
        player_pos[cur_player].append(move)
 
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the Player 1 name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the Player 2 name : ")
    print("\n")
     
    cur_player = player1
 
    player_choice = {'X' : "", 'O' : ""}
 
    options = ['X', 'O']
 
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    while True:
 
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
 
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice! Try Again\n")
 
        winner = single_game(options[choice-1])
         
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
