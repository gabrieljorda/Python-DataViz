import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1- criando um dataframe com dados ficticios 
data = {
    'Preço': [20,25,30,18,22],
    'Quantidade': [100,150,200,80,120],
    'Receita': [2000,3750,6000,1440,2640]
}

df = pd.DataFrame(data)

#2-Criando um pairplot usando seaborn
sns.set(style="ticks")
sns.pairplot(df,diag_kind = 'kde')
plt.suptitle('Pairplot dos Dados de Vendas', y=1.02)
plt.show()
