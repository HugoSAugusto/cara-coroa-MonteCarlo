import random
import matplotlib.pyplot as plt

def jogar_moeda():
    return random.choice(["cara", "coroa"])

def simulacao_monte_carlo(quantidade_simu, lanc_x_simulacao):
    todas_diferencas = []
    
    for _ in range(quantidade_simu):  # Executa várias simulações
        cara_count = 0
        coroa_count = 0
        diferencas = []

        for _ in range(lanc_x_simulacao):  # 1000 lançamentos por simulação
            if jogar_moeda() == "cara":
                cara_count += 1
            else:
                coroa_count += 1
            
            diferencas.append(cara_count - coroa_count)  # Salva a diferença acumulada
        
        todas_diferencas.append(diferencas)  # Adiciona a simulação à lista principal
    
    return todas_diferencas

# Configuração das simulações
quantidade_simu = 100  # Número de simulações
lanc_x_simulacao = 1000  # Número de lançamentos por simulação

# Executa a simulação
resultados = simulacao_monte_carlo(quantidade_simu, lanc_x_simulacao)

# Criando o gráfico com todas as simulações
for resultado in resultados:
    plt.plot(range(1, lanc_x_simulacao + 1), resultado, alpha=0.5)  # alpha deixa as linhas mais transparentes

plt.xlabel("Quantidade de Lançamentos")
plt.ylabel("Diferença Cumulativa")
plt.title("Evolução da Diferença entre simulações")

plt.show()
