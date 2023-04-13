# print("Sejá Bem vindo ao nosso site!")
# print("Olá vamos efetuar seu cadastro no nosso site")
# nome = input("Me informe seu nome completo: ")
idade = int(input("Me informe sua idade: "))
# endereço_cliente = input("Me informe seu endereço: ")
# endereço_entrega = input("Me informe seu endereço entrega: ")
frete = 50
valor = 0.0
vinho_tinto = 50.0
vinho_branco = 40.0
vinho_rosé = 45.0
prosecco = 60.0
champagne = 100.0

catalogo_vinhos = {
        'vinho tinto': 50.0,
        'vinho branco': 40.0,
        'vinho rosé': 45.0,
        'prosecco': 60.0,
        'champagne': 100.0
    }
quantidades = {}

if idade >= 18:
    while True:
        opcao = input("Deseja comprar algum item nosso? (S/N)")
        if opcao.upper() == "S":
            print(catalogo_vinhos)

            for opcao in catalogo_vinhos:
                quantidade = int(input(f"Quantas garrafas de {opcao}"))
                quantidades[opcao] = quantidade

            for opcao, quantidade in quantidades.items():
                preco = catalogo_vinhos[opcao]
                valor += preco * quantidade
        elif opcao.upper() == "N":
            print("Compra finalizada!")
            break
        else:
            print("Opção invalida")



else:
    print("Sinto muito mas o comprador tem que ser maior de idade.")
    print("Até mais!")