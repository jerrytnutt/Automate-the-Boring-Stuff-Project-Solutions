# Chess Dictionary Validator
# Function that returns True or False if argument represents a valid chess board.
# A valid board will have:
  # One black king and one white king. 
  # Each player can only have at most 16 pieces, and at most 8 pawns 
  # Pieces must be on a valid space from '1a' to '8h' 
  # Names begin with either a 'w' or 'b' followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

def is_valid_chess_board(board):
    bking = 0
    wking = 0
    bpiece = 0
    wpiece = 0
    wpawn = 0
    bpawn = 0

    valid_numbers = ['1','2','3','4','5','6','7','8']
    valid_letters = ['a','b','c','d','e','f','g','h']
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for keys,values in board.items():
      if board[keys] != '' and len(keys) == 2:
        if board[keys] == 'bking':
          bking += 1 
        if board[keys] == 'wking':
          wking += 1 
        # Triple check for correct elements based on letters, numbers and pieces arrays
        if keys[0] in valid_letters and keys[1] in valid_numbers and  board[keys][1:] in valid_pieces:
          if board[keys][0] == 'w':
            wpiece +=1
            if board[keys][1:] == 'pawn':
              wpawn += 1
          elif board[keys][0] == 'b':
            bpiece +=1
            if board[keys][1:] == 'pawn':
              bpawn += 1
          else:
            return False
        else:
          return False
    if bking != 1 or wking != 1:
      return False
    if bpiece > 16 or wpiece > 16:
      return False 
    if bpawn > 8 or wpawn > 8:
      return False
    return True

if __name__ == '__main__':
  # Test boards        
  print(is_valid_chess_board({"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking"}))  # True
  print(is_valid_chess_board({"a1": "bpawn", "a2": "wking"}))  # False: no bking
  print(is_valid_chess_board({"a1": "bpawn", "a2": "wking","a4":"bking"})) # True
  print(is_valid_chess_board({"a1": "wking", "a2": "wking", "3c": "bbishop"}))  #False: Cannot have 2 white kings