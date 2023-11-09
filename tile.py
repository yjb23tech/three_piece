from player import Player 
from random import randint
import time 
from game_text import pre_fight_sequence_msg, starting_fight_sequence_msg, attack_defended_against_msg, attack_defended_against_outcome_msg, attack_not_defended_against_msg, special_attack_msg, tile_boss_defeated_msg 

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
    

    def pvp_battle(self, user_player, tile_boss):

        round_counter = 1 

        intro_msg = f"\nWelcome Captain {user_player.str_name} and Captain {tile_boss.str_name}"
        intro_msg += f"\nOnly one of you is going to make it out alive"
        print(intro_msg)

        attacking_avatar = user_player
        defending_avatar = tile_boss 

        print((pre_fight_sequence_msg.format(attacking_avatar.str_name, defending_avatar.str_name)))

        while ((user_player.int_hp > 0) and (tile_boss.int_hp > 0)):

            print((starting_fight_sequence_msg.format(attacking_avatar.str_name, attacking_avatar.int_hp, defending_avatar.str_name, defending_avatar.int_hp, round_counter)))

            dice_score = randint(1, 6)

            if ((dice_score % 2) != 0):
                resulting_damage = attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr - defending_avatar.int_def_pwr 
                print((attack_defended_against_msg.format(attacking_avatar.str_name, attacking_avatar.weapon_weapon_in_hand.str_weapon_name, defending_avatar.str_name, attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr, defending_avatar.str_name)))
                time.sleep(15)
                print((attack_defended_against_outcome_msg.format(attacking_avatar.str_name, attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr, attacking_avatar.str_name, defending_avatar.str_name, defending_avatar.int_def_pwr)))
            else:
                if ((round_counter > 2) and (isinstance(attacking_avatar, Player))):
                    resulting_damage = attacking_avatar.weapon_weapon_in_hand.int_weapon_special_atk_pwr_boost + attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr 
                    print((special_attack_msg.format(attacking_avatar.str_name, (attacking_avatar.weapon_weapon_in_hand.str_weapon_special_atk_name.upper()), defending_avatar.str_name, resulting_damage)))
                else:
                    resulting_damage = attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr 
                    print((attack_not_defended_against_msg.format(attacking_avatar.str_name, attacking_avatar.weapon_weapon_in_hand.int_weapon_atk_pwr, defending_avatar.str_name)))
            
            defending_avatar.int_hp -= resulting_damage

            if attacking_avatar == user_player:
                attacking_avatar = tile_boss
                defending_avatar = user_player
            else:
                attacking_avatar = user_player
                defending_avatar = tile_boss  

            round_counter += 1 

            time.sleep(5)

        if (user_player.int_hp <= 0):
            pass
        else:
            print(((tile_boss_defeated_msg.format(tile_boss.str_name, tile_boss.int_hp, user_player.str_name, user_player.int_hp))))

    
