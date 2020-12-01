# Chess Dictionary Validator
# Function that takes a dict argument and returns True or False if dict represents a valid chess board.
# A valid board will have:
  # One black king and one white king. 
  # Each player can only have at most 16 pieces, at most 8 pawns 
  # Pieces must be on a valid space from '1a' to '8h' 
  # names begin with either a 'w' or 'b' followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

def isValidChessBoard(dict):
    bking = 0
    wking = 0
    bpiece = 0
    wpiece = 0
    wpawn = 0
    bpawn = 0

    validNumbers = ['1','2','3','4','5','6','7','8']
    validLetters = ['a','b','c','d','e','f','g','h']
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for keys,values in dict.items():
      if dict[keys] != '' and len(keys) == 2:
        if dict[keys] == 'bking':
          bking += 1 
        if dict[keys] == 'wking':
          wking += 1 
        # Triple check for correct elements based on letters, numbers and pieces arrays
        if keys[0] in validLetters and keys[1] in validNumbers and  dict[keys][1:] in validPieces:
          if dict[keys][0] == 'w':
            wpiece +=1
            if dict[keys][1:] == 'pawn':
              wpawn += 1
          elif dict[keys][0] == 'b':
            bpiece +=1
            if dict[keys][1:] == 'pawn':
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

    
# Example boards        
print(isValidChessBoard({"h1": "bking", "c6": "wqueen", "g2": "bbishop", "h5": "bqueen", "e3": "wking"}))  # True
print(isValidChessBoard({"a1": "bpawn", "a2": "wking"}))  # False: no bking
print(isValidChessBoard({"a1": "bpawn", "a2": "wking","a4":"bking"})) # True
print(isValidChessBoard({"a1": "wking", "a2": "wking", "3c": "bbishop"}))  #False: Cannot have 2 white kings

