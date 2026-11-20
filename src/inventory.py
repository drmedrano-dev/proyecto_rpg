from src.entities import Creature


class Item:
    def __init__(self, name: str, item_type: str, value: int):
        self.name = name
        self.item_type = item_type
        self.value = value


class Inventory:
    def __init__(self):
        self.items: dict[str, dict] = {}

    def add_item(self, item: Item, quantity: int = 1) -> None:
        if item.name in self.items:
            self.items[item.name]["quantity"] += quantity
        else:
            self.items[item.name] = {"item": item, "quantity": quantity}

    def use_item(self, item_name: str, target_creature: Creature) -> bool:
        if item_name not in self.items or self.items[item_name]["quantity"] <= 0:
            return False

        entry = self.items[item_name]
        item: Item = entry["item"]

        if item.item_type == "heal":
            target_creature.heal(item.value)
        else:
            return False

        entry["quantity"] -= 1
        if entry["quantity"] == 0:
            del self.items[item_name]
        return True