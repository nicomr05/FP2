"""
TODO: Implement in the file the Trainer class
"""

from pokemon import Pokemon

class Trainer:
    '''Clase de entrenador, es al que le pertenecen los pokémons.
    
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
    all_debilitated(self, opponent): 
        Método que comprueba si todos los pokémons están debilitados.
    '''
    def __init__(self, name:str, pokemon:list):
        '''Asigna atributos al objeto. 
 
        Parameters 
        ---------- 
        name : str 
         Nombre del entrenador.
        pokemon : list 
         Lista con los pokémons del entrenador.
 
        Returns 
        ------- 
        None.
        '''
        self._name = name
        self._pokemon = pokemon
        
    def all_debilitated(self, opponent:Pokemon) -> bool:
        '''Asigna True si todos los pokémons del entrenador fueron derrotados.
 
        Returns 
        ------- 
        bool
            Resultado de comprobar si todos los pokémons del entrenador están debilitados.
        '''
        estado = False
        opponent = self._pokemon # ???
        for pokemon in opponent:
            if pokemon._hp <= 0:
                estado = True
            estado = estado # Revisar función (meter lógicos)
        return estado
        
    #def select_initial_pokemon(self) -> Pokemon:    
        
    #def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, nuevo_nombre) -> str:
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._name = nuevo_nombre
        else:
            raise ValueError('El nombre no puede tener longitud 0.')
    
    @property
    def pokemon(self) -> list:
        return self._pokemon
    
    @pokemon.setter
    def pokemon(self, nuevo_pokemon) -> list:
        #Hacer setter de pokemons
        pass