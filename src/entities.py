from config import MIN_DAMAGE

class Creature:
    def __init__(self, name: str, level: int, max_hp: int, attack: int, defense: int, sprite=None):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.sprite = sprite

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        self.hp = min(self.max_hp, self.hp + amount)

    def attack_target(self, target: "Creature") -> int:
        damage = max(MIN_DAMAGE, self.attack - target.defense)
        target.take_damage(damage)
        return damage

    def is_alive(self) -> bool:
        return self.hp > 0