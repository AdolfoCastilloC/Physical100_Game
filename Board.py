from Zone import Zone

class Board():
    def __init__(self, rows, cols, zones):
        self.rows = rows
        self.cols = cols
        self.zones = zones
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
 
      
    def place_zone(self, zone, row, col):
        self.grid[row][col] = zone

    def get_zone(self, row, col):
        return self.grid[row][col]
    
    def initialize_escenario(self):
        
        return None