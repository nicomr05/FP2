import sys
from trainer import Trainer
from pokemon import Pokemon, FirePokemon, GrassPokemon, WaterPokemon

class PokemonSimulator:
    """A class that simulates Pokemon trainers and their Pokemon."""

    def create_trainer_and_pokemons(self, text:str):
        """
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.
        
        Returns:
        None: The function is currently set up to return None. Intended to return a Trainer instance in future development.
        """

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
                # TODO: Implement creation of a FirePokemon
                pokemon = FirePokemon(pokemon_name, level, strength, defense, hp, total_hp, agility, temperature)

                print ("TODO: Crear un FirePokemon - ", end="")
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, temperature: {temperature} ")
            elif pokemon_type == 'Grass':
                # TODO: Implement creation of a GrassPokemon
                healing = details[6].split(': ')[1]
                # Printing the attributes for now
                print ("TODO: Crear un GrassPokemon - ", end="")
                print (f"name: {pokemon_name},  level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, healing: {healing} ")
            elif pokemon_type == 'Water':
                surge_mode = False
                # TODO: Implement creation of a WaterPokemon
                print ("TODO: Crear un WaterPokemon - ", end="")
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, surge_mode: {surge_mode} ")
            else: 
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")

        # Reminder to implement the instance creation of Trainer
        print (f"TODO: Crear instancia de Trainer con nombre {trainer_name} y su lista de pokemon {pokemons} (primero deberas anadir los Pokemon creados a esta lista)\n\n")
        # Function is intended to return a Trainer instance in future development
        return None

    def parse_file(self, text: str):
        """
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        """

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
    metodo1(param1): 
    Una línea de resumen.
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
        Devuelve un string informativo al inicio de la batalla.
        
        Returns 
        ------- 
        cad_inicio : str
         Cadena informativa al inicio de la batalla.
        '''
        cad_inicio = '===============================\nBattle between: {0} vs {1} begins!\n{2} chooses {3}\n{4} chooses {5}\n==============================='\
        .format(self.trainer1.name, self.trainer2.name, self.trainer1.name, self.p1.name, self.trainer2.name, self.p2.name)
        
        return cad_inicio
    
    def inicio(self):
        '''
        Selecciona los dos primeros pokémons que pelean e imprime un mensaje
        indicativo que indica qué pokémons combatirán.
 
        Returns 
        -------- 
        None.
        '''
        self.p1 = self.trainer1.select_first_pokemon()
        self.p2 = self.trainer2.select_first_pokemon()
        print(self.str_inicio())
    
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