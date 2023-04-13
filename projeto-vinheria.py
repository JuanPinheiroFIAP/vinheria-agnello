print("Sejá Bem Vindo!\n\nVamos efetuar seu cadastro!")
print()
nome = input("Me informe seu nome completo: ")
print()
idade = int(input("Me informe sua idade: "))
print()
endereço_cliente = input("Me informe seu endereço: ")
print()
endereço_entrega = input("Me informe seu endereço entrega: ")
frete = 50.0
valor = 0.0
catalogo_vinhos = {
        'vinho tinto': 50.0,
        'vinho branco': 40.0,
        'vinho rosé': 45.0,
        'prosecco': 60.0,
        'champagne': 100.0
}
quantidades = {}
if idade >= 18:
    print(f"Prontinho seu cadastro está feito.\nAqui está nosso catalogo de vinhos: {catalogo_vinhos.items()}")
    for opcao in catalogo_vinhos:
        while True:
            quantidade = input(f"Quantas garrafas de {opcao} você deseja comprar? ")
            if quantidade.isdigit():
                quantidades[opcao] = int(quantidade)
                break
            else:
                print("Quantidade inválida. Por favor, digite um número inteiro válido.")
    for opcao, quantidade in quantidades.items():
        preco = catalogo_vinhos[opcao]
        valor += preco * quantidade
        print(f"Sua compra deu R${valor:.2f}")
    if valor <= 100:
        print(f"Seu frete foi de R$: {frete}")
    else:
        print("Frete gratis")
else:
    print("Sinto muito mas o comprador tem que ser maior de idade.")
    print("Até mais!")