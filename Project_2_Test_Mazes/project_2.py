##          Andrew Garcia      | Project 2 |       11/20/2019

##This program was made to be able to handle multiple mazes with paths that lead to dead ends and still continue to search for the end of the maze marked as E
##This program can also handle erros such as no path to E or no S or E are found in the maze or a file does not contain a maze or special characters

def main():
    variable = []
    invalid_X = False
## Read into the file and turn it into list of lists to be able to index them check for blank space in algorithm
    try:
        filename = input("Enter a file: ")
        fileOpen = open(filename, "r")
        for line in fileOpen:
            line = line.strip("\n")
            temp = []
            for char in line:
                temp.append(char)
            variable.append(temp)
## check if the file read actually has a maze inside it
        if len(variable) == 0:
            print("Error: Specified file contains no maze.")
            return
        given_maze = variable
## find S and E inside the maze and return a number        
        x, y = start("S", given_maze)
        z, w = start("E", given_maze)
        invalid, inchar = in_blocks(given_maze)
## check if invalid char is in the file and return the line num and the char
        if (invalid>0):
            print("Error: Maze contains invalid characters. Line",invalid," contains invalid character",inchar)
            return
## check for S or E to be inside the file by the number returned based on if it is there or not
        if(x == -1 or y == -1):
            print("Error: no start position found.")
            return
        if(z == -1 or w == -1):
            print("Error: no end position found.")
            return
        show_maze(given_maze)
        maze_runner(given_maze, x, y)
        fileOpen.close()
## try/except for crash if file does not exist
    except FileNotFoundError:
        print("Error: Specified file does not exist.")
        return
    
## printing function of maze by turning the maze into a string and print all of it at once
def show_maze(maze):
    p_maze = " "
    for every_line in maze:
        temp = ''.join(every_line)
        p_maze = p_maze + '\n' + temp
    print(p_maze)
    print("")
    
## function to identify any invalid char by for looping across file    
def in_blocks(maze):
    blocks = ["#",' ','S','E']
    invalid_X = 0
    for line in maze:
        for element in line:
            if element not in blocks:
                return invalid_X, element
        invalid_X += 1
    invalid_X = 0
    return invalid_X, '0'

## function to find the char requested which would be S and E for the maze
def start(character, maze):
    row_count = 0
    for row in maze:
        column_count = 0
        for column in row:
            if column == character:
                return row_count, column_count
            column_count += 1
        row_count += 1
    return (-1, -1)

## function that iterates through the list of lists and finds the start to end
def maze_runner(maze, row, column):
    num_row = len(maze)
    rli = []
## make a list of the number of rows
    for i in range(0, num_row):
        rli.append(i)
    num_columns =len(maze[0])
    cli = []
## make a list of number of columns
    for j in range(0,len(maze[0])):
        cli.append(j)

    
    while True:
## interations if the next space is an S so the S does not get replaced and able to handle looking ahead and not get Stuck
        if maze[row][column] == "S":
            if row - 1 in rli and column in cli:
                if maze[row - 1][column] == " ":
                    maze[row - 1][column] = "^"
                    row -= 1
                    show_maze(maze)
                    continue
            if row in rli and column - 1 in cli:   
                if maze[row][column - 1] == " ":
                    maze[row][column - 1] = "<"
                    column -= 1
                    show_maze(maze)
                    continue
            if row + 1 in rli and column in cli:
                if maze[row + 1][column] == " ":
                    maze[row + 1][column] = "v"
                    row += 1
                    show_maze(maze)
                    continue
            if row in rli and column + 1 in cli:
                if maze[row][column + 1] == " ":
                    maze[row][column + 1] = ">"
                    column += 1
                    show_maze(maze)
                    continue
            print("Error: No route could be found from start to end. Maze unsolvable.")
            break
        
## first if checks the position it will just check is actually inside the bounds of the maze if not then it wont run it. so it wont index out. and its all the same for the rest
        if row in rli and column - 1 in cli:
## checks left of maze for open space
            if maze[row][column - 1] == " ":
                maze[row][column] = "<"
                column -= 1
                show_maze(maze)
                continue
## checks below for open space
        if row + 1 in rli and column in cli:
            if maze[row + 1][column] == " ":
                maze[row][column] = "v"
                row += 1
                show_maze(maze)
                continue

        if row in rli and column +1 in cli:
## checks right for open space
            if maze[row][column + 1] == " ":
                maze[row][column] = ">"
                column += 1
                show_maze(maze)
                continue
        if row - 1 in rli and column in cli:
##checks above for open space
            if maze[row - 1][column] == " ":
                maze[row][column] = "^"
                row -= 1
                show_maze(maze)
                continue
        if row in rli and column + 1 in cli:
## these below statements check right left down up if space is E to stop program
            if maze[row][column + 1] == "E":
                maze[row][column] = ">"
                column += 1
                show_maze(maze)
                break
        if not(column -1 < 0):   
            if maze[row][column - 1] == "E":
                maze[row][column] = "<"
                column -= 1
                show_maze(maze)
                break
        if row + 1 in rli and column in cli:
            if maze[row + 1][column] == "E":
                maze[row][column] = "v"
                row += 1
                show_maze(maze)
                break
        if row - 1 in rli and column in cli:
            if maze[row - 1][column] == "E":
                maze[row][column] = "^"
                row -= 1
                show_maze(maze)
                break
## these below statements are backtracking to replace arrows for dots if there is no other way to go and S is included to be able to backtrack up to S and not get Stuck because
## it does not know what exactly S is
        if row - 1 in rli:
            if maze[row - 1][column] == "v" or maze[row-1][column] == 'S':
                maze[row][column] = "."
                row -= 1
                show_maze(maze)
                continue
        if column + 1 in cli:
            if maze[row][column + 1] == "<" or maze[row][column + 1] == 'S':
                maze[row][column] = "."
                column += 1
                show_maze(maze)
                continue
        if row + 1 in rli:
            if maze[row + 1][column] == "^" or maze[row + 1][column] == 'S':
                maze[row][column] = "."
                row += 1
                show_maze(maze)
                continue
        if column - 1 in cli:
            if maze[row][column - 1] == ">" or maze[row][column - 1] == 'S':
                maze[row][column] = "."
                column -= 1
                show_maze(maze)
                continue



main()
