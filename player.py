from weapon import Cutlass, Axe, Dagger

class Player:

    def __init__(self, str_name, str_origin, int_age, int_loc_x, int_loc_y):

        self.str_name = str_name 
        self.str_origin = str_origin
        self.int_age = int_age 

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.weapon_weapon_in_hand = None
        self.arr_weapons_armoury = [Cutlass(), Axe(), Dagger()]

        self.int_hp = 100
    
    def __str__(self):

        return (f"Call me Captain {self.str_name} of {self.str_origin} :D")
    
    def show_weapons_in_armoury(self):

        x = 1
        for weapon in self.arr_weapons_armoury:
            print(weapon)
    
    def get_weapon(self):

        if (self.weapon_weapon_in_hand == None):
            print("\nI need a weapon...")
            self.set_weapon()
        else:
            print(f"I can always rely on my trusty {self.weapon_weapon_in_hand.str_weapon_type} the {self.weapon_weapon_in_hand.str_weapon_name} in the heat of battle!")
    
    def set_weapon(self):

        print(f"\nI wonder which weapon I'll choose from:\n")
        for x, weapon in enumerate(self.arr_weapons_armoury, 1):
            print(f"{x}. {weapon.str_weapon_name} the {weapon.str_weapon_type}; attack power: {weapon.int_weapon_atk_pwr}")
        
        int_weapon_selection = int(input(f"\nI'm going to close my eyes and pick a number between 1 and {len(self.arr_weapons_armoury)} like any good pirate XD:\n"))

        weapon_selected = self.arr_weapons_armoury[int_weapon_selection - 1]
        self.weapon_weapon_in_hand = weapon_selected 
        print(f"\nInto battle we go {self.weapon_weapon_in_hand.str_weapon_name}, my faithful {self.weapon_weapon_in_hand.str_weapon_type}")
    








