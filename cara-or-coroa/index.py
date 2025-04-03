import random
import matplotlib.pyplot as plt

def jogar_cara_ou_coroa():
    return random.choice(["cara", "coroa"])

def simulacao_monte_carlo():
    caras = []
    coroas = []
    
    for i in range(500):  # 500 simulações
        cara_count = 0
        coroa_count = 0
        
        for i in range(1000):  # 1000 jogadas por simulação
            if jogar_cara_ou_coroa() == "cara":
                cara_count += 1
            else:
                coroa_count += 1
        
        caras.append(cara_count)
        coroas.append(coroa_count)
    
    return caras, coroas

# Executar a simulação e armazenar resultados
cara, coroa = simulacao_monte_carlo()

# Criando o gráfico de barras
plt.bar(["Caras", "Coroas"], [sum(cara) / len(cara), sum(coroa) / len(coroa)], color=['blue', 'green'])

plt.xlabel("Resultado")
plt.ylabel("Média de Ocorrências")
plt.title("Média de Caras e Coroas por Simulação")

plt.show()
