#RETO DE LA SEMANA 11. Módulos y funciones.

# Programa que crea listas y elimina los valores existentes en otras listas.

from m_retosemanal import crear_listas, eliminar_duplicados_posteriores

# Recolectar datos del usuario
num_listas = int(input("¿Cuántas listas? "))
datos = []
for i in range(num_listas):
    lon = int(input(f"Longitud lista {i+1}: "))
    datos.append(lon)
    for j in range(lon):
        val = input(f"Valor {j+1} lista {i+1}: ")
        datos.append(val)

# Usar funciones del módulo
listas_originales = crear_listas(num_listas, datos)

print("\n--- LISTAS ORIGINALES ---")
for i, lista in enumerate(listas_originales):
    print(f"Lista {i+1}: {lista}")

listas_modificadas = eliminar_duplicados_posteriores(listas_originales[:])

print("\n--- LISTAS MODIFICADAS SIN REPETICIONES ---")
for i, lista in enumerate(listas_modificadas):
    print(f"Lista {i+1}: {lista}")

