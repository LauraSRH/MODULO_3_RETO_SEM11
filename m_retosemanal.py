 #RETP SEMANA 11. Módulos y funciones.
#Programa que crea listas y elimina los valores existentes en otras listas, 
# 1. Todas las funciones empleadas deberán estar en un archivo m_retosemanal.py.
# 2. Crear varias listas; el usuario del programa especificará cuántas.
# 3. # La longitud de cada lista la definirá el usuario.
# 4. Que imprime las listas e indica que son las originales.
# 5. Eliminara los elementos de una lista que estén también en las listas posteriores.
# 6. # Imprime las listas indicando que se eliminaron los elementos que estaban,
# también, en las listas posteriores.

def crear_listas(num_listas, datos_listas):
    """"Crea varias listas según la cantidad y longitudes especificadas por el usuario."""
    listas = []
    indice = 0
    for i in range(num_listas):
        longitud = datos_listas[indice]      # datos_listas
        indice += 1
        lista = datos_listas[indice:indice + longitud]
        indice += longitud
        listas.append(lista)
    return listas


def eliminar_duplicados_posteriores(listas): 
    """Elimina los elementos de una lista que estén también en las listas posteriores."""
    for i in range(len(listas)):
        elementos_a_eliminar = set()
        for posterior in listas[i+1:]:
            elementos_a_eliminar.update(posterior)
        listas[i] = [elem for elem in listas[i] if elem not in elementos_a_eliminar]
    return listas