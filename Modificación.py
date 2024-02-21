# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:32:13 2024

@author: pablo
"""

class FirePokemon(Pokemon):
    '''
    Clase de los pokémos de tipo fuego.
    Esta clase es hija de la clase Pokemon, por lo que heredará sus métodos y añadirá los suyos propios.
 
    Attributes
    ---------- 
    attr1 : tipo 
        Descripción.
 
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, temperature:float): 
        Asigna atributos al objeto.
    basic_attack():
        Reduce los puntos de vida del oponente.
    is_debilitated():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''   
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, temperature:float):
        '''
        Asigna atributos al objeto. Heredado de la clase Pokemon.
        
        Parameters 
        ----------
        (Hereda los parámetros de Pokemon.)
        temperature : float
         Informa de la temperatura del Pokemon de fuego.
        
        Returns
        -------
        None.
        '''
        self.super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)
        self._temperature = temperature
    
    def fire_attack(self, p:Pokemon)-> int:
        '''
        Calcula el daño realizado a los distintos Pokemons
        
        Returns 
        -------- 
        int
            Resultado de calcular el daño infligido. 
        '''
        pass
    def embers(self, p:Pokemon) -> int:
        '''
        Informa del estado de un Pokemon.
        
        Returns 
        -------- 
        int
            Resultado de calcular el estado de un Pokemon. 
        '''
        pass
    def effectiveness(self, opponent:Pokemon) -> int:
         '''
         Implementación del método abstracto "effectiveness" para un FirePokemon. 
         '''
         if p== GrassPokemon:
             return 1
         elif p==FirePokemon:
             return 0
         else:
             return -1
    class GrassPokemon(Pokemon):
        '''
        Clase de los pokémos de tipo hierba.
        Esta clase es hija de la clase Pokemon, por lo que heredará sus métodos y añadirá los suyos propios.
     
        Attributes
        ---------- 
        attr1 : tipo 
            Descripción.
     
        Methods 
        ------- 
        __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str,healing:float): 
            Asigna atributos al objeto.
         basic_attack():
            Reduce los puntos de vida del oponente.
        is_debilitated():
            Indica si el pokémon tiene 0 puntos de vida.
        effectiveness():
            Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
        '''   
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, healing:float):
            '''
            Asigna atributos al objeto. Heredado de la clase Pokemon.
            
            Parameters 
            ----------
            (Hereda los parámetros de Pokemon.)
            healing : float
             Informa de la recuperación del Pokemon de hierba.
            
            Returns
            -------
            None.
            '''
            self.super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type, healing)
            self._healing = healing
    def grass_attack(self, p:Pokemon)-> int:
            '''
            Calcula el daño realizado a los distintos Pokemons
            
            Returns 
            -------- 
            int
                Resultado de calcular el daño infligido. 
            '''
            pass   
    def heal(self)-> int:
           '''
           Informa de la recuperación de los distintos GrassPokemons.

           Returns
           -------
           int
               Resultado de calcular la recuperación alcanzada por un GrassPokemon.

           '''
           
    def effectiveness(self, opponent:Pokemon) -> int:
         '''
         Implementación del método abstracto "effectiveness" para un GrassPokemon. 
         '''
         pass
     
if __name__ == '__main__':
    Squirtle = Pokemon(name='Squirtle', level=30, strength=4, defense=8, hp=25, total_hp=25, agility=15, pokemon_type=WaterPokemon)
    print(Squirtle)