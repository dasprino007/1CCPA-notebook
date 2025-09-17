import datetime

idade = int(input("coloque sua idade por favor :"))
ano_atual = int(input("coloque o ano atual por favor :"))
aniversairo = input("Você ja fez aniversario :")

if aniversairo == "sim":
    nascimento = ano_atual - idade
else:
    nascimento = ano_atual - idade - 1

print(f"Voce nasceu em {nascimento}")

agora = datetime.datetime.now()
dia = agora.day
mes = agora.month
ano= agora.year

print(f"{dia}/{mes}/{ano}")