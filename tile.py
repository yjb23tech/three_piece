class Tile:
    
    def __init__(self, str_tile_type, str_tile_island_name, str_tile_island_quadrant, int_tile_loc_x, int_tile_loc_y):

        self.str_tile_type = str_tile_type 
        self.str_tile_island_name = str_tile_island_name
        self.str_tile_island_quadrant = str_tile_island_quadrant

        self.int_tile_loc_x = int_tile_loc_x 
        self.int_tile_loc_y = int_tile_loc_y
    
    def __str__(self):

        message = (f"\nWelcome to {self.str_tile_island_name} Island in the {self.str_tile_island_quadrant} of the map")
        message += (f"\nThis island is found at co-ordinates [{self.int_tile_loc_x}, {self.int_tile_loc_y}]")
        return message 

class BattleTile(Tile):

    def __init__(self, str_tile_island_name, str_tile_island_quadrant, int_tile_loc_x, int_tile_loc_y):

        self.enemy_tile_island_boss =  None 

        super().__init__("Battle Tile", str_tile_island_name, str_tile_island_quadrant, int_tile_loc_x, int_tile_loc_y)
    
