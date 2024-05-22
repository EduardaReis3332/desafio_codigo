def calcular_nivel_rank(vitorias, derrotas):
    
    saldoVitorias = vitorias - derrotas

    if vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldoVitorias, nivel

vitorias = int(input("Digite a quantidade de vitórias do jogador: "))
derrotas = int(input("Digite a quantidade de derrotas do jogador: "))

saldoVitorias, nivel = calcular_nivel_rank(vitorias, derrotas)

print(f"O Herói tem um saldo de {saldoVitorias}, está no nível de {nivel}.")