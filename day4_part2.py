
def word_search_xmas_diagonal(grid):
    """
    find the number of times the word 'MAS' appears as a diagonal X in the word search and return the count. 
    
    Here is an example of a valid diagonal X:
    Valid Diagonals:
        [M . M]    [M . S]    [S . S]    [S . M]
        [. A .] or [. A .] or [. A .] or [. A .]
        [S . S]    [M . S]    [M . M]    [S . M]
    """
    x_goal = ['MAS', 'SAM']
    count= 0

    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            diagonal_1 = ''.join([grid[row][col],
                                  grid[row+1][col+1],
                                  grid[row+2][col+2]])
            diagonal_2 = ''.join([grid[row+2][col],
                                  grid[row+1][col+1],
                                  grid[row][col+2]])
            count += diagonal_1 in x_goal and diagonal_2 in x_goal
    
    return count
  

with open('day4_input.txt') as f:
    lines = f.readlines()

temp_matrix = []
for line in lines:
    line = line.rstrip()
    temp = []
    for element in line:
        temp.append(element)
    temp_matrix.append(temp)

count = word_search_xmas_diagonal(temp_matrix)

print (f"Count: {count}")

