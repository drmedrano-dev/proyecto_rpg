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
    
class Player(Creature):
     XP_PER_LEVEL = 100
     HP_PER_LEVEL = 10
     ATTACK_PER_LEVEL = 2
     DEFENSE_PER_LEVEL = 1
     
     def __init__(self, name: str, level: int, max_hp: int, attack: int, defense: int, sprite = None):
         super().__init__(name, level, max_hp, attack, defense, sprite)
         self.xp = 0
         
     def xp_to_next_level(self) -> int:
         return self.level * self.XP_PER_LEVEL
     
     def gain_xp(self, amount: int) -> bool:
         self.xp += amount
         leveled_up = False
         while self.xp >= self.xp_to_next_level():
             self.xp -= self.xp_to_next_level()
             self.level_up()
             leveled_up = True
         return leveled_up
     
     def level_up(self) -> None:
         self.level += 1
         self.max_hp += self.HP_PER_LEVEL
         self.hp = self.max_hp
         self.attack += self.ATTACK_PER_LEVEL
         self.defense += self.DEFENSE_PER_LEVEL
         
class Enemy(Creature):
    
    DEFAULT_XP_REWARD = 20
    
    def __init__(self, name: str, level: int, max_hp: int, attack: int, defense: int, sprite = None, xp_reward: int = DEFAULT_XP_REWARD):
        super().__init__(name, level, max_hp, attack, defense, sprite)
        self.xp_reward = xp_reward