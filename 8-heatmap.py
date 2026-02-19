import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Criando dados ficticios de preços de ações 
# para diferentes empresas ao Longo de trimestres

empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']

dados = np.random.rand(4, 4) * 100
# Valores aleatórios entre 0 a 100 para simular os preços das ações 

#2 - Criando um Dataframe com os dados 
df= pd.DataFrame(
    dados,
    columns=trimestres,
    index=empresas
)

#3 - criando o heatmap usando seaborn

plt.figure(figsize=(8,6))
sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Preços das Ações por Trimestre')
plt.xlabel('Trimestre')
plt.ylabel('Empresa')
plt.show()
