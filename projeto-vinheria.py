#rm552202 Juan Pinheiro de França
# Fazendo o cadastro do cliente
print("Seja Bem-Vindo!\n\nVamos efetuar seu cadastro!")
print()

nome = input("Me informe seu nome completo: ")
print()

idade = int(input("Me informe sua idade: "))
print()

endereco_cliente = input("Me informe seu endereço: ")
print()

endereco_entrega = input("Me informe seu endereço de entrega: ")

# Criando um valor de frete e de compra e um catálogo
frete = 50.0
valor = 0.0
quantidades = {}

# Criando um catálogo de vinhos com seus preços
catalogo_vinhos = {
    'vinho tinto': 50.0,
    'vinho branco': 40.0,
    'vinho rosé': 45.0,
    'prosecco': 60.0,
    'champagne': 100.0
}

# Verificando se o cliente é maior de idade
if idade >= 18:
    # Exibindo o catálogo de vinhos para o usuário
    print(f"Prontinho seu cadastro está feito.")
    print(f"Aqui está nosso catálogo de vinhos: {catalogo_vinhos}")

    # Perguntando quanto de cada vinho o usuário quer comprar
    for opcao in catalogo_vinhos:
        while True:
            quantidade = input(f"Quantas garrafas de {opcao} você deseja comprar? ")
            if quantidade.isdigit():
                quantidades[opcao] = int(quantidade)
                break
            else:
                # Caso o usuário digite uma entrada inválida, exibe uma mensagem de erro
                print("Opção inválida. Por favor, digite um número inteiro válido.")

    # Pegando as quantidades de cada vinho e multiplicando pelo valor de cada um deles
    for opcao, quantidade in quantidades.items():
        preco = catalogo_vinhos[opcao]
        valor += preco * quantidade

    # Criando uma condição para o frete
    if valor < 100:
        # Caso o valor da compra seja menor que 100, cobra o valor do frete
        print(f"Seu frete foi de R$: {frete:.2f}")
        valor_frete = frete + valor
    elif valor >= 100 and valor < 200:
        # Caso o valor da compra seja entre 100 e 200, o frete é grátis
        frete = 0
        valor_frete = valor + frete
        print("Frete grátis")
    else:
        # Caso o valor da compra seja maior que 200, o frete é grátis e exibe uma mensagem
        frete = 0
        valor_frete = valor + frete
        print("Frete grátis em compras acima de R$ 200.00")

    # Exibindo a quantidade de produtos comprados, o valor total da compra e o endereço de entrega
    print(f"Você comprou {sum(quantidades.values())} produtos no valor total de R${valor_frete:.2f}")
    print(f"Seu endereço de entrega é: {endereco_entrega}")
    print("Obrigado por comprar conosco!")
else:
    # Caso o cliente seja menor de idade
    print("Desculpe, não podemos vender bebidas alcoólicas para menores de idade.")
