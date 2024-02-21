"""
TODO: Implement in this file the Pokemon hierarchy.
"""

from abc import ABC, abstractmethod

class Pokemon(ABC):
    '''
    Clase de todos los pokémons.
    De esta clase saldrán las clases hijas de los diferentes tipos de pokémon (Agua, Hierba o Fuego).
    Todo pokémon tiene los atributos de vida, 
 
    Attributes 
    ---------- 
    attr1 : tipo 
        Descripción.
 
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str): 
        Asigna atributos al objeto.
    basic_attack():
        Reduce los puntos de vida del oponente.
    is_debilitated():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''

    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        '''
        Asigna atributos al objeto. 
 
        Parameters 
        ---------- 
        name : str 
         Nombre del pokémon.
        level : int
         Nivel del pokémon.
        strength : int
         Fuerza del pokémon.
        defense: int
         Defensa del pokémon.
        hp : int
         Vida actual del pokémon.
        total_hp : int
        Vida máxima del pokémon.
        agility : int
         Agilidad del pokémon.
        pokemon_type : str
         Tipo de pokémon.
 
        Returns 
        ------- 
        None.
        '''
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type
        
    def __str__(self):
        '''
        Muestra los atributos del pokémon como un str.
 
        Returns 
        -------- 
        str 
            Atributos del pokémon como strings.
        '''
        cadena = '{name}({pokemon_type}) Stats: Level:{level}, ATT: {strength}, DEF: {defense}, AGI: {agility}, HP: {hp}/{total_hp}.' \
                .format(self._name, self._pokemon_type, self._level, self._strength, self._defense, self._agility, self._hp, self._total_hp)
        return cadena
        
    def basic_attack(self, opponent:'Pokemon') -> int:
        '''
        Disminuye la vida del pokémon rival en n unidades de daño.
 
        Parameters 
        ---------- 
        opponent : tipo
         Pokémon al que se le quitan los puntos de vida. 
 
        Returns 
        -------- 
        int
            Devuelve las unidades de daño inflingidas al rival. 
        '''
        damage = self._strength - opponent._defense
        self._hp = max(1, damage)
        return damage
    
    def is_debilitated(self) -> bool:
        '''
        Comprueba si la vida del pokémon llegó a 0.

        Returns 
        -------- 
        bool
            Resultado de comprobar si el pokémon está debilitado.
        '''
        if self._hp <= 0:
            return True
        else:
            return False
    
    @abstractmethod
    def effectiveness(self, opponent:'Pokemon') -> int:
        '''
        Método abstracto dentro de Pokemon. Este método debe ser implementado en todas las clases hijas de Pokemon.
        Indica la efectividad de un tipo de pokémon frente al resto.
        
        Parameters
        ---------- 
        opponent : Pokemon
         Pokémon rival.
 
        Returns 
        -------- 
        int
            Devuelve 1, 0 o -1 según el tipo de pokémon contra el que se esté enfrentando el pokémon del entrenador. 
        '''
        pass
        
class WaterPokemon(Pokemon):
    '''
    Clase de los pokémos de tipo agua.
    Esta clase es hija de la clase Pokemon, por lo que heredará sus métodos y añadirá los suyos propios.
 
    Attributes
    ---------- 
    attr1 : tipo 
        Descripción.
 
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str): 
        Asigna atributos al objeto.
    basic_attack():
        Reduce los puntos de vida del oponente.
    is_debilitated():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        '''
        Asigna atributos al objeto. Heredado de la clase Pokemon.
        '''
        return self.super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)
    
    def basic_attack(self, opponent:Pokemon) -> int:
        '''
        Método heredado de Pokemon, disminuye la vida del rival.
        '''
        return self.super().basic_attack(opponent)
    
    def is_debilitated(self) -> bool:
        '''
        Método heredado de Pokemon, devuelve si el pokémon está debilitado o no.
        '''
        return self.super().is_debilitated()
    
    def effectiveness(self, opponent:Pokemon) -> int:
        '''
        Implementación del método abstracto "effectiveness" para un WaterPokemon. 
        '''
        pass
    
if __name__ == '__main__':
    Squirtle = Pokemon(name='Squirtle', level=30, strength=4, defense=8, hp=25, total_hp=25, agility=15, pokemon_type=WaterPokemon)
    print(Squirtle)