from player import Player
from weapon import Cutlass, Axe, Dagger
from tile import BattleTile

test_player = Player("Monkey D Luffy", "Romance Dawn Island", 29, 1, 1)
print(test_player)

test_player.show_weapons_in_armoury()

#No weapon to begin with
test_player.get_weapon()
#Post iniital weapon selection, checking to confirm I have a weapon in hand
test_player.get_weapon()

#Changing my weapon from my current weapon selection
test_player.set_weapon()
#Confirming my weapon selection was successful 
test_player.get_weapon()

test_battle_tile = BattleTile("Dressrosa", "Eastern", 2, 1)
print(test_battle_tile)


