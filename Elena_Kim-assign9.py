#Elena Kim
#assignment 9
#CS 51 
#3/5/2019

#This assignment finds the number of solutions to the n queens problem
#for and 8x8 board and gives an example of a solution



import copy 

class NQueenState:
    """This class keeps track of the chess board and is able to update it
    with queens placed on the board"""
    
    def __init__(self, size):
        """Takes the size of the side of the board as a parameter and 
        constructs a new state that is a board with no queens placed."""
        
        self.size=size
        self.num_queens_placed=0
        self.board=[]
        for i in range(0, size):
            self.board.append([0]*size)  #bulds size x size matrix of zeros
    
    
    def __str__(self):
        """Returns a string representation of the board."""
        
        board=""
        for row in self.board:       #board with a list per row but no
            board+= str(row) + "\n"  #brackets on the very ends
        
        str1= "Board size: " + str(self.size) 
        str2= "Number of queens placed: " + str(self.num_queens_placed)
        
        return str1 + "\n"  + str2  + "\n" + board 
    
    
    def check_entry(self, row, column):
        """Checks to see if a queen is already in the entry"""
        
        return self.board[row][column] == 0
    
    
    def check_row(self, row):
        """Checks to see if a queen is already in the row"""
        
        return 1 not in self.board[row] 
    
    
    def check_column(self, column):
        """Checks to see if the queen is already in the column"""
        
        for i in range(self.size):
            if self.board[i][column]:
                return False
        
        return True
      
      
    def check_number_queens(self):
        """Checks to make sure the number of queens already placed is less than 
        the size of the board"""
        
        return self.num_queens_placed < self.size
    
    
    def is_part_of_board(self, row, column):
        """Helps the check_diagonals function to check if a entry is a valid
        part of the baord"""
        
        return row in range(self.size) and column in range(self.size)
    
    
    def check_diagonals(self, row, column):
        """Checks to see if a queen is already in the diagonal"""
        
        for i in range(-row, row):
            if self.is_part_of_board(row+i,column+i) and \
               1 == self.board[row+i][column+i]:    #checks main diagonal
                return False

        for i in range(-row, row):
            if self.is_part_of_board(row+i,column-i) and \
               1 == self.board[row+i][column-i]:   #checks other diagonal
                return False
        
        return True
    
    
    def is_valid_move(self, row, column):
        """Returns True if putting a queen at row, col on this board would 
        result in a valid state"""
        
        if self.check_number_queens() and \
        self.check_entry(row, column) and \
        self.check_row(row) and \
        self.check_column(column) and \
        self.check_diagonals(row, column):
            return True  #true if queen is valid
        else:
            return False  #false if queen is not valid
        
    
    def add_queen(self, row, column):
        """Takes row and column as parameters and returns a new state 
        that is a copy of the current state, but has the queen put down at 
        row, col"""
        
        new_state=copy.deepcopy(self)
        new_state.board[row][column]=1  #changes copied board to add queen
        new_state.num_queens_placed+=1  #increases count of queens placed
        return new_state    
    
    
    def next_states(self):
        """Returns a list of valid states that can be reached by adding
        one more queen to the board."""
        
        next_states_list=[]
        
        for i in range(0, self.size):            
            if self.is_valid_move(self.num_queens_placed, i):
                next_states_list.append\
                    (self.add_queen(self.num_queens_placed, i)) #adds queen to 
                                                 #board only if quenn is valid
        return next_states_list
    
    
    def is_goal(self):
        """True if this state represents a goal state and False otherwise"""
        
        return self.num_queens_placed == self.size
        
        
def dfs(state):
    """Recursive depth first search implementation
    
    Input:
    Takes as input a state.  The state class MUST have the following
    returned True) that can be reached from the input state.
    """
    
    #if the current state is a goal state, then return it in a list
    if state.is_goal():
        return [state]
    else:
        # else, recurse on the possible next states
        result = []
        
        for s in state.next_states():
            # append all of the s
            result += dfs(s)
            
        return result
    
start_state = NQueenState(8)

solutions = dfs(start_state)
print("There were " + str(len(solutions)) + " solutions.\n")

if( len(solutions) > 0 ):
    print(solutions[0])