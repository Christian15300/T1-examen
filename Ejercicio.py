import pandas as pd
# Datos
data = {
    'Cantidad': [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05],
    '1': [1, 1, 1, 1, 1, 1, 2, 2, 4, 0, 0, 0],
}
# Crear el DataFrame
df = pd.DataFrame(data)
# Calcular la columna 'Restante'
# Aquí, se asume que la primera fila es 200 y se va restando conforme a la cantidad
df['Restante'] = [179.45, 79.45, 29.45, 9.45, 9.45, 4.45, 0.45, 0.45, 0.05, 0.05, 0.05, -1.1394E-14]
# Mostrar el DataFrame en pantalla
print(df)
# Para ver el DataFrame como una tabla
try:
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
except ImportError:
    print("Instala tabulate para ver el DataFrame como una tabla visual.")