import random

def jogar_cara_ou_coroa():
    return random.choice(["cara", "coroa"])

def simulacao_monte_carlo():
    for i in range(500):
        caras = 0
        coroas = 0
        
        for i in range(1000):
            if jogar_cara_ou_coroa() == "cara":
                caras += 1
            else:
                coroas += 1
        
        print(f"Caras: {caras}, Coroas: {coroas}")

simulacao_monte_carlo()
