from weapon import Cutlass, Axe, Dagger

class Player:

    def __init__(self, str_name, str_origin, int_age, int_loc_x, int_loc_y):

        self.str_name = str_name 
        self.str_origin = str_origin
        self.int_age = int_age 

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.weapon_weapon_in_hand = None
        self.arr_armoury = [Cutlass(), Axe(), Dagger()]

        self.int_hp = 100
    
    def __str__(self):

        return (f"Call me Captain {self.str_name} of {self.str_origin} :D")
    
    def show_weapons_in_armoury(self):

        x = 1
        for weapon in self.arr_armoury:
            print(weapon)



