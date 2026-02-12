import matplotlib.pyplot as plt
import numpy as np

#dandos ficticios 
pontuacoes = np.random.randint(50, 100, 100)

# criando o histograma
plt.figure(figsize=(8,6))
plt.hist(pontuacoes, bins=10, color='blue', edgecolor='black')

# adicionando rotulos

plt.xlabel('Pontuacoes')
plt.ylabel('Frequencia')
plt.title('Histograma de Pontuacoes')

plt.show()
