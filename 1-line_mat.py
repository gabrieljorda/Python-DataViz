import matplotlib.pyplot as plt

# Dados ficticios - Vendas ao longo dos meses
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", ]
vendas = ["150", "200", "180", "220", "190", "210"]

# criando o grafico de linha 

plt.figure(figsize=(8,5))
plt.plot(
    meses,
    vendas,
    marker="o",
    linestyle="-",
    color="blue",
    label="Vendas"
)
#adicionando rótulos e titulo ao gáfico 
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.title("Vendas ao longo dos meses")
plt.legend()
plt.grid(True)


#Exibindo gráfico
plt.show()
