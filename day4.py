import numpy as np


def word_search(grid, word):
    """
    Find all occurrences of the word in a word search grid (numpy array) that is made of up individual letters, 
    where the word can be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
    Return a count of all instances found.
    """

    def search_from_position(x, y, dx, dy):
        """
        Searches for the word starting from position (x, y) in the direction specified by (dx, dy).
        """
        for i in range(len(word)):
            if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
                return False
            if grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    def count_word():
        """
        Iterates through each cell in the grid and checks all eight possible directions 
        (up, down, left, right, and the four diagonals). It also checks the reverse directions.
        """
        count = 0
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # vertical and horizontal
            (1, 1), (-1, -1), (1, -1), (-1, 1) # diagonal
        ]
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                # iterate through each direction
                for dx, dy in directions:
                    if search_from_position(x, y, dx, dy):
                        count += 1
        return count

    return count_word()


with open('day4_input.txt') as f:
    lines = f.readlines()

temp_matrix = []
for line in lines:
    line = line.rstrip()
    temp = []
    for element in line:
        temp.append(element)
    temp_matrix.append(temp)

word = "XMAS"
ws_grid = np.array(temp_matrix)
#print (ws_grid)

count = word_search(ws_grid, word)

print (f"Count: {count}")

