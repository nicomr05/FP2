'''
Nicolás Muñiz Rodríguez : nicolas.muniz@udc.es
Pablo José Pérez Pazos : pablo.perez.pazos@udc.es
'''

from avl_tree import AVL
import pandas as pd

class Pandas:
    '''
    '''
    def __init__(self) -> None:
        '''
        Asigna atributos al objeto.

        Returns
        -------
        None
        '''
        self._dataframe = pd.DataFrame(columns=['Nombre', 'Duracion', 'Estudiantes', 'Nivel', 'Idioma', 'precio'])
    
    def estad_totales(self, arbol:AVL) -> tuple:
        '''
        Método que recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

        Returns
        -------
        tuple
         Tupla con tres valores: número de películas por director, media de puntuación del
         director y la media de puntuación por año.
        '''
        for curso in arbol:
            fila: dict = {'Director':curso.nombre}
            self.dataframe.loc[len(self.dataframe)] = fila # Añadimos cada diccionario al dataframe. Intentamos hacerlo con append pero daba error.
        
        return (self.peliculas_por_director(), self.media_director(), self.media_por_anho())
            
    def peliculas_por_director(self) -> None:
        '''
        Método que cuenta el número de películas por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Título'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['count']})
        print ("\n\n#############################################")
        print ("    Número de películas por director         ")
        print ("#############################################\n")
        print (data_directores)
    
    def media_director(self) -> None:
        '''
        Método que realiza la media de la puntuación por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        print ("\n\n#############################################")
        print ("    Puntuación media agrupada por director   ")
        print ("#############################################\n")
        print (data_directores)
    
    def media_por_anho(self) -> None:
        '''
        Método que realiza la media por año de estreno.

        Returns
        -------
        None
        '''
        group_col = 'Fecha'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        print ("\n\n#############################################")
        print ("    Puntuación media agrupada por año        ")
        print ("#############################################\n")
        print (data_directores)

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe