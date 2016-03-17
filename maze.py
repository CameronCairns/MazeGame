import pdb

class Maze:
    
    def __init__(self, dimensions=30):
        # Constructs a grid full of walls
        self.grid = [[Node(row, column) for column in range(dimensions)] for row in range(dimensions)]
        visited_nodes = [self.grid[0][0]]
        while len(visited_nodes) > 0:
            current_node = visited_nodes.pop()
            row_index, col_index = current_node.coordinates
            # Check Top
            if 0 <= row_index - 1 < dimensions:
                top = self.grid[row_index-1][col_index]
                if top.visited == False:
                    top.visited = True
                    top.wall_bottom = False
                    visited_nodes.append(top)
            # Check Bottom
            if 0 <= row_index + 1 < dimensions:
                bottom = self.grid[row_index+1][col_index]
                if bottom.visited == False:
                    bottom.visited = True
                    current_node.wall_bottom = False
                    visited_nodes.append(bottom)
            # Check Right
            if 0 <= col_index - 1 < dimensions:
                right = self.grid[row_index][col_index-1]
                if right.visited == False:
                    right.visited = True
                    right.wall_left = False
                    visited_nodes.append(right)
            # Check Left
            if 0 <= col_index + 1 < dimensions:
                left = self.grid[row_index][col_index+1]
                if left.visited == False:
                    left.visited = True
                    current_node.wall_left = False
                    visited_nodes.append(left)
        self.character = (0,0)


    def print_grid(self):
        for row in self.grid:
            print('')
            for node in row:
                print(node, end='')
        print('')

    def move_character(self):
        pass

class Node:

    def __init__(self, row, column):
        # Only need bottom and left wall per node to represent walls of maze
        self.coordinates = (row, column)
        self.wall_bottom = True
        self.wall_left = True
        self.has_character = False
        self.visited = False

    def __str__(self):
        string = ''
        if self.wall_left:
            string += '|'
        else:
            string += ' '
        if self.wall_bottom:
            string += '_'
        else:
            string += ' '
        return string


if __name__ == '__main__':
   maze = Maze() 
   character = maze.character
   game_over = False
   print("""
    Welcome to the maze game!
    Your character is represented by the character 0 in the grid.
    Walls are represented by the character | and _ in the grid. Your character
    will not be able to move through them. The goal of the game is to
    successfully navigate to the end of the maze by issuing movement commands
    to your character. A list of legal commands will be listed before every 
    turn. For example:

    Moves: Up, Right

    Good Luck!
    """)
   while game_over == False:
       maze.print_grid()
       moves = maze.list_character_moves()
       direction = input()
       if direction not in moves:
           #Player did not enter a valid move
           print('Invalid move choice, please choose a move from the valid'
                 'moves list')
       else:
           maze.move_character(direction)
           if character.coordinates == maze.exit.coordinates:
               # player has reached the end of the maze!
               print('You\'ve won!, thank you for playing')
               game_over == True
