from player import Player
from enemy import Enemy 
from weapon import Cutlass, Axe, Dagger
from tile import BattleTile
from data_structures import arr_world_map_back_end as world_map_be
from functions import set_player_name, set_player_origin, set_player_age

test_player = Player(set_player_name(), set_player_origin(), set_player_age(), 1, 1)
print(test_player)

test_player.get_weapon()
test_player.get_weapon()

test_enemy = Enemy("Doffy", 2, 1)
print(test_enemy)

test_battle_tile = BattleTile("Dressrosa", "Eastern", 2, 1)
print(test_battle_tile)

test_battle_tile.pvp_battle(test_player, test_enemy)






