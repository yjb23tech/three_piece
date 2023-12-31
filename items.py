class Item:

    def __init__(self, str_item_type, str_item_name, int_item_gold_cost):

        self.str_item_type = str_item_type 
        self.str_item_name = str_item_name

        self.int_item_gold_cost = int_item_gold_cost

    def __str__(self):

        item_details_msg = f"This is the {self.str_item_name} and it belongs to the {self.str_item_type} family of items "
        item_details_msg += f"\nThis item will cost you {self.int_item_gold_cost} gold coins"

        return (item_details_msg)

class HealthPotion(Item):

    def __init__(self):

        self.int_hp_boost_value = 50 

        super().__init__("Health", "Health Potion", 20)
    
    def health_potion_property_description(self):

        description_msg = f"Using the {self.str_item_name} can raise your total number of health points by {self.int_hp_boost_value}"
        print(description_msg)


class AttackWhetstone(Item):

    def __init__(self):

        self.int_atk_pwr_boost_value = 40

        super().__init__("Attack", "Whetstone", 50)

    def attack_whetstone_property_description(self):

        description_msg = f"Using the {self.str_item_name} can raise your total attacking power by {self.int_atk_pwr_boost_value} damage points"
        print(description_msg)


class DefenseCharm(Item):

    def __init__(self):

        self.int_def_boost_value = 30 

        super().__init__("Defensive", "Defense Charm", 14)
    
    def defense_charm_property_description(self):

        description_msg = f"Using the {self.str_item_name} can raise your defensive guard by {self.int_def_boost_value} points"
        print(description_msg)





