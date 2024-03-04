"""
TODO: Implement in this file the Pokemon hierarchy.
"""

from abc import ABC, abstractmethod
from math import floor

class Pokemon(ABC):
    '''
    Clase de todos los pokémons.
    De esta clase saldrán las clases hijas de los diferentes tipos de pokémon (Agua, Hierba o Fuego).
    Todo pokémon tiene los atributos de nombre, nivel, fuerza, defensa, puntos de salud, salud total,
    agilidad y tipo de pokémon, además de los atributos propios de cada tipo de pokémon.
 
    Attributes 
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
 
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str): 
        Asigna atributos al objeto.
    __str__():
        Muestra los atributos del pokémon como un str.
    basic_attack():
        Reduce los puntos de vida del oponente.
    is_debilitated():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''

    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str):
        '''
        Clase de todos los pokémons.
        De esta clase saldrán las clases hijas de los diferentes tipos de pokémon (Agua, Hierba o Fuego).
        Todo pokémon tiene los atributos de nombre, nivel, fuerza, defensa, puntos de salud, salud total,
        agilidad y tipo de pokémon, además de los atributos propios de cada tipo de pokémon.
 
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
        cadena : str 
        Atributos del pokémon como strings.
        '''
        cadena = '{name}({pokemon_type}) Stats: Level:{level}, ATT: {strength}, DEF: {defense}, AGI: {agility}, HP: {hp}/{total_hp}.' \
                .format(self.name, self.pokemon_type, self.level, self.strength, self.defense, self.agility, self.hp, self.total_hp)
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
        damage : int
         Devuelve las unidades de daño inflingidas al rival. 
        '''
        damage = max(1, self.strength - opponent.defense)
        opponent.hp -= damage
        
        if opponent.hp < 0:
            opponent.hp = 0
        
        return damage
    
    def is_debilitated(self) -> bool:
        '''
        Comprueba si la vida del pokémon llegó a 0.

        Returns 
        -------- 
        bool
            Resultado de comprobar si el pokémon está debilitado.
            True si está debilitado.
            False si no está debilitado.
        '''
        if self.hp <= 0:
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
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def total_hp(self) -> int:
        return self._total_hp
    
    @property
    def level(self) -> int:
        return self._level
    
    @level.setter
    def level(self, nuevo_nivel):
        if isinstance(nuevo_nivel, int) and nuevo_nivel >= 0:
            self._level = nuevo_nivel
        else:
            raise ValueError('El nivel debe ser un entero no negativo.')
    
    @property
    def strength(self) -> int:
        return self._strength
    
    @strength.setter
    def strength(self, nueva_fuerza):
        if isinstance(nueva_fuerza, int) and nueva_fuerza >= 0:
            self._strength = nueva_fuerza
        else:
            raise ValueError('La fuerza debe ser un entero no negativo.')
    
    @property
    def defense(self) -> int:
        return self._defense
    
    @defense.setter
    def defense(self, nueva_defensa):
        if isinstance(nueva_defensa, int) and nueva_defensa >= 0:
            self._defense = nueva_defensa
        else:
            raise ValueError('La defensa debe ser no negativa.')
    
    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, nueva_vida):
        if isinstance(nueva_vida, int) and nueva_vida >= 0:
            self._hp = nueva_vida
        else:
            raise ValueError('La vida debe ser no negativa.')
    
    @property
    def agility(self) -> int:
        return self._agility
    
    @agility.setter
    def agility(self, nueva_agilidad):
        if isinstance(nueva_agilidad, int) and nueva_agilidad >= 0:
            self._agility = nueva_agilidad
        else:
            raise ValueError('La agilidad debe ser no negativa.')
    
    @property
    def pokemon_type(self) -> str:
        return self._pokemon_type
    
    @pokemon_type.setter  #Revisar setter
    def pokemon_type(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str) and len(nuevo_tipo) > 0 and nuevo_tipo in ['Water','Fire','Grass']:
            self._pokemon_type = nuevo_tipo
        else:
            raise ValueError('El tipo del pokémon debe ser uno de los siguientes: Water/Fire/Grass')
    

