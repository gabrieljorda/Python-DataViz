import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/Pedidos.csv ", sep=",")

#criando uma única figura com quatro subplots
fig , ax = plt.subplots(2, 2, figsize=(15,15))

#grágico 1 - quantidade de unicades vendidas por região
df.groupby("Regiao")["Unidades"].sum().plot(kind="bar", ax=ax[0,0], color="skyblue")
ax[0,0].set_title("Quantidade de Unidades Vendidas por Região")
ax[0,0].set_xlabel("Região")
ax[0,0].set_ylabel("Quantidade de Unidades Vendidas")
ax[0,0].tick_params(axis="x",rotation=45)


# grafico 2 distribuição das vendas por item 

df['Item'].value_counts().plot(kind='pie', autopct = '%1.1f%%', startangle = 90, ax=ax[0,1])
ax[0,1].set_title('Distribuição das vendas por item')
ax[0,1].set_xlabel('Item')
ax[0,1].axis('equal')


#grafico 3 relação entre preço unitário e quantidade de inidades
ax[1,0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color = "orange"
)
ax[1,0].set_title('Relação entre preço unitário e quantidade de unidades')
ax[1,0].set_xlabel('Preço Unitário')
ax[1,0].set_ylabel('Quantidade de Unidades')
ax[1,0].grid(True)


#grafico 4 quantidade de unidades vendidas ao longo do tempo
#convertendo coluna DataPedido para o formato de data
df["DataPedido"] = pd.to_datetime(df["DataPedido"])


df.groupby("DataPedido")["Unidades"].sum().plot(kind="line", color="green", marker ='o', ax=ax[1,1])
ax[1,1].set_title('Quantidade de Unidades vendidas ao longo do tempo')
ax[1,1].set_xlabel('Data do pedido')
ax[1,1].set_ylabel('Quantidade de Unidades vendidas')
ax[1,1].grid(True)

plt.tight_layout()

plt.show()
