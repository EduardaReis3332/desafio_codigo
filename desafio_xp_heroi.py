nome_heroi = input('Digite o nome do herói: ')
xp_heroi = int(input('Digite a quantidade de XP do herói: '))

nivel = ""

if xp_heroi <= 1000:
  nivel = "Ferro"
elif 1001 <= xp_heroi <= 2000:
  nivel = "Bronze"
elif 2001 <= xp_heroi <= 5000:
  nivel = "Prata"
elif 5001 <= xp_heroi <= 7000:
  nivel = "Ouro"
elif 7001 <= xp_heroi <= 8000:
  nivel = "Platina"
elif 8001 <= xp_heroi <= 9000:
  nivel = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
  nivel = "Imortal"
else:
  nivel = "Radiante"

repeticoes = 1
contador = 0

while contador < repeticoes:
  print(f"O Herói {nome_heroi} está no nível {nivel}. Parabéns pelo esforço!!")
  contador += 1