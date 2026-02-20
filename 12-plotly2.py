import seaborn as sns
import plotly.express as px

#carregando o dataset Diamonds
diamonds = sns.load_dataset('diamonds')

print(diamonds.head())

#cirando gráfico de dispersão interatico com plotly

fig = px.scatter(
    diamonds,
    x='carat',
    y='price',
    color='cut',
    size='depth',
    hover_data=['x','y'],
    title='Relação entre Peso e Preço dos Diamantes'
)

#mostrando o grafico
fig.show()
