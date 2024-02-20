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
 
        Returns 
        ------- 
        None.
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
        estado = False #Iniciamos la variable que controla el estado de todos los pokémons en False.
        estado_pokemon = False # Iniciamos la variable que controla el estado de cada pokémon en False. 
        lista_pokemons = self._pokemon
        
        for pokemon in lista_pokemons:
            if pokemon._hp <= 0:
                estado_pokemon = True
            estado = estado and estado_pokemon # Revisar función otra vez.
        
        return estado
        
    def select_first_pokemon(self) -> Pokemon:    
        '''
        Devuelve el primer pokémon de la lista de pokémons del entrenador que no esté
        debilitado. Devuelve None en caso de que no exista ningún pokémon disponible.
        
        Returns 
        ------- 
        Pokemon
         Primer pokémon que no está debilitado dentro de la lista de pokémons del entrenador.
        '''
        pass

    def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        '''
        Selecciona el pokémon del entrenador que más probabilidades de ganar
        tenga contra el pokémon contra el que se esté luchando.
        
        Returns 
        ------- 
        Pokemon
         Pokémon que mejor se ajuste a la batalla.
        '''
        pass

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