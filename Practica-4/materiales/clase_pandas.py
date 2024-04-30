'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from avl_tree import AVL
import pandas as pd

class Pandas:
    '''
    Clase que calcula y gestiona las estadísticas de los cursos del árbol.
    '''
    def __init__(self) -> None:
        '''
        Asigna atributos al objeto.

        Returns
        -------
        None
        '''
        self._dataframe = pd.DataFrame(columns=['Nombre', 'Duracion', 'Estudiantes', 'Nivel', 'Idioma', 'Precio', 'Ingresos Totales'])
    
    def estad_totales(self, arbol:AVL) -> tuple:
        '''
        Método que recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

        Returns
        -------
        tuple
         Tupla con tres valores: número de estudiantes por idioma, nº medio de estudiantes
         por nivel y los ingresos totales posibles.
        '''
        for curso in arbol.values():
            fila: dict = {'Nombre':curso.nombre, 'Duracion':curso.duracion, 'Estudiantes':curso.estudiantes, 'Nivel':curso.nivel, 'Idioma':curso.idioma, 'Precio':curso.precio, 'Ingresos Totales':curso.beneficio}
            self.dataframe.loc[len(self.dataframe)] = fila # Añadimos cada diccionario al dataframe. Intentamos hacerlo con append pero daba error.
        
        return (self.estudiantes_por_idioma(), self.media_estudiantes_nivel(), self.ingresos_totales())
            
    def estudiantes_por_idioma(self) -> None:
        '''
        Método que cuenta el número de estudiantes por idioma.

        Returns
        -------
        None
        '''
        group_col: str = 'Idioma'
        target_col: str = 'Estudiantes'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['count']})
        
        cad: str = 'Número de estudiantes por idioma'
        n: int = 50

        print ('\n','#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')
    
    def media_estudiantes_nivel(self) -> None:
        '''
        Método que muestra el número medio de estudiantes por nivel.

        Returns
        -------
        None
        '''
        group_col: str = 'Nivel'
        target_col: str = 'Estudiantes'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        
        cad: str = 'Número medio de estudiantes por nivel'
        n: int = 50

        print ('\n','#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')
    
    def ingresos_totales(self) -> None:
        '''
        Método que muestra los ingresos totales posibles..

        Returns
        -------
        None
        '''
        target_col: str = 'Ingresos Totales'
        data_directores = self.dataframe.agg({target_col: ['sum']})
        
        cad: str = 'Ingresos totales posibles'
        n: int = 50

        print ('\n','#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe