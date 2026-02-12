import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/Pedidos.csv')

#grafico quantidade vendidas por região 

plt.figure(figsize=(10,5))
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color="skyblue")
plt.title('Quantidade  de Unidades vendidas por região')
plt.xlabel('Região')
plt.ylabel('Quantidade de Unidades')
plt.xticks(rotation=45)
plt.show()

# grafico 2 distribuição das vendas por item 

plt.figure(figsize=(10,5))
df['Item'].value_counts().plot(kind='pie', autopct = '%1.1f%%', startangle = 90)
plt.title('Distribuição das vendas por item')
plt.xlabel('Item')
plt.axis('equal')
plt.show()

#grafico 3 relação entre preço unitário e quantidade de inidades
plt.figure(figsize=(10,5))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color = "orange"
)
plt.title('Relação entre preço unitário e quantidade de unidades')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de Unidades')
plt.grid(True)
plt.show()
