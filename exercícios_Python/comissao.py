porc_com = float(input("Qual a porcentagem da comissão?"))


def calc_comissao(porc_com, ven_total):
    return (ven_total * porc_com) + 5


def compra(num_laranjas, num_bananas, num_macas):
    print("Você comprou: \n", num_laranjas, 'laranjas\n',
          num_bananas, 'bananas\n',
          num_macas, 'maçãs\n')
    print('Olá, Bem Vindo a SoftFruits!')
    print('Hoje você comprou: \n', str(num_laranjas) + " laranjas \n",
          str(num_bananas) + " bananas \n",
          str(num_macas) + " maçãs")
    laranjas, bananas, macas = num_laranjas * 1.50, num_bananas * 1.00, num_macas * 2.00
    valor_total = laranjas + bananas + macas
    print("O valor total da compra é de: ", str(valor_total))
    comissao = calc_comissao(porc_com, valor_total)
    print("O valor da comissão nesta venda é de: ", str(comissao))


num_laranjas = int(input("Quantas laranjas você deseja? (valor unitário: R$1.50)"))
num_bananas = int(input("Quantas bananas você deseja? (valor unitário: R$1.00)"))
num_macas = int(input("Quantas maçãs você deseja? (valor unitário: R$2.00)"))
compra(num_laranjas, num_bananas, num_macas)
