
class Solution:
    def numIslands(self, grid):
        if grid == None:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    # if i or j out of bounds or not an island, do nothing
    # but if it is part of the island, mark it so that it doesn't get 
    # double counted
    
    def dfs(self, grid, i, j):
        if i< 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return None
        
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)