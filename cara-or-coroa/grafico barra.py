import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D"]
valores = [4, 7, 1, 8]

plt.bar(categorias, valores, color='green')

plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")

plt.show()
