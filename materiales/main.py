import sys

from trainer import Trainer
from pokemon import Pokemon, FirePokemon, GrassPokemon, WaterPokemon

class PokemonSimulator:
    '''
    Clase que simula la creación de los entrenadores pokémon.
    Los dos métodos de esta clase recibirán un input de texto y extraerán la
    información necesaria para la elaboración de los entrenadores y los
    pokémons que poseerán.

    Methods 
    ------- 
    create_trainer_and_pokemons(text:str):
        Crea un entrenador y le asigna sus pokémons, así como asignarles a
        estos últimos las propiedades necesarias.

    parse_file(text:str):
        Asigna los pokémons a cada entrenador y devuelve una lista de entrenadores.
    '''

    def create_trainer_and_pokemons(self, text:str):
        '''
        Crea un entrenador y sus pokémons a partir de un texto dado.

        Parameters
        ----------
        text : str
         Líneas de texto con la información necesaria sobre un entrenador y los
         pokémons que poseerá para el combate. La primera línea se corresponde
         con el nombre del entrenador, mientras que las siguientes con los diferentes
         detalles de los pokémons de ese mismo entrenador.
        
        Returns
        -------
        trainer : Trainer
         Entrenador creado a partir de la lista de pokémons previamente elaborada.
        '''

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0] # Extracting the pokemon's name
            details = parts[1].strip(')').split(', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            
            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = float(details[6].split(': ')[1])
                pokemon = FirePokemon(name=pokemon_name, level=level, strength=strength, defense=defense, hp=hp, total_hp=total_hp, agility=agility, temperature=temperature)
                
            elif pokemon_type == 'Grass':
                healing = float(details[6].split(': ')[1])
                pokemon = GrassPokemon(name=pokemon_name, level=level, strength=strength, defense=defense, hp=hp, total_hp=total_hp, agility=agility, healing=healing)

            elif pokemon_type == 'Water':
                surge_mode = False
                pokemon = WaterPokemon(name=pokemon_name, level=level, strength=strength, defense=defense, hp=hp, total_hp=total_hp, agility=agility, surge_mode=surge_mode)

            else: 
                raise ValueError(f'Tipo de pokémon no válido: {pokemon_type}')

            pokemons.append(pokemon)
        
        trainer = Trainer(name = trainer_name, pokemon = pokemons)
        return trainer

    def parse_file(self, text: str) -> list:
        '''
        Crea los entrenadores por separado y les asigna sus pokémons mediante la función
        create_trainer_and_pokemons().

        Parameters
        ----------
        text : str
         Texto que contiene la información de los entrenadores y sus pokémons.

        Returns
        -------
        list
         Lista de los entrenadores creados.
        '''

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return [trainer1, trainer2]


class Batalla:
    '''
    Clase de batalla entre dos entrenadores pokémon.
    Esta clase contiene las funciones necesarias para implementar tanto el inicio de la batalla
    entera, como el inicio del combate entre dos pokémons concretos, como la selección de un nuevo
    pokémon si el actual ha sido debilitado.
    
    Attributes 
    ---------- 
    trainer1 : Trainer
     Primer entrenador combatiente.
    trainer2 : Trainer 
     Segundo entrenador combatiente.
    
    Methods 
    ------- 
    __init__(self, trainer1:Trainer, trainer2:Trainer, round_number=1):
        Asigna atributos al objeto.
    
    str_inicio(self) -> str:
        Devuelve un string informativo al comienzo de la batalla.

    str_combate(self) -> str:
        Devuelve un string informativo al comenzar el combate entre dos pokémons.

    inicio(self):
        Selecciona los dos primeros pokémons e imprime un
        mensaje indicativo que muestra los pokémons que combatirán.

    prioridad(self) -> :

    combate(self):
        Gestiona el combate entre dos pokémons.
    
    prioridad(self):

    '''

    def __init__(self, trainer1:Trainer, trainer2:Trainer, round_number=1):
        '''
        Asigna atributos al objeto. 
 
        Parameters 
        ---------- 
        trainer1 : Trainer
         Primer entrenador combatiente.
        trainer2 : Trainer 
         Segundo entrenador combatiente.
        '''
        self._trainer1 = trainer1
        self._trainer2 = trainer2
        self._round_number = round_number
        self._p1 = Pokemon
        self._p2 = Pokemon
        
    def str_inicio(self) -> str:
        '''
        Devuelve un string informativo al inicio de la batalla entre dos entrenadores.
        
        Returns 
        ------- 
        cad_inicio : str
         Cadena informativa al inicio de la batalla.
        '''
        cad_inicio = '\n===============================\nBattle between: {0} vs {1} begins!\n{2} chooses {3}\n{4} chooses {5}\n===============================\n'\
        .format(self.trainer1.name, self.trainer2.name, self.trainer1.name, self.p1.name, self.trainer2.name, self.p2.name)
        
        return cad_inicio
    
    def str_combate(self, round:int) -> str:
        '''
        Devuelve un string informativo al comenzar el combate entre dos pokémons.
        
        Returns 
        ------- 
        cad_combate : str
         Cadena informativa al inicio del combate.
        '''
        cad_ronda = f'\n┌───────── Round {round} ─────────┐\n'

        primer_combatiente = 'Fighter 1: {0}({1}) Stats: Level:{2}, ATT:{3}, DEF:{4}, AGI:{5}, HP:{6}/{7}.\n'\
            .format(self.p1.name, self.p1.pokemon_type, self.p1.level, self.p1.strength, self.p1.defense, self.p1.agility, self.p1.hp, self.p1.total_hp)
        
        saegundo_combatiente = 'Fighter 2: {0}({1}) Stats: Level:{2}, ATT:{3}, DEF:{4}, AGI:{5}, HP:{6}/{7}.\n'\
            .format(self.p2.name, self.p2.pokemon_type, self.p2.level, self.p2.strength, self.p2.defense, self.p2.agility, self.p2.hp, self.p2.total_hp)

        actions = '\nActions:'

        cad_combate = cad_ronda + primer_combatiente + saegundo_combatiente + actions
        return cad_combate

    def inicio(self):
        '''
        Selecciona los dos primeros pokémons que pelean e imprime un
        mensaje indicativo que muestra los pokémons elegidos.
        '''
        self.p1 = self.trainer1.select_first_pokemon()
        self.p2 = self.trainer2.select_first_pokemon()
        print(self.str_inicio())

    def prioridad(self) -> Pokemon:
        '''
        Define qué pokémon atacará primero según la agilidad de ambos contrincantes.

        Returns 
        ------- 
        Pokemon
         Pokémon que atacará primero y, en segunda posición,
         el pokémon que atacará después.
        '''
        if self.p1.agility >= self.p1.agility:
            return (self.p1, self.p2)
        elif self.p1.agility < self.p1.agility:
            return (self.p2, self.p1)

    def ronda_impar(self, atacante:Pokemon, defensor:Pokemon) -> Pokemon:
        '''
        Gestiona el combate entre dos pokémons dados de ambos entrenadores si en
        número de ronda es par. Además, imprime un mensaje por cada ronda, indicando 
        información sobre el ataque y/o acción realizada.
        
        Parameters 
        ---------- 
        atacante : Pokemon
         Pokémon que realiza el ataque.
        defensor : Pokemon 
         Pokémon que recibe el ataque.
        
        Returns
        -------
        defensor : Pokemon
         Pokémon que recibe el ataque
        '''
        if isinstance(atacante, FirePokemon):
            type_attack = 'fire_attack'
            print(f'\n {atacante.name} uses a {type_attack} on {defensor.name}! (Damage: -{atacante.fire_attack(defensor)} HP: {defensor.hp})')
            if defensor.is_debilitated():
                print(f'\n {defensor.name} is debilitated.')
                return defensor
            print(f'\n {atacante.name} uses embers on {defensor.name}! (Damage: -{atacante.embers(defensor)} HP: {defensor.hp})')
            if defensor.is_debilitated():
                print(f'\n {defensor.name} is debilitated.')
            return defensor
                    
        if isinstance(atacante, GrassPokemon):
            type_attack = 'grass_attack'           
            print(f'\n {atacante.name} uses a {type_attack} on {defensor.name}! (Damage: -{atacante.grass_attack(defensor)} HP: {defensor.hp})')
            print(f'\n {atacante.name} is healing! (Healing: +{atacante.heal()} HP: {atacante.hp}) ')
            if defensor.is_debilitated():
                print(f'\n {defensor.name} is debilitated.')
            return defensor

        if isinstance(atacante, WaterPokemon):
            type_attack = 'water_attack'
            print(f'\n {atacante.name} uses a {type_attack} on {defensor.name}! (Damage: -{atacante.water_attack(defensor)} HP: {defensor.hp})')
            if defensor.is_debilitated():
                print(f'{defensor.name} is debilitated.')
            return defensor
    
    def ronda_par(self, atacante:Pokemon, defensor:Pokemon) -> Pokemon:
        '''
        Gestiona el combate entre dos pokémons dados de ambos entrenadores si en
        número de ronda es impar. Además, imprime un mensaje por cada ronda, indicando 
        información sobre el ataque realizado.
        
        Parameters 
        ---------- 
        atacante : Pokemon
         Pokémon que realiza el ataque.
        defensor : Pokemon 
         Pokémon que recibe el ataque.
        '''
        type_attack = 'basic_attack'
        print(f'\n {atacante.name} uses a {type_attack} on {defensor.name}! (Damage: -{atacante.basic_attack(defensor)} HP: {defensor.hp})')
        if defensor.is_debilitated():
            print(f'\n {defensor.name} is debilitated.')
        return defensor


    @property
    def trainer1(self) -> Trainer:
        return self._trainer1
    
    @trainer1.setter
    def trainer1(self, nuevo_entrenador):
        if isinstance(nuevo_entrenador, Trainer):
            self._trainer1 = nuevo_entrenador
        else:
            raise ValueError('El  entrenador debe ser de tipo Trainer.')
    
    @property
    def trainer2(self) -> Trainer:
        return self._trainer2
    
    @trainer2.setter
    def trainer2(self, nuevo_entrenador):
        if isinstance(nuevo_entrenador, Trainer):
            self._trainer2 = nuevo_entrenador
        else:
            raise ValueError('El entrenador debe ser de tipo Trainer.')
    
    @property
    def round_number(self) -> int:
        return self._round_number
    
    @round_number.setter
    def round_number(self, nueva_ronda):
        if isinstance(nueva_ronda, int) and nueva_ronda > 1:
            self._round_number = nueva_ronda
        else:
            raise ValueError('La ronda debe de ser un entero mayor que 1.')
    
    @property
    def p1(self) -> Pokemon:
        return self._p1

    @p1.setter
    def p1(self, pokemon_actual):
        if isinstance(pokemon_actual, Pokemon):
            self._p1 = pokemon_actual
        else:
            raise ValueError('El pokémon debe ser de tipo Pokemon.')
    
    @property
    def p2(self) -> Pokemon:
        return self._p2
    
    @p2.setter
    def p2(self, pokemon_actual):
        if isinstance(pokemon_actual, Pokemon):
            self._p2 = pokemon_actual
        else:
            raise ValueError('El pokémon debe ser de tipo Pokemon.')
    

def main():
    '''
    Función principal que lee el archivo y ejecuta la simulación de la batalla.
    '''
    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        tr1, tr2 = simulator.parse_file(pokemon_text)
        
        # Creación de la batalla entre trainer1 y trainer2:
        batalla = Batalla(trainer1= tr1, trainer2= tr2)
        
        # Inicio de la batalla entre los dos entrenadores:
        batalla.inicio()
        
        # Combate entre dos pokémons, uno atacante y otro defensor:
        atacante = batalla.prioridad()[0]
        defensor = batalla.prioridad()[1]
        
        if not batalla.trainer1.all_debilitated() and not batalla.trainer2.all_debilitated():
            
            while not atacante.is_debilitated() and not defensor.is_debilitated():
                
                if batalla.round_number % 2 == 1:
                    print(batalla.str_combate(batalla.round_number))
                    batalla.ronda_impar(atacante= atacante, defensor= defensor)
                    batalla.ronda_impar(atacante= defensor, defensor= atacante)
                    batalla.round_number += 1
                
                else:
                    print(batalla.str_combate(batalla.round_number))
                    batalla.ronda_par(atacante= atacante, defensor= defensor)
                    batalla.ronda_par(atacante= defensor, defensor= atacante)
                    batalla.round_number += 1
            
            if atacante.is_debilitated() and atacante in batalla.trainer1.pokemon:
                print(f'\n{batalla.trainer1.name} chooses {batalla.trainer1.select_next_pokemon(batalla.p2).name}!')
            if defensor.is_debilitated() and defensor in batalla.trainer2.pokemon:
                print(f'\n{batalla.trainer2.name} chooses {batalla.trainer1.select_next_pokemon(batalla.p1).name}!')
        
        # Si todos los pokémons de alguno de los entrenadores se debilita, imprime un mensaje de victoria:
        if batalla.trainer2.all_debilitated():
            ganador = batalla.trainer1
        if batalla.trainer1.all_debilitated():
            ganador = batalla.trainer2
    
        print(f'=================================\nEnd of the Battle: {ganador.name} wins!\n=================================')

if __name__ == '__main__':
    main()
