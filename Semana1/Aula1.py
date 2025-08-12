name = "João"
message = "Olá %s, tudo bem?" % name
print(message)

age = "\nMeu avô fez %d anos hoje, parabéns vovô!!!" % 95
print(age)

gift = "\nEstou sem um R$ %.2f para comprar um presente!!!" % 1.00
print(gift)

date = "\nHoje é dia %d/%d/%d ás %d:%d, puxa, viajei no tempo!!" % (26,18,1985,22,4)
print(date)

data = "\nFormatos diferentes: int={}, float={}, str={}".format(1, 1.5, "dois")
print(data)