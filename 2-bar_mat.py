import matplotlib.pyplot as plt

# dados ficticios - Quantidade de produtos vendidos por vendedores 

vendedores  = ["Joao", "Maria", "Pedro", "Ana", "Carlos", "Luisa", "Paulo", "Julia", "Marcos", "Fernanda"]

vendas = [150, 200, 180, 220, 190, 210, 230, 250, 200, 180]

#Criando o grafico de barra

plt.figure(figsize=(10,5))
plt.bar(vendedores, vendas,color="green")


#adicionando rotulos e titulos para o gráfico 

plt.xlabel("Vendedores")
plt.ylabel("Vendas")
plt.title("Vendas por Vendedor")


#exibindo o grafico 
plt.show()


