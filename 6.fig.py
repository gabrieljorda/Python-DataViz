import matplotlib.pyplot as plt
import numpy as np

#dados fictícios para os graficos 
x  = np.arange(1,6)
y1 = np.array([3,5,9,7,3])
y2 = np.array([1,6,2,8,4])

#Criando subplots

fig , ax = plt.subplots(2, figsize=(8,8))
# Gráfico de barras no subplot superior 
ax[0].bar(x,y1, color="skyblue")
ax[0].set_title("Gráfico de Barras")

# Gráfico de linhas no subplot inferior
ax[1].plot(x,y2, marker = "o", linestyle = "-",color="orange")

plt.show()
