import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#gerando dados aleatorios
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

#criando o gráfico de dispersão

plt.figure(figsize=(8,6))
plt.scatter(x,y,)
plt.title("Gráfico de Dispersão com dados aleatorios")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()


#criando um grafico 3d

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)

ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.grid(True)
ax.set_title("Gráfico 3D com dados aleatorios")
plt.show()