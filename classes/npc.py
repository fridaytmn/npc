from family import Family
from Inventory import Item, Weapon, Wear
from work import Work
from skills import Skill

class Npc:
    def __init__(self, id:int, name:str, family:Family, item:Item, work:Work, skills:Skill):    
        self.id = id
        self.name = name
        self.family = family
        self.inventory = [...item]
        self.work = work
        self.skills = skills
        
    def print_info(self):
        return print(f' Номер Персонажа - {self.id}\n',
                     f'Имя персонажа - {self.name}\n',
                     f'Родственники - {self.family.relationship_level[0]}, {self.family.name}\n',
                     f'Инвентарь - {self.inventory.print_info()}\n',
                     f'Должность - {self.work.position}\n',
                     f'Спец. способность - {self.skills.skill}')

def main():
    Anton = Family('Anton', 'Brat', 1)
    Bow = Weapon('Bow', 100, 'Ручной', 10, True)
    Shorts = Wear('Шорты', 10, True, 'Хлопок', 4, False)
    Stolyar = Work('Столяр', 'Столярная мастерская', 'Мастер')
    skill = Skill('Fire')
    npc = Npc(1, 'Stepa', Anton, Shorts, Stolyar, skill)
    npc.print_info()
    pass

if __name__ == "__main__":
    main()
    
