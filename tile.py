from random import randint

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
    

    def pvp_battle(user_player, tile_boss):

        round_counter = 1 

        intro_msg = f"Welcome Captain {user_player.str_name} and Captain {tile_boss.str_name}"
        intro_msg += f"Only one of you is going to make it out alive"

        attacking_avatar = user_player
        defending_avatar = tile_boss 

        pre_fight_sequence_msg = f"Captain {attacking_avatar.str_name} will be on attack first and {defending_avatar.str_name} will be on defence"
        pre_fight_sequence_msg += f"\nAt the end of each round your battle stances will change"
        pre_fight_sequence_msg += "\nIT'S TIME TO FIGHT!"

        print(pre_fight_sequence_msg)

        while ((user_player.int_hp > 0) and (tile_boss.int_hp > 0)):

            starting_fight_sequence_msg = f"Captain {attacking_avatar.str_name} has {attacking_avatar.int_hp} health points remaining"
            starting_fight_sequence_msg += f"\nCaptain {defending_avatar.str_name} has {defending_avatar.int_hp} health points remaining"
            starting_fight_sequence_msg += f"\nRound {round_counter} - BEGIN!\n"

            print(starting_fight_sequence_msg)

            dice_score = randint(1, 6)

            if ((dice_score % 2) != 0):
                attack_defended_against_msg = f"{attacking_avatar.str_name} launches a ferocious attack with his trusted weapon {attacking_avatar.weapon_weapon_in_hand.str_weapon_name}"
                attack_defended_against_msg = f"But Captain {defending_avatar.str_name} skillfully parries, reducing the damage impact - it's heating up!"

                resulting_damage = attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr - defending_avatar.int_def_pwr 
            else:

                attack_not_defended_against_msg = f"{attacking_avatar.str_name} lands a devastating blow that shocks the crowd! This was a deadly assault {defending_avatar.str_name} failed to dodge!"
                resulting_damage = attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr 
            
            defending_avatar.int_hp -= resulting_damage

            attacking_avatar = defending_avatar 
            defending_avatar = attacking_avatar 

            round_counter += 1 


            #user_player launches an attack 
            #if dice_roll == odd tile_boss has the ability to block and reduce damage 
    
