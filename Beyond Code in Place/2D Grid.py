"""Question : Implement a function, make_true_grid(grid) that is passed in a 2-dimensional list of integers (i.e., grid) and modifies the grid 
              passed in so that every row has the same number of elements. When your function is done, every row in the grid passed in should 
              have the same number of elements as the longest row (row with the most elements) in the original grid passed in
"""

def make_true_grid(grid):
	max_cols = 0
	for i in range(len(grid)):
	  cols = len(grid[i])
	  if cols > max_cols:
	      max_cols = cols

	for i in range(len(grid)):
	  cols = len(grid[i])
	  for j in range(max_cols - cols):
	      grid[i].append(0)
