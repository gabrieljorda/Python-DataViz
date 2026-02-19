import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# O ciolinplot é útil para cisualizar a distribuição de uma variável numérica em diferentes categorias 

#1 - Criando um Dataframe com dados ficticios 
categorias = ["eletrônicos", "roupas", "alimentos", "móveis"]
vendas = {
    'categoria': np.random.choice(categorias, 1000),
    'vendas': np.random.normal(loc= 50, scale= 20, size = 1000)
}

df = pd.DataFrame(vendas)

#2- criando Violinplot com seaborn
plt.figure(figsize=(10,6))
sns.violinplot(x='categoria', y='vendas', data=df , palette='muted')
plt.title("Distribuição das Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Vendas")
plt.show()