def calcular_nivel_rank(vitorias, derrotas):
  
  saldoRank = vitorias - derrotas

  if saldoRank <= 10:
    nivel = "Ferro"
  elif 11 <= saldoRank <= 20:
    nivel = "Bronze"
  elif 21 <= saldoRank <= 50:
    nivel = "Prata"
  elif 51 <= saldoRank <= 80:
    nivel = "Ouro"
  elif 81 <= saldoRank <= 90:
    nivel = "Diamante"
  elif 91 <= saldoRank <= 100:
    nivel = "Lendário"
  else:
    nivel = "Imortal"
  
  return saldoRank, nivel

vitorias = int(input("Digite a quantidade de vitórias do jogador: "))
derrotas = int(input("Digite a quantidade de derrotas do jogador: "))

saldoRank, nivel = calcular_nivel_rank(vitorias, derrotas)

print(f"O Herói tem um saldo de {saldoRank}, e está no nível de {nivel}.")