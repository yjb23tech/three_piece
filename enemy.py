from data_structures import arr_world_map_back_end as arr_world_map_be
from weapon import StandardEnemyWeapon 
import random 


class Enemy:

    def __init__(self, str_name, int_loc_x, int_loc_y):

        self.str_name = str_name 

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y 

        self.int_hp = 100

        self.weapon_weapon_in_hand = StandardEnemyWeapon()

        self.int_def_pwr = random.randint(1, 10)
    
    def __str__(self):

        message = f"\nMy name is Captain {self.str_name} of {arr_world_map_be[self.int_loc_x][self.int_loc_y].str_tile_island_name} Island"
        message += f"\nAre you ready to die, Sailor?"
        return message 
    
    def get_atk_pwr(self):

        int_atk_pwr = self.int_atk_pwr
        return int_atk_pwr 
    
    def get_def_pwr(self):

        int_def_pwr = self.int_def_pwr
        return int_def_pwr 
    

    

