fim = 1
total = 0.0
valor = 0.0

while True:
    try:
        if fim == 1:
            nome = input("Digite o nome do produto: ")
            str_valor = input("Digite o valor da unidade: ").replace(',', '.')
            valor = float(str_valor)
            quantidade = int(input("Digite a quantidade desejada: "))
            total = total + (valor * quantidade)
            fim = int(input("Digite 1 para continuar ou 0 para finalizar: "))
        elif fim == 0:
            print("Finalizando o programa...")
            break
        elif fim != 1 or 0:
            print("Digite um valor válido.")
            fim = int(input("Digite 1 para continuar ou 0 para finalizar: "))
            continue
    except ValueError:
        print("Valor inválido.")

str_total = str(total).replace('.', ',')
print(f"O total do seu pedido é R${str_total}")