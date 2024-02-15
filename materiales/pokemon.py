"""
TODO: Implement in this file the Pokemon hierarchy.
"""

from abc import ABC, abstractmethod

class Pokemon(ABC):
    '''
    
    '''
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
        
    def __str__(self):
        
        pass
        
    def basic_attack(self, p:Pokemon) -> int:
        damage = self._strength - p._defense
        self._hp = max(1, damage)
        return damage
    
    def is_debilitated(self) -> bool:
        if self._hp <= 0:
            return True
        else:
            return False
    
    @abstractmethod
    def effectiveness(self, p:Pokemon) -> int:
        '''Clase abstracta dentro de Pokemon'''
        pass
        
class WaterPokemon(Pokemon):
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        self.super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)
        