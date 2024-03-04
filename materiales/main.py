import sys
from trainer import Trainer
from pokemon import Pokemon, FirePokemon, GrassPokemon, WaterPokemon

class PokemonSimulator:
    '''A class that simulates Pokemon trainers and their Pokemon.'''

    def create_trainer_and_pokemons(self, text:str):
        '''
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.
        
        Returns:
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
                temperature = details[6].split(': ')[1]
                pokemon = FirePokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, temperature)
                
            elif pokemon_type == 'Grass':
                healing = details[6].split(': ')[1]
                pokemon = GrassPokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, healing)

            elif pokemon_type == 'Water':
                surge_mode = False
                pokemon = WaterPokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, surge_mode)

            else: 
                raise ValueError(f'Invalid Pokemon type: {pokemon_type}')

            pokemons.append(pokemon)
        
        trainer = Trainer(name = trainer_name, pokemon = pokemons)
        return trainer

    def parse_file(self, text: str):                                    # Preguntar funcionalidad de esta función
        '''
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        '''

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2


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
    __init__(self, name:str, pokemon:list): 
        Asigna atributos al objeto.
    
    '''

    def __init__(self, trainer1:Trainer, trainer2:Trainer):
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
        cad_inicio = '===============================\nBattle between: {0} vs {1} begins!\n{2} chooses {3}\n{4} chooses {5}\n==============================='\
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
        cad_ronda = f'┌───────── Round {round} ─────────┐\n'

        primer_combatiente = 'Fighter 1: {0}({1}) Stats: Level:{2}, ATT:{3}, DEF:{4}, AGI:{5}, HP:{6}/{7}.\n'\
            .format(self.p1.name, self.p1.pokemon_type, self.p1.level, self.p1.strength, self.p1.defense, self.p1.agility, self.p1.hp, self.p1.total_hp)
        
        saegundo_combatiente = 'Fighter 2: {0}({1}) Stats: Level:{2}, ATT:{3}, DEF:{4}, AGI:{5}, HP:{6}/{7}.\n'\
            .format(self.p2.name, self.p2.pokemon_type, self.p2.level, self.p2.strength, self.p2.defense, self.p2.agility, self.p2.hp, self.p2.total_hp)

        actions = 'Actions\n'

        cad_combate = cad_ronda + primer_combatiente + saegundo_combatiente + actions
        return cad_combate

    def inicio(self):
        '''
        Selecciona los dos primeros pokémons que pelean e imprime un mensaje
        indicativo que muestra los pokémons elegidos.
 
        Returns 
        -------
        None.
        '''
        self.p1 = self.trainer1.select_first_pokemon()
        self.p2 = self.trainer2.select_first_pokemon()
        print(self.str_inicio())

    def combate(self):
        '''
        Gestiona el combate entre dos pokémons dados de ambos entrenadores.
 
        Returns 
        -------
        None.
        '''
        round_number = 1
        while not (self.p1.is_debilitated() or self.p2.is_debilitated()):
            print(self.str_combate(round_number))

            if round_number % 2 == 1:
                if self.p1.agility > self.p2.agility and isinstance(self.p1, FirePokemon):
                    self.p1.fire_attack(self.p2)

                if self.p1.agility > self.p2.agility and isinstance(self.p1, GrassPokemon):            
                    self.p1.grass_attack(self.p2)

                if self.p1.agility > self.p2.agility and isinstance(self.p1, WaterPokemon):            
                    self.p1.water_attack(self.p2)  






                if self.p1.agility >= self.p2.agility:
                    self.p1.type_attack(self.p2)
                    if self.p2.hp > 0:
                        self.p2.type_attack(self.p1)
                else:
                    self.p2.type_attack(self.p1)
                    if self.p1.hp > 0:
                        self.p1.type_attack(self.p2)




            else:
                self.p1.basic_attack(self.p2)
                self.p2.basic_attack(self.p1)
            
            round_number += 1


    @property
    def trainer1(self):
        return self._trainer1
    
    @property
    def trainer2(self):
        return self._trainer2
    
    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, pokemon_actual) -> Pokemon:
        if isinstance(pokemon_actual, Pokemon):
            self._p1 = pokemon_actual
        else:
            raise ValueError('El nuevo pokémon debe ser de tipo Pokemon.')
    
    @property
    def p2(self):
        return self._p2
    
    @p2.setter
    def p2(self, pokemon_actual) -> Pokemon:
        if isinstance(pokemon_actual, Pokemon):
            self._p2 = pokemon_actual
        else:
            raise ValueError('El nuevo pokémon debe ser de tipo Pokemon.')
    

def main():
    '''
    The main function that reads from a file and starts the simulation.
    '''
    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        print ("""TODO: Implement the rest of the practice from here. Define classes and functions and
        maintain the code structured, respecting the object-oriented programming paradigm""")
    

if __name__ == '__main__':
    main()
