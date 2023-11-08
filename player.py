class Player:

    def __init__(self, str_name, str_origin, int_age, int_loc_x, int_loc_y):

        self.str_name = str_name 
        self.str_origin = str_origin
        self.int_age = int_age 

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.weapon_weapon_in_hand = None
        self.arr_armoury = []

        self.int_hp = 100
    
    def __str__(self):

        return (f"Call me Captain {self.str_name} of {self.str_origin} :D")

