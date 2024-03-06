"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon

class Trainer:
    '''
    Clase de entrenador, es al que le pertenecen los pokémons.
    
    Clase en la que se recoge la lista de los nombres de los 6 pokémons pertenecientes al entrenador además
    de comprobar si todos los pokémons del mismo están debilitados o no.
 
    Attributes 
    ---------- 
    name : str
         Nombre del entrenador.
        pokemon : list 
         Lista con los pokémons del entrenador.
 
    Methods 
    -------
    __init__(self, name:str, pokemon:list): 
        Asigna atributos al objeto.

    all_debilitated(self, opponent): 
        Comprueba si todos los pokémons están debilitados.
    
    select_first_pokemon(self):
        Selecciona el pokémon que se escogerá al iniciar el combate.
    
    select_next_pokemon(self, p:Pokemon):
        Selecciona el pokémon no debilitado que mejor vaya contra el oponente actual.
        Tiene como precondición que exista un pokémon no debilitado.
    '''
    def __init__(self, name:str, pokemon:list):
        '''
        Asigna atributos al objeto. 
 
        Parameters 
        ---------- 
        name : str 
         Nombre del entrenador.
        pokemon : list 
         Lista con los pokémons del entrenador.
        '''
        self._name = name
        self._pokemon = pokemon
        
    def all_debilitated(self) -> bool:
        '''
        Asigna True si todos los pokémons del entrenador fueron derrotados.
        
        Returns 
        ------- 
        bool
         Resultado de comprobar si todos los pokémons del entrenador están debilitados (T/F).
        '''
        for bicho in self.pokemon:
            if bicho.hp > 0:
                return False
        return True
        
    def select_first_pokemon(self) -> Pokemon:    
        '''
        Devuelve el primer pokémon de la lista de pokémons del entrenador que no esté
        debilitado.
        Devuelve None en caso de que no exista ningún pokémon disponible.
        
        Returns 
        ------- 
        bicho : Pokemon
         Primer pokémon que no está debilitado dentro de la lista de pokémons del entrenador.
        None.
        '''
        if self.all_debilitated():
            return None
        
        for bicho in self.pokemon:
            if bicho.hp > 0:
                return bicho

    def select_next_pokemon(self, opponent:Pokemon) -> Pokemon:
        '''
        Selecciona el pokémon del entrenador que más probabilidades de ganar
        tenga contra el pokémon contra el que se esté luchando.
        
        Returns 
        ------- 
        pok : Pokemon
         Pokémon que mejor se ajuste a la batalla.
        '''
        if self.all_debilitated():
            return None
        else:
            efectividad = -1
            for bicho in self.pokemon:
                if not bicho.is_debilitated() and bicho.effectiveness(opponent) > efectividad:
                    efectividad = bicho.effectiveness(opponent)
                    pok = bicho
                elif not bicho.is_debilitated() and bicho.effectiveness(opponent) == efectividad:
                    if bicho.level >= pok.level:
                        efectividad = bicho.effectiveness(opponent)
                        pok = bicho
                        
            return pok
            
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._name = nuevo_nombre
        else:
            raise ValueError('El nombre debe de ser un string con longitud mayor que 0.')
    
    @property
    def pokemon(self) -> list:
        return self._pokemon
    
    @pokemon.setter
    def pokemon(self, nuevo_pokemon):
        if isinstance(nuevo_pokemon, Pokemon):
            self._pokemon.append(nuevo_pokemon)
        else:
            raise ValueError('El pokémon a añadir debe de ser de tipo Pokemon.')
    