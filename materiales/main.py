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
                temperature = details[6].split(': ')[1]
                pokemon = FirePokemon(name=pokemon_name, level=level, strength=strength, defense=defense, hp=hp, total_hp=total_hp, agility=agility, temperature=temperature)
                
            elif pokemon_type == 'Grass':
                healing = details[6].split(': ')[1]
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
    
    def str_ataque(self) -> str:
        pass

    def inicio(self):
        '''
        Selecciona los dos primeros pokémons que pelean e imprime un
        mensaje indicativo que muestra los pokémons elegidos.
        '''
        self.p1 = self.trainer1.select_first_pokemon()
        self.p2 = self.trainer2.select_first_pokemon()
        print(self.str_inicio())

    def combate(self):
        '''
        Gestiona el combate entre dos pokémons dados de ambos entrenadores dependiendo
        del número de ronda actual. Además, imprime un mensaje por cada ronda, indicando 
        el estado actual de los pokémons y otro mensaje por cada ataque realizado.
        '''
        while not (self.p1.is_debilitated() or self.p2.is_debilitated()):
            
            print(self.str_combate(self.round_number))

            if self.round_number % 2 == 1:
                if isinstance(self.p1, FirePokemon):
                    type_attack = 'fire_attack'
                    self.p1.fire_attack(self.p2)

                if isinstance(self.p1, GrassPokemon):
                    type_attack = 'grass_attack'           
                    self.p1.grass_attack(self.p2)

                if isinstance(self.p1, WaterPokemon):
                    type_attack = 'water_attack'
                    self.p1.water_attack(self.p2)

            else:
                self.p1.basic_attack(self.p2)
                self.p2.basic_attack(self.p1)
            
            self.round_number += 1

    def prioridad(self):
        pass
        

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
    Función principal que lee el archivo y comienza la simulación de la batalla.
    '''
    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        
        #Creación de la batalla entre trainer1 y trainer2:
        batalla = Batalla(trainer1= trainer1, trainer2= trainer2)
        
        #Inicio de la batalla entre los dos entrenadores:
        batalla.inicio()
        
        #Combate entre dos pokémons, cada uno siendo de cada entrenador respectivamente:
        batalla.combate()
        
        
    

if __name__ == '__main__':
    main()
