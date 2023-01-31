class Item:
    def __init__(self, name:str, weight:int, equipped=False):
        self.name = name
        self.weight = weight
        self.equipped = equipped
        
    def print_info(self):
        result = [self.name, self.weight, self.equipped]
        return result
    
class Wear(Item):        
    def __init__(self, name: str, weight: int, type: str, materials: str, armor: int, equipped=False):
        super().__init__(name, weight, equipped)
        self.type = type
        self.materials = materials
        self.armor = armor
        
    def print_info(self):
        return [f'{super().print_info()}',
                f'Армор - {self.armor}',
                f'Материал - {self.materials}',
                f'Тип - {self.type}']
                
        

class Weapon(Item):
    def __init__(self, name: str, weight: int, type_weapon: str, damage: int, equipped=False):
        super().__init__(name, weight, equipped)
        self.type_weapon = type_weapon
        self.damage = damage
        self.equipped = equipped
        
    def print_info(self):
        return [f'{super().print_info()}',
                f'Тип - {self.type_weapon}',
                f'Урон - {self.damage}',]

        