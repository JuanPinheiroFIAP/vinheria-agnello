#Fazendo o cadastro do cliente
print("Sejá Bem Vindo!\n\nVamos efetuar seu cadastro!")
print()
nome = input("Me informe seu nome completo: ")
print()
idade = int(input("Me informe sua idade: "))
print()
endereço_cliente = input("Me informe seu endereço: ")
print()
endereço_entrega = input("Me informe seu endereço entrega: ")
#Criand um valor de frete e de compra e um catalogo
frete = 50.0
valor = 0.0
quantidades = {}
#Craindo um catalogo de vinhos
catalogo_vinhos = {
        'vinho tinto': 50.0,
        'vinho branco': 40.0,
        'vinho rosé': 45.0,
        'prosecco': 60.0,
        'champagne': 100.0
}
#Chamando o codigo caso o cliente sejá maior de idade
if idade >= 18:
#Exibindo o catalogo de vinhos para o usuario
    print(f"Prontinho seu cadastro está feito.\nAqui está nosso catalogo de vinhos: {catalogo_vinhos.items()}")
#Perguntando quanto de cada vinho o usuario quer comprar
    for opcao in catalogo_vinhos:
        while True:
            quantidade = input(f"Quantas garrafas de {opcao} você deseja comprar? ")
            if quantidade.isdigit():
                quantidades[opcao] = int(quantidade)
                break
#caso o usuario coloque algum letra, o codigo mostra uma mensagem
            else:
                print("Opção inválida. Por favor, digite um número inteiro válido.")
#Pegando as quantidades de cada vinho e multiplicando pelo valor de cada um deles
    for opcao, quantidade in quantidades.items():
        preco = catalogo_vinhos[opcao]
        valor += preco * quantidade


#Criando uma condição para o frete
    if valor <= 100:
        print(f"Seu frete foi de R$: {frete}")
        valor_frete = frete + valor
    else:
        frete = 0
        valor_frete = valor + frete
        print("Frete gratis")

    print(quantidades)
    print(f"Sua compra deu R${valor_frete:.2f}")
    print(endereço_entrega)


#caso o cliente sejá menor de idade
else:
    print("Sinto muito mas o comprador tem que ser maior de idade.")
    print("Até mais!")