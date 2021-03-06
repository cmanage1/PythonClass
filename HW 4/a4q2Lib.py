# X COLUMN --> checked
# O COLUMN --> checked
# X ROW --> checked
# O ROW --> checked
# left_to_right diag --> check
# right_to_left diag --> check


def eraseTable (tab):
   '''
   (list) -> None
   This function prepares the game table (array)
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''
   for i in range (len(tab)):
       for j in range(len(tab[0])):
           tab[i][j]= '-'
    # returns nothing


def verifyWin(tab):
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won"
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    Col = testCols(tab)
    Row = testRows(tab)
    Diag = testDiags(tab)

    if Col == 'X' or Row == 'X' or Diag == 'X':
        print("Player X has won!")
        return True
    elif Col == 'O' or Row == 'O' or Diag == 'O':
        print("Player O has won!")
        return True
    elif testDraw(tab) == True:
        print("Draw")
        return True
    else:
        return False

def testRows(tab):
   ''' (list) ->  str
   * verify if there is a winning row.
   * Look for three 'X' or three 'O' in a row.
   * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for i in tab :
        if i == ['X', 'X', 'X']:
           return 'X'
        elif i == ['O', 'O', 'O']:
           return 'O'
   return '-'

   # to complete
   # to be modified so that it returns the winner, or '-' if there is no winner

def testCols(tab):
   ''' (list) ->  str
   * verify a winning column.
   * look for three 'X' or three 'O' in a column.
   * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for i in range (len (tab )) :
       col = []
       for j in range (len (tab[0])):
            col.append(tab[j][i])
       if col == ['X', 'X', 'X']:
           return 'X'
       elif col == ['O', 'O' , 'O']:
           return 'O'
   return '-'


def testDiags(tab):
   ''' (list) ->  str
   * Look for three 'X' or three 'O' in a diagonal.
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''

   Xcount = 0
   Ocount = 0

   for i in range ( len(tab) ):
       for j in range ( len(tab[0])):
           if i == j:
               if tab[i][j] == 'X':
                   Xcount +=1
               elif tab[i][j] == 'O':
                   Ocount +=1
       if Xcount ==3:
            return 'X'
       if Ocount ==3:
            return 'O'

   Xcount = 0
   Ocount = 0

   for i in range ( len(tab) ):
       if i == 0:
            if tab[i][2] == 'X':
                Xcount+=1
            elif tab[i][2] == 'O':
                Ocount+=1
       elif i == 1:
           if tab[i][1] == 'X':
               Xcount+=1
           elif tab[i][1] == 'O':
               Ocount+=1
       elif i == 2:
           if tab[i][0] == 'X':
               Xcount+=1
           elif tab[i][0] == 'O':
               Ocount+=1
       if Xcount ==3:
           return 'X'
       if Ocount ==3:
           return 'O'

   return '-'   # #to be modified so that it returns the winner, or '-' if there is no winner
   # to complete


def testDraw(tab):
   ''' (list) ->  bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.
   * If we do not find find any '-' in the array, return True.
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for i in tab:
       for j in i:
           if j == '-':
               return False
   return True
