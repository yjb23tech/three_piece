from items import HealthPotion, AttackWhetstone, DefenseCharm

class NPC:

    def __init__(self, str_npc_type, str_npc_name):

        self.str_npc_type = str_npc_type
        self.str_npc_name = str_npc_name

    def __str__(self):

        intro_msg = f"\nHi! I'm a {self.str_npc_type} but you can call me {self.str_npc_name} - nice to meet ya XD"
        return intro_msg

class Merchant(NPC):

    def __init__(self):

        self.int_gold_in_wallet = 1_000
        self.arr_items_inventory = [HealthPotion(), AttackWhetstone(), DefenseCharm()]

        super().__init__("Merchant", "Silvers Raleigh")
    
    def display_merchant_inventory(self):

        for x, item in enumerate(self.arr_items_inventory, 1):

            print(f"\n{x}. {item.str_item_name}")
            print(item)





