class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        path[i] = "n", "S", "E", "W" 
        each representing movement 
        start on (0,0) and move 
        return True if path crosses itself at any point 

        """
        options = {"N": (0, 1), "E": (1, 0), "S": (0,-1), "W": (-1, 0)}
        start_row = 0
        start_col = 0
        visited = set([(0,0)])

        for option in path:
            
            start_row += options[option][0]
            start_col += options[option][-1]
            start = (start_row, start_col)
            if start in visited:
                return True 
            visited.add(start)
        return False
        