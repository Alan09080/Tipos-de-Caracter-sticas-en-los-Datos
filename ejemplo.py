import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("titanic.csv")
print(df.head())

# Tipos de características
categóricas = df.select_dtypes(include=['object']).columns
continuas = df.select_dtypes(include=['float64', 'int64']).columns

# Asignar ejemplos
ordinales = ["Pclass"]  # Ejemplo de característica ordinal

print(f"Categóricas: {list(categóricas)}")
print(f"Continuas: {list(continuas)}")
print(f"Ordinales: {ordinales}")

# Distribución de datos categóricos:
sns.countplot(data=df, x='Sex', palette='pastel')
plt.title("Distribución por Género")
plt.show()

# Distribución de datos continuos:
sns.histplot(data=df, x='Age', kde=True, color='skyblue')
plt.title("Distribución de Edades")
plt.show()

# Distribución de datos ordinales:
sns.countplot(data=df, x='Pclass', palette='muted')
plt.title("Clases de Pasajeros")
plt.show()
