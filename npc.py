from items import HealingPotion, DefenseCharm

class NPC:

    def __init__(self, str_npc_type, str_npc_name):

        self.str_npc_type = str_npc_type
        self.str_npc_name = str_npc_name

    def __str__(self):

        intro_msg = f"\nHi! I'm a {self.str_npc_type} but you can call me {self.str_npc_name} - nice to meet ya XD"
        return intro_msg

class Merchant(NPC):

    def __init__(self):

        self.arr_items_inventory = [HealingPotion(), DefenseCharm()]

        super().__init__("Merchant", "Silvers Raleigh")

