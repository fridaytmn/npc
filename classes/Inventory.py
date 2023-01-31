class Item:
    def __init__(self, name:str, weight:int, equipped=False):
        self.name = name
        self.weight = weight
        self.equipped = equipped
        
    def print_info(self):
        return [f'Наименование - {self.name}',
                f'Вес предмета - {self.weight}',
                f'Экипирован ли - {self.equipped}']
    
class Wear(Item):        
    def __init__(self, name: str, weight: int, type: str, materials: str, armor: int, equipped=False):
        super().__init__(name, weight, equipped)
        self.type = type
        self.materials = materials
        self.armor = armor
        

class Weapon(Item):
    def __init__(self, name: str, weight: int, type_weapon: str, damage: int, equipped=False):
        super().__init__(name, weight, equipped)
        self.type_weapon = type_weapon
        self.damage = damage
        self.equipped = equipped

        