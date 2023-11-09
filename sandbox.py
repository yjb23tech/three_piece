from player import Player
from npc import Merchant
from enemy import Enemy 
from weapon import Cutlass, Axe, Dagger
from items import HealthPotion, AttackWhetstone, DefenseCharm
from tile import TradeTile, BattleTile
from data_structures import arr_world_map_back_end as world_map_be
from functions import set_player_name, set_player_origin, set_player_age

test_player = Player(set_player_name(), set_player_origin(), set_player_age(), 1, 1)
print(test_player)

test_trade_tile = TradeTile("Floating Fleamarket", "North Eastern", 2, 2)
print(test_trade_tile)

test_merchant = Merchant()
print(test_merchant)

test_attack_whetstone = AttackWhetstone()
print(test_attack_whetstone)
test_attack_whetstone.attack_whetstone_property_description()

test_merchant.display_merchant_inventory()
















