from player import Player
from enemy import Enemy 
from weapon import Cutlass, Axe, Dagger
from items import HealingPotion
from tile import TradeTile, BattleTile
from data_structures import arr_world_map_back_end as world_map_be
from functions import set_player_name, set_player_origin, set_player_age

test_player = Player(set_player_name(), set_player_origin(), set_player_age(), 1, 1)
print(test_player)

test_trade_tile = TradeTile("Floating Fleamarket", "North Eastern", 2, 2)
print(test_trade_tile)

test_healing_potion = HealingPotion()
print(test_healing_potion)
test_healing_potion.healing_potion_property_description()











