import random 

class Weapon:

    def __init__(self, str_weapon_type, str_weapon_name):

        self.str_weapon_type = str_weapon_type 
        self.str_weapon_name = str_weapon_name
    
    def __str__(self):

        message = (f"\nThis weapon is called the {self.str_weapon_name}; it is a {self.str_weapon_type} with an attack power of {self.int_weapon_atk_pwr}")
        message += (f"\nWhen the time is right... you can increase your attack power by {self.int_weapon_special_atk_pwr_boost} damage points ")
        message += (f"through your special move called '{self.str_weapon_special_atk_name}'")

        return message

class Cutlass(Weapon):

    def __init__(self):

        self.int_weapon_atk_pwr = random.randint(40, 50) 

        self.str_weapon_special_atk_name = "Divine Departure"
        self.int_weapon_special_atk_pwr_boost = 50 

        super().__init__("Cutlass", "Widow Maker")

class Axe(Weapon):

    def __init__(self):

        self.int_weapon_atk_pwr = random.randint(30, 40)

        self.str_weapon_special_atk_name = "Ragnarok"
        self.int_weapon_special_atk_pwr_boost = 30

        super().__init__("Axe", "Mjolnir")

class Dagger(Weapon):

    def __init__(self):

        self.int_weapon_atk_pwr = random.randint(20, 30) 
        self.str_weapon_special_atk_name = "Creeping Cut"
        self.int_weapon_special_atk_pwr_boost = 10 

        super().__init__("Dagger", "Gut Guest")

