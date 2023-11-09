from player import Player
from weapon import Cutlass, Axe, Dagger
from tile import BattleTile
from data_structures import arr_world_map_back_end as world_map_be
from functions import set_player_name, set_player_origin, set_player_age

test_player = Player(set_player_name(), set_player_origin(), set_player_age(), 1, 1)
print(test_player)

for x in range(len(world_map_be)):
    for y in range(len(world_map_be[x])):
        island = world_map_be[x][y]
        print(island)
print(" ")