class WaterPokemon(Pokemon):
    '''
    Clase de los pokémos de tipo agua.
    Esta clase es hija de la clase Pokemon, por lo que heredará sus
    atributos y métodos y añadirá los suyos.
    
    Attributes
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
    surge_mode : bool
     Modo especial de un pokémon tipo agua en el que
     hace un poco más de daño al atacar.
    
    Methods 
    -------
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, surge_mode:bool): 
        Asigna atributos al objeto.
    check_surge_activation():
        Comprueba si el pokémon está en modo surge.
    water_attack(opponent: Pokemon) -> int:
        Reduce en n unidades la salud del oponente según un factor.
        Además, si el modo surge está activado, el pokémon del entrenador hace un poco más de daño.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, surge_mode:bool):
        '''
        Clase de los pokémos de tipo agua.
        Esta clase es hija de la clase Pokemon, por lo que heredará sus
        atributos y métodos y añadirá los suyos.
            
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
        surge_mode : bool
         Modo especial de un pokémon tipo agua en el que
         hace un poco más de daño al atacar.
        '''
        super().__init__(name, level, strength, defense, hp, total_hp, agility)
        self._surge_mode = surge_mode
        self._pokemon_type = 'Water'
    
    def check_surge_activation(self)-> bool:
        '''
        Comprueba si el pokémon está en modo surge.
        
        Returns 
        -------- 
        bool
         Resultado de comprobar si el modo surge está activado.
             True  : si está en modo surge.
             False : si no está en modo surge. 
        '''
        if self.surge_mode:
            return True
        else:
            return False
    
    def water_attack(self, opponent:Pokemon) -> int:
        '''
        Reduce en n unidades la salud del oponente según un factor.
        Además, si el modo surge está activado, el pokémon del entrenador hace un poco más de daño.
        Finalmente, la vida del oponente no puede ser inferior a 0 al terminar el ataque.
        
        Parameters 
        ---------- 
        opponent : Pokemon 
         Pokémon rival.
 
        Returns 
        --------
        damage : int
         Devuelve los puntos de daño inflingidos al contrincante. 
        '''
        if self.check_surge_activation():
            self.surge_mode = True
        else:
            self.surge_mode = False
        
        if opponent.pokemon_type == 'Fire':
            factor = 1.5
        elif opponent.pokemon_type == 'Water':
            factor = 1
        elif opponent.pokemon_type == 'Grass':
            factor = 0.5
        
        if self.surge_mode:
            factor += 0.1
        
        damage = int(floor(max(1, (factor*self.strength) - opponent.defense)))
        opponent.hp -= damage
        
        if opponent.hp < 0:
            opponent.hp = 0
        
        return damage
    
    def effectiveness(self, opponent:Pokemon) -> int:
        '''
        Implementación del método abstracto "effectiveness" para un WaterPokemon.
        Indica la efectividad de un WaterPokemon frente a las otras clases de pokémon.
 
        Parameters
        ---------- 
        opponent : Pokemon 
         Pokémon del entrenador rival.
 
        Returns 
        -------- 
        int
         Devuelve la efectividad del pokémon de agua contra los diferentes tipos:
             Contra un pokémon tipo Fuego:   1
             Contra un pokémon tipo Agua:    0 
             Contra un pokémon tipo Hierba: -1
        '''
        if opponent.pokemon_type == 'Fire':
            return 1
        elif opponent.pokemon_type == 'Water':
            return 0
        elif opponent.pokemon_type == 'Grass':
            return -1

    @property
    def surge_mode(self) -> str:
        return self._surge_mode

class FirePokemon(Pokemon):
    '''
    Clase de los pokémos de tipo fuego.
    Esta clase es hija de la clase Pokemon, por lo que heredará sus métodos y añadirá los suyos propios.
 
    Attributes
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
    temperature : float
     Temperatura del pokémon.
 
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, temperature:float): 
        Asigna atributos al objeto.
    fire_attack():
        Reduce los puntos de vida del oponente.
    embers():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
    '''
    
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, temperature:float):
        '''
        Asigna atributos al objeto. Heredado de la clase Pokemon.
        
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
        temperature : float
         Temperatura del pokémon.
        '''
        super().__init__(name, level, strength, defense, hp, total_hp, agility)
        self._temperature = temperature
        self._pokemon_type = 'Fire'
    
    def fire_attack(self, opponent:Pokemon)-> int:
        '''
        Ataque específico de un FirePokemon.
        Calcula el daño realizado al pokémon oponente.
        Además, la vida del oponente no puede ser inferior a 0 al terminar el ataque.
        
        Parameters 
        ----------
        opponent : Pokemon
         Pokémon del entrenador rival.
        
        Returns 
        -------- 
        damage : int
         Daño inflingido al oponente.
        '''
        if opponent.pokemon_type == 'Grass':
            factor = 1.5
        elif opponent.pokemon_type == 'Fire':
            factor = 1
        elif opponent.pokemon_type == 'Water':
            factor = 0.5 

        damage = int(floor(max(1, (factor*self.strength) - opponent.defense)))
        opponent.hp -= damage
        
        if opponent.hp < 0:
            opponent.hp = 0
        
        return damage
    
    def embers(self, opponent:Pokemon) -> int:
        '''
        Disminuye la vida del oponente n unidades de daño.
        Además, la salud del oponente no puede ser inferior a 0.
        
        Parameters 
        ----------
        opponent : Pokemon
         Pokémon del entrenador rival.
        
        Returns 
        -------- 
        damage : int
         Daño causado al oponente.
        '''
        damage = int(floor(self.strength*self.temperature))
        opponent.hp -= damage
        
        if opponent.hp < 0:
            opponent.hp = 0
        
        return damage
    
    def effectiveness(self, opponent:Pokemon) -> int:
        '''
        Implementación del método abstracto "effectiveness" para un FirePokemon.
        Indica la efectividad de un FirePokemon frente a las otras clases de pokémon.
 
        Parameters
        ---------- 
        opponent : Pokemon 
         Pokémon del entrenador rival.
 
        Returns 
        -------- 
        int
         Devuelve la efectividad del pokémon de agua contra los diferentes tipos:
             Contra un pokémon tipo Hierba:   1
             Contra un pokémon tipo Fuego:    0 
             Contra un pokémon tipo Agua:    -1
        '''
        if opponent._pokemon_type() == 'Grass':
            return 1
        elif opponent._pokemon_type() == 'Fire':
            return 0
        elif opponent._pokemon_type() == 'Water':
            return -1
    
    @property
    def temperature(self) -> str:
        return self._temperature

class GrassPokemon(Pokemon):
    '''
    Clase de los pokémos de tipo hierba.
    Esta clase es hija de la clase Pokemon, por lo que heredará sus métodos y añadirá los suyos propios.
     
    Attributes
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
    healing : float
     Curación del pokémon.
     
    Methods 
    ------- 
    __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, pokemon_type:str, healing:float): 
        Asigna atributos al objeto.
    basic_attack():
        Reduce los puntos de vida del oponente.
    is_debilitated():
        Indica si el pokémon tiene 0 puntos de vida.
    effectiveness():
        Método abstracto que indica la efectividad que el pokémon del entrenador tiene frente al pokémon rival. 
        '''
        
    def __init__(self, name:str, level:int, strength:int, defense:int, hp:int, total_hp:int, agility:int, healing:float):
        '''
        Asigna atributos al objeto. Heredado de la clase Pokemon.
            
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
        healing : float
         Curación del pokémon.
        '''
        super().__init__(name, level, strength, defense, hp, total_hp, agility, healing)
        self._healing = healing
        self._pokemon_type = 'Grass'
            
    def grass_attack(self, opponent:Pokemon)-> int:
        '''
        Disminuye la vida del oponente en n unidades de daño.
        Además, la vida del oponente no puede ser inferior a 0 al terminar el ataque.
        
        Parameters 
        ----------
        opponent : Pokemon
         Pokémon del entrenador rival.
        
        Returns 
        -------- 
        damage : int
         Daño infligido al pokémon del entrenador rival. 
        '''
        if opponent.pokemon_type == 'Water':
            factor = 1.5
        elif opponent.pokemon_type == 'Grass':
            factor = 1
        elif opponent.pokemon_type == 'Fire':
            factor = 0.5 

        damage = int(floor(max(1, (factor*self.strength) - opponent.defense)))
        opponent.hp -= damage
        
        if opponent.hp < 0:
            opponent.hp = 0
        
        return damage
           
    def heal(self)-> int:
        '''
        Cura el pokémon un máximo de n unidades.
        Además, la curación no puede superar los puntos de salud máximos al terminar la curación.
        
        Returns
        -------
        int
         Puntos de vida que ha recuperado el pokémon.
        '''
        cura = int(floor(self.healing*self.hp))
        self.hp += cura
        
        if self.hp > self.total_hp:
            self.hp = self.total_hp
        
        return cura
           
    def effectiveness(self, opponent:Pokemon) -> int:
        '''
        Implementación del método abstracto "effectiveness" para un GrassPokemon.
        Indica la efectividad de un GrassPokemon frente a las otras clases de pokémon.
 
        Parameters
        ---------- 
        opponent : Pokemon 
         Pokémon del entrenador rival.
 
        Returns 
        -------- 
        int
         Devuelve la efectividad del pokémon de agua contra los diferentes tipos:
             Contra un pokémon tipo Agua:     1        
             Contra un pokémon tipo Hierba:   0
             Contra un pokémon tipo Fuego:   -1 
        '''
        if opponent._pokemon_type() == 'Water':
            return 1
        elif opponent._pokemon_type() == 'Grass':
            return 0
        elif opponent._pokemon_type() == 'Fire':
            return -1
    
    @property
    def healing(self) -> str:
        return self._healing