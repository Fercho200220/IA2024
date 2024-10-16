import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el CSV
csv_file = 'datos_bala 20.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(csv_file)

# Verificar los nombres de las columnas
print("Nombres originales de las columnas:", df.columns)

# Asegurarse de que no haya espacios adicionales en los nombres de las columnas
df.columns = df.columns.str.strip()

# Verificar nuevamente después de eliminar espacios
print("Nombres de las columnas después de limpiar espacios:", df.columns)

# Crear gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['Desplazamiento Bala'], df['Velocidad Bala'], label='Velocidad Bala', color='b')

# Etiquetas y título
plt.title('Gráfico de Dispersión: Desplazamiento vs Velocidad de la Bala')
plt.xlabel('Desplazamiento Bala')
plt.ylabel('Velocidad Bala')

# Mostrar leyenda y la gráfica
plt.legend()
plt.grid(True)
plt.show()
